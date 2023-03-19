#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------- External libraries imports
import argparse
import json
import os

# ------- Internal library imports
from pcgnca.utils import get_settings, get_evolver, generate_fixed_tiles

# ------- Global vars definition
SETTINGS_LOAD_PATH = "settings"
EXPERIMENT_SAVE_PATH = "experiments"
GRAPHICS_PATH = os.path.join("assets", "games")

# ------- CLI arguments definition
parser = argparse.ArgumentParser(
    description='Control flow of CLI')

# -- Extraction flags
# --- Main activities
parser.add_argument('--train', action='store_true', default=False)
parser.add_argument('--evaluate', action='store_true', default=False)
parser.add_argument('--gen-fixed-seeds', action='store_true', default=False)

# --- Hyper-parameters for activities
parser.add_argument('--n_cores', action='store')
parser.add_argument('--n_generations', action='store')
parser.add_argument('--save_freq', action='store', default=100)

# ---- For fixed input seeds generation
parser.add_argument('--fixedgen-game', action='store')
parser.add_argument('--fixedgen-nseeds', action='store')
parser.add_argument('--fixedgen-difficulty', action='store')

# -- Parse the arguments
args = parser.parse_args()

# ------- Execution based on flags
def main():

    # TRAINING
    if args.train:

        # -- Assertions
        assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"
        assert args.n_generations is not None, "You must specify --n_generations flag denoting generations the archive should go through"

        # -- Load settings and path to save the experiment related files
        settings = get_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH)
        
        # -- Merge the experiment settings with cli args
        settings.update(vars(args))

        # -- Get evolver
        evolver = get_evolver(settings)

        # -- Finally, let the evolver do the training
        evolver.evolve()

    # EVALUATION
    if args.evaluate:
        pass

    # GENERATION OF FIXED SEEDS
    if args.gen_fixed_seeds:

        # Assertions
        assert args.fixedgen_game is not None, "Must specify for which game you want to generate fixed tiles."
        assert args.fixedgen_nseeds is not None, "Must specify how many seeds of fixed tiles you want to generate."
        assert args.fixedgen_difficulty is not None, "Must specify the difficulty of fixed tiles generation."

        # Generate and save the seeds
        generate_fixed_tiles(
            game=args.fixedgen_game,
            n_seeds=int(args.fixedgen_nseeds),
            difficulty=args.fixedgen_difficulty,
            path=SETTINGS_LOAD_PATH,
            graphics_path=os.path.join(GRAPHICS_PATH, args.fixedgen_game)
        )

if __name__ == '__main__':
    main()
