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
    obj_weights,
    extended_stats
):
    states_copy = np.copy(init_states)
    return _simulate(model, states_copy, fixed_tiles, binary_mask, n_tile_types, n_steps, overwrite, obj_weights, extended_stats)

def _simulate(
    model,
    init_states,
    fixed_tiles,
    binary_mask,
    n_tile_types,
    n_steps,
    overwrite,
    obj_weights,
    extended_stats
):

    # - Initialise the evaluator
    evaluator = ZeldaEvaluation(init_states.shape[1], obj_weights)
 
    # - Let the model go over each init state for N steps
    # and collect the stats for each level generation
    batch_stats = []
    for state_i in range(len(init_states)):
        # -- Setup input for the model
        # --- Fixed tiles =
        # ---- if ovewrite is true, ovewrite model's output in the position of fixed tiles if neccessary
        # ---- add binary channel
        # ---- Rest same as with no fixed tiles (see below)
        if fixed_tiles is not None:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, fixed_tiles[state_i], binary_mask[state_i], overwrite)
        
        # --- NO fixed tiles =
        # ---- One hot encode the channels
        # ---- Convert the numpy array to PyTorch's tensor
        else:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types)

        for step in range(n_steps):

            # --- Run the single forward pass
            action = model(in_tensor)

            # -- Extract the level (now 2d int array)
            level = th.argmax(action[0], dim=0).numpy()

            # -- Setup the input for the model again
            if fixed_tiles is not None:
                in_tensor = _preprocess_input(level, n_tile_types, fixed_tiles[state_i], binary_mask[state_i], overwrite)
            else:
                in_tensor = _preprocess_input(level, n_tile_types)
    
        # -- Compute stats about the level (e.g. how many enemies, doors, keys etc.)
        level_stats = evaluator.get_zelda_level_stats(level)
        batch_stats.append(level_stats)

    
    # - Evaluate the batch of level stats
    return evaluator.evaluate_level_batch(batch_stats, extended_stats)

def _preprocess_input(seed, n_tile_types, fixed=None, bin_mask=None, overwrite=False):
    
    # --- Overwrite = Make sure that model always receive the fixed tiles
    if overwrite and fixed is not None:
        np.putmask(seed, bin_mask, fixed)

    # --- One hot encode the seed
    seed_encoded = (np.arange(n_tile_types) == seed[..., None]).astype(int)
    seed_encoded = seed_encoded.transpose(2, 0, 1)

    # --- Add binary channel
    if bin_mask is not None:
        bin_mask = bin_mask[np.newaxis, ...]
        seed_encoded = np.concatenate((seed_encoded, bin_mask), axis=0)

    # --- Convert to the Tensory instead of nd array
    in_tensor = th.unsqueeze(th.Tensor(seed_encoded), 0)

    return in_tensor