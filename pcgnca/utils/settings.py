"""
Functions that help with handling the settings of the experimet.
"""

# --------------------- External libraries imports
import json
import os
import pickle

import numpy as np

# --------------------- Internal libraries imports
from ..evo import Evolver
from .logging import ScriptInformation

# --------------------- Private functions
def _load_settings(path):

    # Save the settings to dict
    settings = dict()

    # Load the experiment settings
    full_path = os.path.join(path, "experiment", "settings.json")
    with open(full_path, 'r') as f:
        exp_settings = json.load(f) 
        settings.update(exp_settings)
        settings["settings_to_log"] = exp_settings

    # Load the given game's settings
    game_settings_path = os.path.join(path, "games", f"{settings['game']}.json")
    with open(game_settings_path, 'r') as f:
        game_settings = json.load(f)
        settings.update(game_settings)
        settings["settings_to_log"].update(game_settings)

    # Load slurm settings
    slurm_set_path = os.path.join(path, "slurm", "settings.json")
    with open(slurm_set_path, 'r') as f:
        slurm_set = json.load(f)
        settings.update(slurm_set)

    return settings, game_settings, slurm_set

def _log_settings(settings, path, exp_name):

    # Create new save path 
    save_path = os.path.join(path, exp_name)

    # Check whether it is neccessary to log the settings
    experiment_exists = os.path.exists(save_path)
    if not experiment_exists:

        # Make the experiment folder
        os.makedirs(save_path)

        # Drop description of the experiment which will go into separate file
        desc = settings.pop("description", None)

        # Save the settings
        settings_path = os.path.join(save_path, "settings.json")
        with open(settings_path, "w") as f:
            json.dump(settings, f)

        # Save the description
        desc_path = os.path.join(save_path, "README.md")
        with open(desc_path, "w") as f:
            f.write(desc)

    return save_path

def _find_path_to_experiment(experiments_path, expid):
    path = None
    all_experiments = os.listdir(experiments_path)
    for exp_filename in all_experiments:
        if f"ExperimentId-{expid}" in exp_filename:
            path = os.path.join(experiments_path, exp_filename)
            break
    return path

# --------------------- Public functions
def from_experimentid_to_settings(load_path, experiments_path, expid, cli_args):
    # - Find the path to the experiment
    path = _find_path_to_experiment(experiments_path, expid)
 
    # - Assertion
    assert path is not None, f"Experiment with {expid} does not exist!"

    # - Get settings
    # -- Load it from the file
    with open(os.path.join(path, "settings.json")) as f:
        settings = json.load(f)

    # -- Update it with cli args
    settings.update(cli_args)

    # -- Finally, add logger and save path
    settings["save_path"] = path
    settings["settings_path"] = load_path
    settings["logger"] = ScriptInformation()
    
    return settings

def from_experimentid_to_evolver(load_path, experiments_path, expid, cli_args):

    # - Get settings
    settings = from_experimentid_to_settings(load_path, experiments_path, expid, cli_args)

    # - Get evolver
    evolver_path = os.path.join(settings["save_path"], "evolver.pkl")
    evolver = get_evolver(settings, evolver_path)

    return evolver, settings
 
def get_settings(load_path, save_path):
    """Loads experiments settings,
    saves it to the experiment folder (if not already),
    and returns new save path which incorporates the
    experiment name.
    """

    # Load the json file into dict
    settings, game_settings, slurm_settings = _load_settings(load_path)

    # Get experiment name based on Id
    exp_name = f"ExperimentId-{settings['experiment_id']}"

    # Save the settings dict to an experiment folder
    save_path = _log_settings(settings, save_path, exp_name)

    # Add save and settings path to settings dict
    settings["save_path"] = save_path
    settings["settings_path"] = load_path

    # Initialise logging
    settings["logger"] = ScriptInformation()

    return settings

def get_evolver(settings, evolver_path=None):
    """Loads the given evolver based on the save path:
    - path exists including the evolver.pkl -> continue in evolution
    - does not exist, the evolver needs -> start from scratch
    """

    # - Show the setup
    settings["logger"].section_start(":construction: Load evolver")

    # - Continue
    try:
        path = evolver_path if evolver_path else os.path.join(settings["save_path"], "evolver.pkl")
        evolver = pickle.load(open(path, "rb"))
        evolver._init(**settings)
        evolver.logger.working_on("Will start evolution using EXISTING archive")
    
    # - Start from scratch
    except Exception as e:
        evolver = Evolver(**settings)
        evolver.logger.working_on("Will start evolution from SCRATCH")

    return evolver