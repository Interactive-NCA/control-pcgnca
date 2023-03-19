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
    overwrite
):

    # - Initialise the evaluator
    evaluator = ZeldaEvaluation(binary_mask.shape[1])
 
    # - Let the model go over each init state for N steps
    # and collect the stats for each level generation
    batch_stats = []
    for state_i in range(len(init_states)):

        # -- Setup input for the model
        if fixed_tiles:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types, fixed_tiles[state_i], binary_mask[state_i], overwrite)
        else:
            in_tensor = _preprocess_input(init_states[state_i], n_tile_types)

        for step in range(n_steps):

            # --- Run the single forward pass
            action = model(in_tensor)

            # -- Extract the level (now 2d int array)
            level = th.argmax(action[0], dim=0)

            # -- Setup the input for the model again
            if fixed_tiles:
                in_tensor = _preprocess_input(init_states[state_i], n_tile_types, fixed_tiles[state_i], binary_mask[state_i], overwrite)
            else:
                in_tensor = _preprocess_input(init_states[state_i], n_tile_types)
    
        # -- Compute stats about the level (e.g. how many enemies, doors, keys etc.)
        level_stats = evaluator.get_zelda_level_stats(level)
        batch_stats.append(level_stats)

    
    # - Evaluate the batch of level stats
    



def _preprocess_input(seed, n_tile_types, fixed=None, bin_mask=None, overwrite=False):
    
    # --- Overwrite = Make sure that model always receive the fixed tiles
    if overwrite and fixed is not None:
        np.putmask(seed, bin_mask, fixed)

    # --- One hot encode the seed
    seed_encoded = (np.arange(n_tile_types) == seed[..., None]).astype(int)
    seed_encoded = seed_encoded.transpose(2, 0, 1)

    # --- Add binary channel
    seed_encoded = np.concatenate((seed_encoded, bin_mask), axis=0)

    # --- Convert to the Tensory instead of nd array
    in_tensor = th.unsqueeze(th.Tensor(seed_encoded), 0)

    return in_tensor