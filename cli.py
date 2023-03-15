#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------- External libraries imports
import argparse
import json

# ------- Internal library imports
from pcgnca.utils import get_settings, get_evolver

# ------- Global vars definition
SETTINGS_LOAD_PATH = "settings/experiment/settings.json"
EXPERIMENT_SAVE_PATH = "experiments"

# ------- CLI arguments definition
parser = argparse.ArgumentParser(
    description='Control flow of CLI')

# -- Extraction flags
parser.add_argument('--train', action='store_true', default=False)
parser.add_argument('--evaluate', action='store_true', default=False)
parser.add_argument('--n_cores', action='store')
parser.add_argument('--n_generations', action='store')
parser.add_argument('--save_freq', action='store', default=100)


# -- Parse the arguments
args = parser.parse_args()

# ------- Execution based on flags
def main():

    # ASSERTIONS
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"
    assert args.n_generations is not None, "You must specify --n_generations flag denoting generations the archive should go through"

    # TRAINING
    if args.train:

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

if __name__ == '__main__':
    main()
