"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import json
import os
import pickle

class Evolver:

    # --------------------- Class initialisation
    def __init__(self, **settings):

        # -- User defined attributes
        for member_name, member_value in settings.items():
            setattr(self, member_name, member_value)

        # -- Infered attributes
        self.completed_generations = None


    # --------------------- Public functions
    def evolve(self):
        self.completed_generations = 10
        self._save()
        pass

    # --------------------- Private functions
    def _save(self):

        # Nothing to be saved
        if self.completed_generations is None:
            return

        # Save the object via pickle 
        pickle.dump(
            self, open(os.path.join(self.save_path, "evolver.pkl"), "wb"), protocol=4
        ) 
