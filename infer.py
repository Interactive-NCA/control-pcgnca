"""
Delete this file when polishing repo.

For Lukas: This is how we could do inference in production.
"""

import pickle
import json
import random

import pandas as pd
from ribs.archives import ArchiveDataFrame

from pcgnca.evo._models import NCA, set_weights
from pcgnca.evo._simulate import _simulate

# Load the archive
print("-"*50)
df = ArchiveDataFrame(pd.read_csv("experiments/ExperimentId-6/trained_archive.csv"))
print(f"Number of models in the trained archive is {df.shape[0]}")

# Load the training seeds
with open("experiments/ExperimentId-6/training_seeds.pkl", "rb") as f:
    train_seeds = pickle.load(f)
print(f"Number of generations is {len(train_seeds)}")

# Load the exp settings
with open("experiments/ExperimentId-6/settings.json") as f:
    settings = json.load(f)

# Init model
# - Get the model object
model = NCA(settings["n_tiles"], settings["n_aux_chans"], settings["binary_channel"])

# - Get the weights of arbitrary model
model_id = random.randint(0, df.shape[0] - 1)
start = list(df.columns).index("solution_0")
weights = df.iloc[model_id, start:-1].to_numpy().flatten() # NOTICE: till -1 since last column is metadata

# - Set the models' weights
set_weights(model, weights=weights)

# Get the input for the model
# - Find out which generation is it from
model_generation = df.iloc[model_id, -1]
print(f"The selected model is from the generation n. {model_generation}")

# - Select one of the training seeds
init_state = train_seeds[model_generation]["init_states"]

# - TODO: here we can also consider the fixed tiles and corresponding bin mask
fixed_tiles = None
binary_mask = None

# - Infer objective function weights from the settings
obj_weights = {
        "playability" : settings["playability_weight"],
        "reliability": settings["reliability_weight"]
}

# - Run the model against the input
stats = _simulate(
    model,
    init_state,
    fixed_tiles,
    binary_mask,
    settings['n_tiles'],
    settings['n_steps'],
    settings['overwrite'],
    settings['padding_type'],
    obj_weights,
    "optimiser_stats",
    settings['bcs'],
    settings['include_diversity']
)

print("-"*50)
print("Key stats (Expected vs actual)")
print(f"Objective: {df.iloc[model_id, 4]} vs {stats[0]}")
print(f"Symmetry: {df.iloc[model_id, 2]} vs {stats[1]}")
print(f"Path-length: {df.iloc[model_id, 3]} vs {stats[2]}")
print("-"*50)
