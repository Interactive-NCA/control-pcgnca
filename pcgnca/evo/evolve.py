"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import json
import os
import pickle

from ribs.archives import GridArchive
from ribs.schedulers import Scheduler
from ribs.emitters import EvolutionStrategyEmitter

# --------------------- Internal libraries imports
from ._models import NCA, get_init_weights

class Evolver:

    # --------------------- Class initialisation
    def __init__(self, **settings):
        """Called when starting from Scratch.
        """

        # -- User defined attributes
        self._init(**settings)

        # -- Infered attributes
        self.completed_generations = None

        # -- Setup the model
        self._init_model()

        # -- Setup the optimiser
        self._init_pyribs()


    # --------------------- Public functions
    def evolve(self):
        self.completed_generations = 10
        self._save()

    # --------------------- Private functions (not exposed to cli)
    def _from_name_to_model(self, name):
        # - Overview of all models
        mapping = {
            "NCA" : NCA
        }

        # - Make sure the requested model is available
        assert name in mapping, "The specified model does not exist in the models.py"

        # - Initialise the model
        if name == "NCA":
            model = mapping[name](self.n_tiles, self.n_aux_chans, self.binary_channel)

        # - Return the PyTorch model
        return model

    def _init_model(self):
        # - Get the selected model (PyTorch instance)
        self.gen_model = self._from_name_to_model(self.model_name)

    def _init_pyribs(self):
        # - Get initial random weights of the model
        initial_w = get_init_weights(self.gen_model)

        # - Define archive
        self.gen_archive = GridArchive(
            solution_dim=len(initial_w),
            dims=[100 for _ in self.bcs],
            ranges=[self.bcs_bounds[i] for i in range(len(self.bcs))]
        )

        # - Define emmiters
        # -- First, define hyper-parameters of the emmitter
        n_emitters, batch_size, ranker = 5, 30, "2imp"

        # -- Finally, initialize the emitters
        gen_emitters = [
            EvolutionStrategyEmitter(
                archive=self.gen_archive,
                x0=initial_w.detach(),
                sigma0=self.step_size,
                ranker=ranker,
                batch_size=batch_size,
            )
            for _ in range(n_emitters)
        ]

        # - Define scheduler using the archive and emitters
        self.scheduler = Scheduler(self.gen_archive, gen_emitters)

    def _init(self, **settings):
        # -- Save the settings dict for later reference
        self.settings = settings

        # -- Set the user defined attributes (hyper-parameters)
        for member_name, member_value in settings.items():
            setattr(self, member_name, member_value)

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
