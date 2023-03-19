"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import json
import os
import pickle

import numpy as np
from ribs.archives import GridArchive
from ribs.schedulers import Scheduler
from ribs.emitters import EvolutionStrategyEmitter
from tqdm import tqdm

# --------------------- Internal libraries imports
from ._models import NCA, get_init_weights

class Evolver:

    # --------------------- Class initialisation
    def __init__(self, **settings):
        """Called when starting from Scratch.
        """

        # - User defined attributes
        self._init(**settings)

        # - Infered attributes
        self.completed_generations = 0

        # - Setup the model
        self._init_model()

        # - Setup the optimiser
        self._init_pyribs()

        # - Load the fixed tiles if neccesary
        self._load_fixed_tiles_arch()


    # --------------------- Public functions
    def evolve(self):

        # - Main training loop
        for itr in tqdm(range(self.completed_generations, int(self.n_generations) + 1)):

            # -- Request potential new models/elites from the optimizer
            gen_sols = self.gen_optimizer.ask()

            # -- Get latent seeds
            init_states, fixed_states, binary_mask = self._get_latent_seeds()

            # -- Run stats about each solutions' performance
            objs, bcs = self._get_gen_sols_stats(gen_sols)

            # -- Send the stats back to the optimiser
            self.gen_optimizer.tell(objs, bcs)

            # -- Increment the number of completed generations
            self.completed_generations += 1

            # -- Save the evolver if neccessary
            if itr % 100:
                self._save()

    # --------------------- Private functions (not exposed to cli)
    def _get_gen_sols_stats(self, gen_sols):

        # - Compute how many models can run simultaneously based
        # on the number of available cores
        n_sols = len(gen_sols)
        n_launches = np.ceil(n_sols / self.n_cores)

        # - Collect results (obj, bcs) for each model
        # TODO: call set weights in here
        results = []
        for n_launch in range(int(n_launches)):
            futures = [
                multi_evo.remote(
                    self.env,
                    self.gen_model,
                    model_w,
                    self.n_tile_types,
                    init_states,
                    self.bc_names,
                    self.static_targets,
                    self.env.unwrapped._reward_weights,
                    fixed_tiles,
                    seed,
                    player_1=self.player_1,
                    player_2=self.player_2,
                    door_coords=self.door_coords,
                )
                for model_w in gen_sols[n_launch * self.n_cores: (n_launch+1) * self.n_cores]
            ]
            results += ray.get(futures)
            del futures
            auto_garbage_collect()
        
        # - Parse the results into the expected format

    def _load_fixed_tiles_arch(self):
        """
        Loads an archive (3D np array) of grid with semi-randomly generated
        levels.
        """
        if self.fixed_tiles:
            fxtiles_settings_path = os.path.join(self.settings_path, "fixed_tiles", f"{self.game}.npy")
            self.fixed_tiles_arch = np.load(fxtiles_settings_path)
        else:
            self.fixed_tiles_arch = None

    def _get_latent_seeds(self):

        # - Get the random initial states. Essenitally each seed is
        # 2D array where each cell contains int encoding tile type
        # Since we may have multiple seeds, the result is a 3D array
        init_states = np.random.randint(
            low=0, high=self.n_tiles, size=(self.n_init_states, *self.grid_dim)
        )

        # - If certain tiles should be fixed,
        # generate semi-random fixed tiles (semi = still have to conform to game rules),
        # and adjust the init_states accordingly. Finally, add binary
        # channel that denotes which encodes the fixed tile positions
        if self.fixed_tiles_arch is not None:

            # -- Sample from the archive
            idx = np.random.randint(low=0, high=len(self.fixed_tiles_arch), size=self.n_init_states)
            fixed_tiles_sample = self.fixed_tiles_arch[idx] # 3D array

            # -- Create binary mask
            binary_mask = (fixed_tiles_sample > 0).astype(int) # IMPORTANT: fixed tiles means 1 to 7, you can not fix 0 (empty)

            # -- Overwrite the init_state tiles with fixed tiles
            np.putmask(init_states, binary_mask, fixed_tiles_sample)

            return init_states, fixed_tiles_sample, binary_mask

        return init_states, None, None

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
