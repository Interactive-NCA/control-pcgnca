"""
This module includes code to simulate level generation via a SINGLE model.
"""

# --------------------- External libraries import
import ray
import torch as th
import numpy as np

# --------------------- Internal libraries import
from ._evaluate import ZeldaEvaluation

@ray.remote
def simulate(
    model,
    init_states,
    fixed_tiles,
    binary_mask,
    n_tile_types,
    n_steps,
    overwrite,
    padding_type,
    obj_weights,
    to_return,
    bcs,
    incl_diversity
):
    states_copy = np.copy(init_states)
    return _simulate(model, states_copy, fixed_tiles, binary_mask, n_tile_types, n_steps, overwrite, padding_type, obj_weights, to_return, bcs, incl_diversity)

def _simulate(
    model,
    init_states,
    fixed_tiles,
    binary_mask,
    n_tile_types,
    n_steps,
    overwrite,
    padding_type,
    obj_weights,
    to_return,
    bcs,
    incl_diversity
):

    # - Initialise the evaluator
    evaluator = ZeldaEvaluation(init_states.shape[1], obj_weights, n_tile_types, bcs, incl_diversity)

    # - Let the model go over each init state for N steps
    # and collect the stats for each level generation
    batch_stats = []
    batch_steps_levels = []
    for state_i in range(len(init_states)):
        # -- Setup input for the model
        # --- Fixed tiles with bin mask =
        # ---- if ovewrite is true, ovewrite model's output in the position of fixed tiles if neccessary
        # ---- add binary channel
        # ---- Rest same as with no fixed tiles (see below)
        if fixed_tiles is not None and binary_mask is not None:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, padding_type, fixed_tiles[state_i], binary_mask[state_i], overwrite)

        # --- Only fixed tiles =
        # ---- if ovewrite is true, ovewrite model's output in the position of fixed tiles if neccessary
        # ---- Rest same as with no fixed tiles
        elif fixed_tiles is not None:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, padding_type, fixed_tiles[state_i], None, overwrite)

        # --- Only bin mask =
        # ---- Add bin channel
        # ---- Rest same as with no fixed tiles
        elif binary_mask is not None:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, padding_type, None, binary_mask[state_i], overwrite)
        
        # --- NO fixed tiles and Bin mask=
        # ---- One hot encode the channels
        # ---- Convert the numpy array to PyTorch's tensor
        else:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, padding_type)
        
        # -- Run the forward pass for n_steps
        levels = [] # keeps track of generated levels after each step
        aux_channels = []
        for _ in range(n_steps):

            # --- Run the single forward pass
            action, aux = model(in_tensor)

            # --- Extract the level (now 2d int array)
            level = th.argmax(action[0], dim=0).numpy()

            # --- Save the levels
            aux_channels.append(aux.numpy()) # get all aux channels
            levels.append(level)

            # --- Setup the input for the model again
            if fixed_tiles is not None and binary_mask is not None:
                in_tensor = _preprocess_input(level, n_tile_types, padding_type, fixed_tiles[state_i], binary_mask[state_i], overwrite)
            elif fixed_tiles is not None:
                in_tensor = _preprocess_input(level, n_tile_types, padding_type, fixed_tiles[state_i], None, overwrite)
            elif binary_mask is not None:
                in_tensor = _preprocess_input(level, n_tile_types, padding_type, None, binary_mask[state_i], overwrite)
            else:
                in_tensor = _preprocess_input(level, n_tile_types, padding_type)

        # -- Reset the auxiliary channels for the next input seed to zero
        model.reset()

        # -- Evaluate the episode accordingly 
        # --- Compute stats about the level (e.g. how many enemies, doors, keys etc.)
        batch_steps_levels.append(levels)
        level_stats = evaluator.get_zelda_level_stats(level)
        batch_stats.append(level_stats)
    
    # - Evaluate the batch accordingly
    if to_return == "generated_lvls":
        extended_stats = evaluator.evaluate_level_batch(batch_stats, np.array(batch_steps_levels), "extended_stats")
        return np.array(batch_steps_levels), np.array(aux_channels), evaluator.get_zelda_level_stats(level), extended_stats
    else:
        return evaluator.evaluate_level_batch(batch_stats, np.array(batch_steps_levels), to_return)

def _preprocess_input(seed, n_tile_types, padding_type, fixed=None, bin_mask=None, overwrite=False):
    
    # --- Overwrite = Make sure that model always receive the fixed tiles
    if overwrite and fixed is not None:  
        np.putmask(seed, (fixed > 0).astype(int), fixed)

    # --- One hot encode the seed
    seed_encoded = (np.arange(n_tile_types) == seed[..., None]).astype(int)
    seed_encoded = seed_encoded.transpose(2, 0, 1)

    # --- Pad the one hot encoded seed 
    seed_encoded = np.pad(seed_encoded, ((0,0), (1,1), (1,1)), mode='constant', constant_values=padding_type)

    # --- Add binary channel
    if bin_mask is not None:
        # ---- Pad the binary mask
        bin_mask = np.pad(bin_mask, 1, mode="constant", constant_values=0)

        # ---- Add it to the encoded seeds
        bin_mask = bin_mask[np.newaxis, ...]
        seed_encoded = np.concatenate((seed_encoded, bin_mask), axis=0)

    # --- Convert to the Tensory instead of nd array
    in_tensor = th.unsqueeze(th.Tensor(seed_encoded), 0)

    return in_tensor