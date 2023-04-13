"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import gc
import json
import shutil
import os
import pickle
import logging

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psutil
from ribs.archives import GridArchive
from ribs.visualize import grid_archive_heatmap
from ribs.schedulers import Scheduler
from ribs.emitters import EvolutionStrategyEmitter
from tqdm import tqdm

import ray

# --------------------- Internal libraries imports
from ._models import NCA, get_init_weights, set_weights
from ._simulate import simulate

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

        self.logger.section_start(":microbe: Evolution")

        # - Keep track of latent seeds generated
        # the shape is: total_number of stored training batches x gen_num (1) x type (3) x batch_size (?) x dim (16) x dim (16)
        latent_seeds = {}

        # - Main training loop
        for itr in tqdm(range(self.completed_generations, int(self.n_generations))):

            # -- Request potential new models/elites from the optimizer
            gen_sols = self.scheduler.ask()

            # -- Get latent seeds
            init_states, fixed_states, binary_mask = self._get_latent_seeds()

            # -- Compute the objective values and BCs of the proposed solutions
            # --- STRATEGY 1: Compute objective values based on seeds with fixed tiles, BCs computed on seeds without fixed tiles
            if self.evolve_strategy == "obj_based_on_swft":
                # ---- Generate bin mask full of zeroes since this model expexts bin channel
                bin_mask_zeros = np.zeros((self.n_init_states, self.grid_dim, self.grid_dim))

                # ---- Retrive the stats as desribed above
                objs_without, bcs_without = self._get_gen_sols_stats(gen_sols, init_states, None, bin_mask_zeros, "optimiser_stats")
                objs_with, bcs_with = self._get_gen_sols_stats(gen_sols, init_states, fixed_states, binary_mask, "optimiser_stats")

                # ---- Save bcs and objs for comparison
                if (itr % self.save_freq) == 0:
                    n = len(gen_sols)
                    withoutfxs = [bcs_without[i] + [objs_without[i]] for i in range(n)]
                    withfxs = [bcs_with[i] + [objs_with[i]] for i in range(n)]
                    self._save_objs_bcs_for_comparison(withfxs, withoutfxs)

                # -- Add metadata for each added solution
                gen_number = self.completed_generations + 1
                meta = [gen_number for _ in range(len(gen_sols))]

                # ---- Send the stats back to the optimiser
                self.scheduler.tell(objs_with, bcs_without, meta)

            # --- STRATEGY DEFAULT: compute both objs and bcs based on given seeds
            # Note: given seeds can be either just seeds with no fixed tiles, or seeds with fixed tiles
            # This depends on the setting of the experiment
            else:
                # -- Evolve and compute the stats
                objs, bcs = self._get_gen_sols_stats(gen_sols, init_states, fixed_states, binary_mask, "optimiser_stats")

                # -- Add metadata for each added solution
                gen_number = self.completed_generations + 1
                meta = [gen_number for _ in range(len(gen_sols))]

                # -- Send the stats back to the optimiser
                self.scheduler.tell(objs, bcs, meta)

            # -- Increment the number of completed generations
            self.completed_generations += 1

            # -- Save the seeds on which the generation was trained
            # --- Collect the arrs in a list
            arrs = [init_states, fixed_states, binary_mask]

            # --- Create a dictionary out of the list
            new_d = self._get_training_seed_batch_to_add(arrs)

            latent_seeds.update(new_d) 

            # -- Save the evolver and its context info based on freq interval
            if (itr % self.save_freq) == 0:
                # Save training seeds and set the latent seeds to None
                latent_seeds = self._save_training_seeds(latent_seeds)

                # Save the evolver 
                self._save()

    def evaluate_archive(self):
        
        # - Section intro
        self.logger.section_start(":mage: Evaluation of the trained archive")
        
        # - Summarise the statistics about the trained archive
        # -- Remove the older folder if it exists indeed
        try:
            shutil.rmtree(os.path.join(self.save_path, "training_summary"))
        except Exception:
            pass

        # -- Create the new folder with the fresh content
        self.logger.working_on("Summarising trained archive ...")
        self._compute_archive_stats(self.gen_archive, "training_summary", "objective")

        # - Summarise results for seeds with and without fixed tiles
        self._compute_archive_stats_on_unseen_seeds()

    # --------------------- Private functions (not exposed to cli)
    def _get_training_seed_batch_to_add(self, arrs):        
        # - Create new dictionary
        new_dict = {
                    self.completed_generations:
                        {
                            "init_states": arrs[0],
                            "fixed_states": arrs[1],
                            "binary_mask": arrs[2]
                        }
                    }
        return new_dict

    def _save_training_seeds(self, seeds):
        # - Merge new training seeds with the existing seeds (if exists)
        filename = "training_seeds.pkl"
        path = os.path.join(self.save_path, filename)
        if os.path.exists(path):
            # -- Load
            with open(path, 'rb') as f:
                previous_seeds = pickle.load(f)
            # -- Merge
            previous_seeds.update(seeds)
        else:
            previous_seeds = seeds
        # - Save the seeds
        with open(path, 'wb') as f:
            pickle.dump(previous_seeds, f)
        
        return {}


    def _save_objs_bcs_for_comparison(self, withfxs, withoutfxs):

        # - Define the filename for storing the data
        filename = "objs_bcs_history.csv"

        # - Create Pandas DataFrame
        n = len(withfxs)
        df = pd.DataFrame(withoutfxs[i] + withfxs[i] for i in range(n))

        # - Add column names
        bc0_name, bc1_name = self.bcs[0], self.bcs[1]
        df.columns = [f"{bc0_name}_without", f"{bc1_name}_without", "obj_without", f"{bc0_name}_with", f"{bc1_name}_with", "obj_with"]

        # - If there is already dataframe, load it and add the results to it
        path = os.path.join(self.save_path, filename)
        if os.path.exists(path):
            # -- Load
            df_old = pd.read_csv(path)
            # -- Add 
            df = pd.concat([df, df_old], ignore_index=True)

        # - Save
        df.to_csv(path, index=False)

    def _compute_archive_stats_on_unseen_seeds(self):

        # INITIAL setup
        # -------------------- 
        # - Retrieve solutions from the archive as pandas df
        solutions = self.gen_archive.as_pandas()
        model_weights = np.array(solutions.loc[:, "solution_0":])

        # - Get setup of the evolver before going through evaluation
        # This to ensure that the state of evolve before and after evalution is the same
        fixed_tiles_archive = self.fixed_tiles_arch
        overwrite = self.overwrite

        # FIXED tiles eval
        # --------------------
        self.logger.working_on("Summarising performance of trained archive on NEW seeds with FIXED TILES ...")
        # - Assertions of assumptions
        # -- Make sure that fixed tiles archive is loaded --> this is to ensure that _get_latent_seeds generates also fixed states (tiles)
        if self.fixed_tiles_arch is None:
            self._load_fixed_tiles_arch() # it is now available under self.fixed_tiles_arch
        
        # -- Make sure overwriting is enabled
        # (this means that after each step, we make sure that fix tiles do not get changed)
        self.overwrite = True
        
        # - Evaluate the archive on seeds with fixed tiles --> since the fixed
        #   tiles archive is loaded, _get_latent_seeds knows to generate seeds with fixed tiles
        # -- Generate the seeds
        init_states, fixed_states, binary_mask = self._get_latent_seeds()

        # -- Run and evaluate the models
        df = self._get_gen_sols_stats(model_weights, init_states, fixed_states, binary_mask, "extended_stats")
        
        # -- Evalute the df and save the results
        self._compute_eval_archive_stats(df, model_weights, fixed_seeds=True)


        # NO FIXED tiles eval
        # -------------------- 
        self.logger.working_on("Summarising performance of trained archive on NEW seeds WITHOUT FIXED TILES ...")
        # - Assertions
        # -- Set the fixed tiles archive to none --> no fixed seeds
        self.fixed_tiles_arch = None

        # -- No fixed seeds no need for overwrite
        self.overwrite = False

        # - Evaluate the archive on seeds with NO fixed tiles
        # -- Generate the seeds
        init_states, fixed_states, binary_mask = self._get_latent_seeds()  # fixed states and bin mask is None
        assert fixed_states is None and binary_mask is None, "Incorrect evaluation setup!"

        # -- Run and evaluate the models
        # --- If model expects binary channel, create it (all zeros since there are no fixed tiles)
        if fixed_tiles_archive is not None:
            bin_mask_zeros = np.zeros((self.n_init_states, self.grid_dim, self.grid_dim))
            df = self._get_gen_sols_stats(model_weights, init_states, fixed_states, bin_mask_zeros, "extended_stats")
        # --- Else just let both fixed tiles and binary channel to be empty
        else:
            df = self._get_gen_sols_stats(model_weights, init_states, fixed_states, binary_mask, "extended_stats")
        
        # -- Evalute the df and save the results
        self._compute_eval_archive_stats(df, model_weights, fixed_seeds=False)

        # CLEANUP
        # --------------------
        self.fixed_tiles_arch = fixed_tiles_archive 
        self.overwrite = overwrite

    def _compute_eval_archive_stats(self, df, weights, fixed_seeds):

        # - Define criteria of the archive to evaluate
        criterias = ["objective", "playability", "reliability"]

        # - Get dir name where to save the results
        fixed = "fixed_tiles_" if fixed_seeds else ""
        dirname = fixed + "evaluation_summary"

        # - Erase the old directory if it exists
        try:
            shutil.rmtree(os.path.join(self.save_path, dirname))
        except Exception:
            pass

        # - Run evaluation of archive on that criteria
        for criteria in criterias:

            # -- Create a GridArchive based on the criteria
            # --- Initiliase the archive
            archive = GridArchive(
                solution_dim=weights.shape[1],
                dims=[v for v in self.n_models_per_bc],
                ranges=[self.bcs_bounds[i] for i in range(len(self.bcs))]
            )
            # --- Add obtained solutions to the archive
            archive.add(weights, df[criteria].to_numpy(), df[self.bcs].to_numpy())

            # -- Finally evalutate the archive
            self._compute_archive_stats(archive, dirname, criteria)

    def _compute_archive_stats(self, archive, dirname, filename):

        # - Get the archive as df
        df = archive.as_pandas()

        # - Compute the summary
        max_n_solutions = self.n_models_per_bc[0]*self.n_models_per_bc[1]
        stats = {
            filename : self._get_metric_summary(df["objective"]),
            "N. Solutions" : len(df),
            "N. Solutions Possible": max_n_solutions,
            "Perc. of Archive Filled": 100*round(len(df)/(max_n_solutions), 2),
            "Number of generations": self.completed_generations
        }

        # - Save the summary along with the csv version of the archive
        # -- Make directory
        dir_path = os.path.join(self.save_path, dirname)
        os.makedirs(dir_path, exist_ok=True)

        # -- Save the summary there as json
        with open(os.path.join(dir_path, f"{filename}_stats.json"), "w") as f:
            json.dump(
                stats, f
            )
        
        # -- Save the archive as csv
        csv_path = os.path.join(dir_path, f"{filename}_eval_archive.csv")
        df.to_csv(csv_path)
        
        # - Create a visualisation of the archive
        title = f"{filename} function value across archive"
        fig = self._get_archive_heatmap(title, archive)
        fig.savefig(os.path.join(dir_path, f"{filename}.png"))
    
    def _get_archive_heatmap(self, title, archive):
        fig, ax = plt.subplots(figsize=(8, 6))
        grid_archive_heatmap(archive, ax=ax, vmin=0, vmax=-25)
        ax.set_title(title)
        ax.set_xlabel(self.bcs[0])
        ax.set_ylabel(self.bcs[1])
        return fig

    def _get_metric_summary(self, metric):

        # - Save the data to dict
        summary = {}

        # - Define stats to compute
        stats = [
            ("Sum (QD score)", pd.DataFrame.sum),
            ("Mean", pd.DataFrame.mean),
            ("Std", pd.DataFrame.std),
            ("Min", pd.DataFrame.min),
            ("Max", pd.DataFrame.max)
        ]

        # - Compute and save the stats
        for stat_name, stat_fun in stats:

            # -- Metric is pandas series
            summary[stat_name] = stat_fun(metric)
        
        # - Return the stats
        return summary

    def _get_gen_sols_stats(self, gen_sols, init_states, fixed_tiles, binary_mask, to_return):

        # - Get bc weights - how important is each metric for the objective
        obj_weights = {
            "playability" : self.playability_weight,
            "reliability": self.reliability_weight
        }

        # - Compute how many models can run simultaneously based
        # on the number of available cores
        n_sols = len(gen_sols)
        n_launches = np.ceil(n_sols / self.n_cores)

        # - Collect results (obj, bcs) for each model
        results = []
        for n_launch in range(int(n_launches)):
            futures = [
                simulate.remote(
                        set_weights(self.gen_model, model_w),
                        init_states,
                        fixed_tiles,
                        binary_mask,
                        self.n_tiles,
                        self.n_steps,
                        self.overwrite,
                        self.padding_type,
                        obj_weights,
                        to_return,
                        self.bcs
                )
                for model_w in gen_sols[n_launch * self.n_cores: (n_launch+1) * self.n_cores]
            ]
            results += ray.get(futures)
            del futures
            self._auto_garbage_collect(80)
        
        # - Parse the results into the expected format
        if to_return == "extended_stats":
            df = pd.DataFrame.from_records(results, columns =["objective", "playability", "reliability"] + self.bcs)
            return df
        elif  to_return == "optimiser_stats":
            objs = [r[0] for r in results]
            bcs = [r[1:] for r in results]
            return objs, bcs
        else:
            raise Exception(f"Unexpected input for the parameter to_return: {to_return}")

    def _load_fixed_tiles_arch(self):
        """
        Loads an archive (3D np array) of grid with semi-randomly generated
        levels.
        """
        # - Load the archive with the fixed tiles
        if self.fixed_tiles:
            # -- Get path to the archive
            filename = f"{self.fixed_tiles_difficulty}_{self.fixed_tiles_archive_size}.npy"
            archive_path = os.path.join(self.settings_path, "fixed_tiles", self.game, filename)

            # -- Try to load it into the numpy array
            try:
                if self.fixed_tiles_difficulty == "manual":
                    self.fixed_tiles_arch = np.fromfile(archive_path, dtype=np.int32).reshape((-1, self.grid_dim, self.grid_dim))
                else:
                    self.fixed_tiles_arch = np.load(archive_path).astype(int)
            except Exception as e:
                raise Exception(f"Could not load the archive w/ fixed tiles! The erroe was {e}")
 
        # - No need to load it
        else:
            self.fixed_tiles_arch = None

    def _get_latent_seeds(self):

        # - Get the random initial states. Essenitally each seed is
        # 2D array where each cell contains int encoding tile type
        # Since we may have multiple seeds, the result is a 3D array
        init_states = np.random.randint(
            low=0, high=self.n_tiles, size=(self.n_init_states, self.grid_dim, self.grid_dim)
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
            dims=[v for v in self.n_models_per_bc],
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
        
        # -- Init ray for parallel processing
        ray.init(logging_level=logging.ERROR)
        self.logger.working_on("Successfully initialised RAY for parallel processing")

        # -- Run some assertions
        # --- Make sure that if you have fixed tiles you also have binary channel
        c1 = self.fixed_tiles and self.binary_channel
        c2 = not self.fixed_tiles and not self.binary_channel
        assert c1 or c2, "You can either have both fixed inputs and binary enabled completely disabled. (nothing in between)"
        
    def _show_exp_settings(self):
        members = [[k, str(v)] for k, v in self.settings["settings_to_log"].items()]
        self.logger.show_table("", ["Parameter", "Value"], members)

    def _save(self):

        # - Save the archive as csv
        df = self.gen_archive.as_pandas(include_metadata=True)
        df.to_csv(os.path.join(self.save_path, "trained_archive.csv"))

        # - Save the heatmap of the archive
        # -- Check the folder exists
        archive_snaps_path = os.path.join(self.save_path, "archive_snaps")
        if not os.path.exists(archive_snaps_path):
            os.mkdir(archive_snaps_path)
        
        # -- Get the figure and save it
        n_gens = self.completed_generations if self.completed_generations else 0 
        title = f"After {n_gens} generations"
        fig = self._get_archive_heatmap(title, self.gen_archive)
        fig.savefig(os.path.join(archive_snaps_path, f"ngens_{n_gens}.png")) 

        # - Save the evolver 
        if self.completed_generations is not None:

            # Before saving, get rid of unpickable members
            self.logger = None
            self.settings = None

            # Save the object via pickle 
            pickle.dump(
                self, open(os.path.join(self.save_path, "evolver.pkl"), "wb")
            ) 

    def _auto_garbage_collect(self, pct=80.0):
        if psutil.virtual_memory().percent >= pct:
            gc.collect() 