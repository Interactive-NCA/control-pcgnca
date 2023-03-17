"""
Functions that help with handling the settings of the experimet.
"""

# --------------------- External libraries imports
import json
import os
import pickle

# --------------------- Internal libraries imports
from ..evo import Evolver
from .logging import ScriptInformation

# --------------------- Private functions
def _load_settings(path):

    # Load the experiment settings
    full_path = os.path.join(path, "experiment", "settings.json")
    with open(full_path, 'r') as f:
        settings = json.load(f) 

    # Load the given game's settings
    game_settings_path = os.path.join(path, "games", f"{settings['game']}.json")
    with open(game_settings_path, 'r') as f:
        game_settings = json.load(f)
        settings.update(game_settings)

    return settings, game_settings

def _log_settings(settings, path, exp_name):

    # Create new save path 
    save_path = os.path.join(path, exp_name)

    # Check whether it is neccessary to log the settings
    experiment_exists = os.path.exists(save_path)
    if not experiment_exists:

        # Make the experiment folder
        os.makedirs(save_path)

        # Save the settings
        settings_path = os.path.join(save_path, "settings.json")
        with open(settings_path, "w") as f:
            json.dump(settings, f)

    return save_path

def _get_experiment_name(settings, avoid):

    # Create a name:
    # use - to separate key value
    # use _ to separate parameters
    name = ""
    for key, value in settings.items():
        if key not in avoid:
            key = "".join([k[0].upper() + k[1:] for k in key.split("_")]) # to Camel Case
            name += f"{key}-{value}_" 

    # Get rid of the last underscore
    name = name[:-1]

    return name

# --------------------- Public functions
def get_settings(load_path, save_path):
    """Loads experiments settings,
    saves it to the experiment folder (if not already),
    and returns new save path which incorporates the
    experiment name.
    """

    # Load the json file into dict
    settings, game_settings = _load_settings(load_path)

    # Get experiment name based on the settings
    avoid = list(game_settings.keys()) # avoid adding these to the name
    exp_name = _get_experiment_name(settings, avoid=avoid)

    # Save the settings dict to an experiment folder
    save_path = _log_settings(settings, save_path, exp_name)

    # Add save path to settings
    settings["save_path"] = save_path

    # Initialise logging
    settings["logger"] = ScriptInformation()
    settings["logger"].script_time()
    settings["logger"].section_start(":construction: Experiment Setup")

    return settings

def get_evolver(settings):
    """Loads the given evolver based on the save path:
    - path exists including the evolver.pkl -> continue in evolution
    - does not exist, the evolver needs -> start from scratch
    """

    # - Continue
    try:
        evolver = pickle.load(open(os.path.join(settings["save_path"], "evolver.pkl"), "rb"))
        evolver._init(**settings)
        evolver.logger.working_on("Will start evolution using EXISTING archive with this experiment setup ...")
    
    # - Start from scratch
    except Exception as E:
        evolver = Evolver(**settings)
        evolver.logger.working_on("Will start evolution from SCRATCH with this experiment setup ...")

    # - Let user know about the result
    evolver._show_exp_settings()

    return evolver