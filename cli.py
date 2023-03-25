#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------- External libraries imports
import argparse
import json
import os

# ------- Internal library imports
from pcgnca.utils import get_settings, get_evolver, generate_fixed_tiles, get_experiments_summary

# ------- Global vars definition
SETTINGS_LOAD_PATH = "settings"
EXPERIMENT_SAVE_PATH = "experiments"
GRAPHICS_PATH = os.path.join("assets", "games")
SUMMARIES_PATH = "summaries"

# ------- CLI arguments definition
parser = argparse.ArgumentParser(
    description='Control flow of CLI')

# -- Extraction flags
# --- Main activities
parser.add_argument('--train', action='store_true', default=False)
parser.add_argument('--evaluate', action='store_true', default=False)
parser.add_argument('--summarise', action='store', type=str)
parser.add_argument('--gen-fixed-seeds', action='store_true', default=False)

# --- Hyper-parameters for activities
# ---- General
parser.add_argument('--n_cores', action='store', type=int)
parser.add_argument('--n_generations', action='store', type=int)
parser.add_argument('--save_freq', action='store', type=int)

# ---- For fixed input seeds generation
parser.add_argument('--fixedgen-game', action='store')
parser.add_argument('--fixedgen-nseeds', action='store', type=int)
parser.add_argument('--fixedgen-difficulty', action='store')

# -- Parse the arguments
args = parser.parse_args()

# ------- Helper functions
def load_evolver():

    # -- Assertions
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"
    assert args.n_generations is not None, "You must specify --n_generations flag denoting generations the archive should go through"
    assert args.save_freq is not None, "You must specify --save_freq flag denoting how often the archive of models should be saved."

    # -- Load settings and path to save the experiment related files
    settings = get_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH)
    
    # -- Merge the experiment settings with cli args
    settings.update(vars(args))

    # -- Get evolver
    evolver = get_evolver(settings)

    return evolver

# ------- Execution based on flags
def main():

    # TRAINING
    if args.train:
        # -- Load evolver
        evolver = load_evolver()

        # -- Finally, let the evolver do the training
        evolver.evolve()
    else:
        evolver = None

    # EVALUATION
    if args.evaluate:

        # -- Load evolver if neccesary
        if evolver is None:
            evolver = load_evolver()

        # -- Finally, evaluate the evolver's archive
        evolver.evaluate_archive()
    
    # MARKDOWN summary and comparioson of diffrent experiments
    if args.summarise:
        ids = [int(expid) for expid in args.summarise.split(",")]
        get_experiments_summary(ids, EXPERIMENT_SAVE_PATH, SUMMARIES_PATH)

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
