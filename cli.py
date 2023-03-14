#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ------- External libraries imports
import argparse
import json

# ------- Internal library imports
from pcgnca.utils import get_settings

# ------- Global vars definition
SETTINGS_LOAD_PATH = "settings/settings.json"
EXPERIMENT_SAVE_PATH = "experiments"

# ------- CLI arguments definition
parser = argparse.ArgumentParser(
    description='Control flow of CLI')

# -- Extraction flags
parser.add_argument('--train', action='store_true', default=False)
parser.add_argument('--evaluate', action='store_true', default=False)
parser.add_argument('--n_cores', action='store')


# -- Parse the arguments
args = parser.parse_args()


# ------- Execution based on flags
def main():

    # ASSERTIONS
    assert args.n_cores is not None, "You must specify --n_cores flag denoting how many cpu cores should be used"

    # TRAINING
    if args.train:

        # -- Load settings and path to save the experiment related files
        settings, save_path = get_settings(SETTINGS_LOAD_PATH, EXPERIMENT_SAVE_PATH)

    # EVALUATION
    if args.evaluate:
        pass

if __name__ == '__main__':
    main()
