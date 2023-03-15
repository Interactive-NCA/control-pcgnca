"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import json
import os
import pickle
# from ribs.optimizers import Optimizer
from ribs.archives import GridArchive

class Evolver:

    # --------------------- Class initialisation
    def __init__(self, **settings):

        # -- User defined attributes
        self._init(**settings)

        # -- Infered attributes
        self.completed_generations = None


    # --------------------- Public functions
    def evolve(self):
        self.completed_generations = 10
        self._save()
        pass

    # --------------------- Private functions (not exposed to cli)
    def _init_pyribs(self):
        pass

        """
        self.gen_archive = GridArchive(
            dims=[100, 100],
            ranges=[self.bc_bounds[bc_name] for bc_name in self.bc_names],
            **init_level_archive_args,
        )
        self.gen_optimizer = Optimizer(self.gen_archive, gen_emitters)
        """

    def _init(self, **settings):
        # -- Save the dict for later reference
        self.settings = settings

        # -- Set the user defined attributes
        for member_name, member_value in settings.items():
            setattr(self, member_name, member_value)

        # -- Set the infered attributes
        self._init_pyribs()

    def _show_exp_settings(self):
        exclude = ["logger", "save_path"]
        members = [[k, str(v)] for k, v in self.settings.items() if k not in exclude]
        self.logger.show_table("", ["Parameter", "Value"], members)

    def _save(self):

        # Nothing to be saved
        if self.completed_generations is None:
            return

        # Before saving, get rid of unpickable members
        self.logger = None
        self.settings = None

        # Save the object via pickle 
        pickle.dump(
            self, open(os.path.join(self.save_path, "evolver.pkl"), "wb")
        ) 
