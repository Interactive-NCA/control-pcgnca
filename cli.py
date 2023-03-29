#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------- External libraries imports
import argparse
import json
import os

# ------- Internal library imports
from pcgnca.utils import get_settings, get_evolver, generate_fixed_tiles, \
get_experiments_summary, from_experimentid_to_evolver, get_slurm_file, from_experimentid_to_settings

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
parser.add_argument('--gen-slurm-script', action='store_true', default=False)
parser.add_argument('--gen-fixed-seeds', action='store_true', default=False)

# --- Hyper-parameters for activities
# ---- General
parser.add_argument('--n_cores', action='store', type=int)
parser.add_argument('--n_generations', action='store', type=int)
parser.add_argument('--save_freq', action='store', type=int)
parser.add_argument('--expid', action='store', type=int, default=None)

# ---- For slurm file generation
parser.add_argument('--timeout_after', action='store', type=str, default=None)

# ---- For fixed input seeds generation
parser.add_argument('--fixedgen-game', action='store')
parser.add_argument('--fixedgen-nseeds', action='store', type=int)
parser.add_argument('--fixedgen-difficulty', action='store')

# -- Parse the arguments
args = parser.parse_args()

# ------- Helper functions
# -------- Assertions (note that certain assetion function may overlap ...
# ... to me this is way clearer since you can look for each activity what exactly ...
# ... needs to be provided)
def run_training_assertions():
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"
    assert args.n_generations is not None, "You must specify --n_generations flag denoting generations the archive should go through"
    assert args.save_freq is not None, "You must specify --save_freq flag denoting how often the archive of models should be saved."

def run_evaluation_assertions():
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"
    assert args.expid is not None, "You specify which experiment you want to evalaute via --expid"

def run_gen_fixed_tiles_assertions():
    assert args.fixedgen_game is not None, "Must specify for which game you want to generate fixed tiles."
    assert args.fixedgen_nseeds is not None, "Must specify how many seeds of fixed tiles you want to generate."
    assert args.fixedgen_difficulty is not None, "Must specify the difficulty of fixed tiles generation."

def run_gen_slurm_file_assertions():
    # - General
    assert args.timeout_after is not None, "Must specify the max time the code should be running on the node" 
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"

    # - Train
    if args.train:
        run_training_assertions()
    
    # - Evaluate
    if args.evaluate:
        run_evaluation_assertions()

def load_evolver():

    # - Assertions
    # -- Assertions for train
    if args.train:
        run_training_assertions()

    # -- Asssertions for evaluate
    if args.evaluate:
        run_evaluation_assertions()

    # -- Load the evolver based on settings.json file
    if not args.expid:
        # -- Load settings and path to save the experiment related files
        settings = get_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH)
        
        # -- Merge the experiment settings with cli args
        settings.update(vars(args))

        # -- Get evolver
        evolver = get_evolver(settings)

        return evolver, settings

    # - Load the evolver based on the expids
    else:  
        evolver, settings = from_experimentid_to_evolver(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH, args.expid, vars(args))
    
        return evolver, settings

# ------- Execution based on flags
def main():

    # GENERATION OF SLURM SCRIPT
    if args.gen_slurm_script:
        # - Assertions
        run_gen_slurm_file_assertions()

        # - Starting from EXISTING experiment
        if args.expid:
            settings = from_experimentid_to_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH, args.expid, vars(args))
            get_slurm_file(settings, vars(args))

        # - Starting from SCRATCH 
        else:
            settings = get_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH) 
            settings.update(vars(args))
            get_slurm_file(settings, vars(args))
        
        # - Return to avoid running the script locally
        # - The file should be generated at this point
        return

    # TRAINING and EVALUATION
    # - Common
    if args.train or args.evaluate:
        # -- Load evolver and settings
        evolver, settings = load_evolver()

        # -- Show user the loaded settings
        evolver.logger.section_start(":crystal_ball: Experiment and Game settings")
        evolver._show_exp_settings()

    # - Train
    if args.train:
        evolver.evolve()

    # - Eval
    if args.evaluate:
        evolver.evaluate_archive()
    
    # MARKDOWN summary and comparison of different experiments
    if args.summarise:
        ids = [int(expid) for expid in args.summarise.split(",")]
        get_experiments_summary(ids, EXPERIMENT_SAVE_PATH, SUMMARIES_PATH)

    # GENERATION OF FIXED SEEDS
    if args.gen_fixed_seeds:

        # Assertions
        run_gen_fixed_tiles_assertions()

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
