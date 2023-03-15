"""
Functions that help with handling the settings of the experimet.
"""

# --------------------- External libraries imports
import json
import os
import pickle

# --------------------- Internal libraries imports
from ..evo import Evolver

# --------------------- Private functions
def _load_settings(path):
    with open(path, 'r') as f:
        settings = json.load(f) 
    return settings

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

def _get_experiment_name(settings):

    # Create a name:
    # use - to separate key value
    # use _ to separate parameters
    name = ""
    for key, value in settings.items():
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
    settings = _load_settings(load_path)

    # Get experiment name based on the settings
    exp_name = _get_experiment_name(settings)

    # Save the settings dict to an experiment folder
    save_path = _log_settings(settings, save_path, exp_name)

    # Add save path to settings
    settings["save_path"] = save_path

    return settings

def get_evolver(settings):
    """Loads the given evolver based on the save path:
    - path exists including the evolver.pkl -> continue in evolution
    - does not exist, the evolver needs -> start from scratch
    """

    # - Continue
    try:
        evolver = pickle.load(open(os.path.join(settings["save_path"], "evolver.pkl"), "rb"))
    
    # - Start from scratch
    except:
        evolver = Evolver(**settings)

    return evolver