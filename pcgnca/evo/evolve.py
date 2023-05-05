"""
Key module in the whole library. Trains the archive of NCA models
according to the given experiment settings. 
"""

# --------------------- External libraries imports
import gc
import json
import shutil
import os
import time
import pickle
import logging
from distutils.dir_util import copy_tree

import numpy as np
import scipy.stats as st
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
        if self.fixed_tiles:
            self._load_fixed_tiles_arch()
        else:
            self.fixed_tiles_arch = None


    # --------------------- Public functions
    def evolve(self):

        self.logger.section_start(":microbe: Evolution")

        # - Keep track of latent seeds generated
        # the shape is: total_number of stored training batches x gen_num (1) x type (3) x batch_size (?) x dim (16) x dim (16)
        latent_seeds = {}

        # - Main training loop
        start_time = time.time()
        for itr in tqdm(range(self.completed_generations, int(self.n_generations))):

            # -- Request potential new models/elites from the optimizer
            gen_sols = self.scheduler.ask()

            # -- Get latent seeds
            init_states, fixed_states, binary_mask = self._get_latent_seeds(self.n_init_states, self.fixed_tiles_arch)

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

                # --- Logging
                tqdm.write(f"> {itr + 1} itrs completed after {time.time() - start_time:.2f}s")
                tqdm.write(f"  - Size: {self.gen_archive.stats.num_elites}")
                tqdm.write(f"  - Coverage: {self.gen_archive.stats.coverage}")  
                tqdm.write(f"  - QD Score: {self.gen_archive.stats.qd_score}")  
                tqdm.write(f"  - Max Obj: {self.gen_archive.stats.obj_max}")
                tqdm.write(f"  - Mean Obj: {self.gen_archive.stats.obj_mean}")
                
                # --- Save training seeds and set the latent seeds to None
                latent_seeds = self._save_training_seeds(latent_seeds)

                # --- Save the evolver 
                self._save()

    def evaluate_archive(self, eval_fold_root, settings_path, assets_path, fxd_til_generator, fixed_tile_type, fixed_tile_arch_size, n_evals, batch_size):
        
        # - Section intro
        self.logger.section_start(":mage: Evaluation of the trained archive")

        # - Check that evaluation folder with the given fixed input exists
        eval_fold_name = f"{fixed_tile_type}-{fixed_tile_arch_size}"
        eval_folder_path = os.path.join(eval_fold_root, eval_fold_name)
        if not os.path.exists(eval_folder_path):
            self.logger.working_on("Setting up the evaluation folder including the fixed seeds ...")
            # -- Create the folder 
            os.makedirs(eval_folder_path)

            # -- Create fixed tiles, TODO: make this more generalisable
            fxd_til_generator(
                game="zelda", 
                n_seeds=fixed_tile_arch_size,
                difficulty=fixed_tile_type,
                settings_path=settings_path,
                save_path=eval_folder_path,
                graphics_path=os.path.join(assets_path, "zelda")
            )

        # - Check that there is a file that includes seeds for the given number of evals and batch size
        self.logger.working_on("Loading seeds ...")
        seeds_path = os.path.join(eval_folder_path, f"nEvals{n_evals}-bSize{batch_size}.pkl")
        if os.path.exists(seeds_path):
            # -- Load it
            with open(seeds_path, "rb") as f:
                seeds = pickle.load(f)
        else:
            # -- Load fixed tiles archive
            filename = f"{fixed_tile_type}_{fixed_tile_arch_size}.npy"
            archive_path = os.path.join(settings_path, "fixed_tiles", "zelda", filename)
            fixed_tiles_arch = np.load(archive_path).astype(int)

            # -- Generate
            seeds = []
            for _ in range(n_evals):
                init_states, fixed_states, binary_mask = self._get_latent_seeds(batch_size, fixed_tiles_arch)
                seeds.append([init_states, fixed_states, binary_mask])

            # -- Save for future use by other experiments
            with open(seeds_path, "wb") as f:
                pickle.dump(seeds, f)

        # - If the given experiment has not been evaluated yet, then create its folder and
        # fill it with the common stuff
        exp_folder_path = os.path.join(eval_folder_path, f"ExperimentId-{self.experiment_id}")
        train_dir_path = os.path.join(exp_folder_path, "training_summary")
        if not os.path.exists(exp_folder_path):

            # - Prepare the new directory
            self.logger.working_on("Preparing directory ...")

            # -- Create its folder first
            os.makedirs(exp_folder_path)

            # -- Copy the neccessary content from the experiments folder
            # --- Folders: Archive snaps
            archive_snaps_path = os.path.join(self.save_path, "archive_snaps")
            copy_snaps_to = os.path.join(exp_folder_path, "archive_snaps")
            copy_tree(archive_snaps_path, copy_snaps_to)
            # --- Files: README.md, settings.json, trained_archive.csv
            file_names = ["README.md", "settings.json", "trained_archive.csv"]
            for f in file_names:
                old_path, new_path = os.path.join(self.save_path, f), os.path.join(exp_folder_path, f)
                shutil.copyfile(old_path, new_path)
    
            # -- Add training summary
            self.logger.working_on("Summarising trained archive ...")
            self._compute_archive_stats(self.gen_archive, train_dir_path, "objective", None)

        # - Get the perc of archive filled during training
        with open(os.path.join(train_dir_path, "objective_stats.json")) as f:
            sts = json.load(f)
            tr_arch_perc = sts["Perc. of Archive Filled"]


        # - Create folder for the requested evalutation
        # -- Define the path
        n_eval_b_size_fold_name = f"evals-nEvals{n_evals}-bSize{batch_size}"
        n_eval_b_size_fold_path = os.path.join(exp_folder_path, n_eval_b_size_fold_name)
        # -- Check whether there has been a same eval run before
        was_evaluated_before = False
        if os.path.exists(n_eval_b_size_fold_path):
            # --- Set the flag (used later)
            was_evaluated_before = True

            # --- Make a copy
            copy_path = n_eval_b_size_fold_path + "_copy"
            copy_tree(n_eval_b_size_fold_path, copy_path)

            # --- Erase the old eval folder
            shutil.rmtree(n_eval_b_size_fold_path)
        # -- Finally create the new folder
        os.makedirs(n_eval_b_size_fold_path)

        # - Summarise results for seeds with and without fixed tiles
        self._compute_archive_stats_on_unseen_seeds(fixed_tile_type, fixed_tile_arch_size, seeds, n_eval_b_size_fold_path, tr_arch_perc)

        # - Erase the copy of the given experiment folder if neccessary
        if was_evaluated_before:
            shutil.rmtree(copy_path)

    # --------------------- Private functions (not exposed to cli)
    def _get_conf_int(self, a, frac):
        return st.t.interval(frac, len(a)-1, loc=np.mean(a), scale=st.sem(a))

    def _aggregate_json_files(self, data, save_path, fname_ext):

        for eval_type, metrics in data.items():
            for metric_name, vals in metrics.items():

                # -- Compute the aggregate
                keys = list(vals[0].keys())
                result = dict()
                for k in keys:
                    k_vals = np.array([v[k] for v in vals])
                    result[f"95CI {k}"] = list(np.around(self._get_conf_int(k_vals, 0.95), 2))
                    result[f"MEAN {k}"] = round(np.mean(k_vals), 2)

                # -- Save it
                sp = os.path.join(save_path, f"{fname_ext}_{eval_type}", f"{metric_name}_stats.json")
                with open(sp, "w") as f:
                    json.dump(result, f)

    def _aggregate_figures(self, data, save_path, fname_ext, metrics):

        # - Init
        solutions = self.gen_archive.as_pandas()
        weights = np.array(solutions.loc[:, "solution_0":])

        # - Create the figures
        for tgo, dfs in data.items():

            # -- Aggregate the dfs using mean
            df_mean = pd.concat(dfs).groupby(level=0).mean()

            # -- Now use it to plot the figures
            for m in metrics:

                # -- Create a GridArchive based on the criteria
                # --- Initiliase the archive
                archive = GridArchive(
                    solution_dim=weights.shape[1],
                    dims=[v for v in self.n_models_per_bc],
                    ranges=[self.bcs_bounds[i] for i in range(len(self.bcs))]
                )
                # --- Add obtained solutions to the archive
                archive.add(weights, df_mean[m].to_numpy(), df_mean[self.bcs].to_numpy())

                # -- Create a visualisation of the archive
                title = f"{m} function value across archive"
                fig = self._get_archive_heatmap(title, archive)
                p = os.path.join(save_path, f"{fname_ext}_{tgo}", f"{m}.png")
                fig.savefig(p)
        

    def _get_evals_summary(self, eval_fold_path, save_path, n_evals, b_size):
        """Computes summary stats based on the folder with several eval runs 
        """

        # - Initial setup
        # -- Define folders to go over in each eval run
        to_go_over = ["fixed_tiles_evaluation_summary", "evaluation_summary"]
        # -- Define metrics
        metrics = ["objective", "reliability", "playability"]
        # -- Extension to the new folder names
        fname_ext = f"nE{n_evals}_bS{b_size}"
        # -- Create the new folders
        n_fold_names = [f"{fname_ext}_{core}" for core in to_go_over]
        for fld_name in n_fold_names:
            p = os.path.join(save_path, fld_name)
            if os.path.exists(p):
                shutil.rmtree(p)    
            os.makedirs(p)
        
        # - Collection of data
        data = {name: {} for name in to_go_over}
        figures_data =  {name: [] for name in to_go_over}
        for i in range(1, n_evals + 1):
            for tgo in to_go_over:

                # --- Collect stats data
                for m in metrics:
                    p = os.path.join(eval_fold_path, f"ev{i}", tgo, f"{m}_stats.json")
                    with open(p) as f:
                        d = json.load(f)
                        if m in data[tgo]:
                            data[tgo][m].append(d)
                        else:
                            data[tgo][m] = [d]
                
                # --- Collect figures data
                p = os.path.join(eval_fold_path, f"ev{i}", tgo, "models_stats.csv")
                figures_data[tgo].append(pd.read_csv(p))

        # - Aggregate and save 
        # -- Json files
        self._aggregate_json_files(data, save_path, fname_ext)
        # -- Figures
        self._aggregate_figures(figures_data, save_path, fname_ext, metrics)
        

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

    def _compute_archive_stats_on_unseen_seeds(self, fxd_tiles_diff, fxd_tiles_arch_size, seeds, save_path, tr_arch_perc):

        # INITIAL setup
        # -------------------- 
        # - Retrieve solutions from the archive as pandas df
        solutions = self.gen_archive.as_pandas()
        model_weights = np.array(solutions.loc[:, "solution_0":])

        # - Get setup of the evolver before going through evaluation
        # This to ensure that the state of evolve before and after evalution is the same
        overwrite = self.overwrite

        # EVALUATION running for N times
        # -------------------- 
        self.logger.working_on(f"Summarising performance of trained archive on UNSEEN seeds w/ ({fxd_tiles_diff}, {fxd_tiles_arch_size}) and w/out FIXED TILES ...")
        i = 1
        for init_states, fixed_states, binary_mask in tqdm(seeds):

            # CREATE new folder
            # --------------------
            save_to = os.path.join(save_path, f"ev{i}")
            os.makedirs(save_to)

            # FIXED tiles eval
            # --------------------
            self.logger.working_on(f"---------- ({i}) Seeds WITH fixed tiles")
            # -- Make sure overwriting is enabled
            # (this means that after each step, we make sure that fix tiles do not get changed)
            self.overwrite = True
            
            # - Evaluate the archive on seeds with fixed tiles --> since the fixed
            # -- Run and evaluate the models
            # --- If the model was not trained with bin channel, set the the bin mask to None
            if not self.binary_channel:
                df = self._get_gen_sols_stats(model_weights, init_states, fixed_states, None, "extended_stats")
            else:
                df = self._get_gen_sols_stats(model_weights, init_states, fixed_states, binary_mask, "extended_stats")
                        
            # -- Evalute the df and save the results
            self._compute_eval_archive_stats(df, model_weights, fixed_seeds=True, save_path=save_to, tr_arch_perc=tr_arch_perc)

            # -- Save the df with the stats
            fname = os.path.join(save_to, "fixed_tiles_evaluation_summary", "models_stats.csv")
            df.to_csv(fname, index=False)

            # NO FIXED tiles eval
            # -------------------- 
            self.logger.working_on(f"---------- ({i}) Seeds WITHOUT fixed tiles")
            # - Assertions
            # -- No fixed seeds no need for overwrite
            self.overwrite = False

            # - Evaluate the archive on seeds with NO fixed tiles
            # -- Run and evaluate the models
            # --- If model expects binary channel, create it (all zeros since there are no fixed tiles)
            if self.binary_channel:
                bin_mask_zeros = np.zeros((self.n_init_states, self.grid_dim, self.grid_dim))
                df = self._get_gen_sols_stats(model_weights, init_states, None, bin_mask_zeros, "extended_stats")
            # --- Else just let both fixed tiles and binary channel to be empty
            else:
                df = self._get_gen_sols_stats(model_weights, init_states, None, None, "extended_stats")

            # -- Evalute the df and save the results
            self._compute_eval_archive_stats(df, model_weights, fixed_seeds=False, save_path=save_to, tr_arch_perc=tr_arch_perc)

            # -- Save the df with the stats
            fname = os.path.join(save_to, "evaluation_summary", "models_stats.csv")
            df.to_csv(fname, index=False)

            # CLEANUP
            # --------------------
            self.overwrite = overwrite

            # UPDATE
            # --------------------
            i += 1

        # AGGREGATE the results accross eval runs
        # --------------------
        n_evals, b_size = len(seeds), seeds[0][0].shape[0]
        aggregate_save_path = os.path.join(save_path, "..")
        self._get_evals_summary(save_path, aggregate_save_path, n_evals, b_size)

    def _compute_eval_archive_stats(self, df, weights, fixed_seeds, save_path, tr_arch_perc):

        # - Define criteria of the archive to evaluate
        criterias = ["objective", "playability", "reliability"]

        # - Get dir name where to save the results
        fixed = "fixed_tiles_" if fixed_seeds else ""
        dirname = fixed + "evaluation_summary"
        dir_path = os.path.join(save_path, dirname)

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
            self._compute_archive_stats(archive, dir_path, criteria, tr_arch_perc)

    def _compute_archive_stats(self, archive, dir_path, filename, tr_arch_perc):

        # - Get the archive as df
        df = archive.as_pandas()

        # - Compute the summary
        # -- Core stats
        max_n_solutions = self.n_models_per_bc[0]*self.n_models_per_bc[1]
        stats = self._get_metric_summary(df["objective"])
        stats["Perc. of Archive Filled"] =  100*round(len(df)/(max_n_solutions), 2)

        # -- Optional
        # --- Number of generations (only in training summary)
        if tr_arch_perc is None:
            stats["Number of generations"] = self.completed_generations

        # --- Drop in terms of archive filled train to eval
        if tr_arch_perc is not None:
            stats["Number of perc. points drop (arch. fill.)"] = tr_arch_perc - stats["Perc. of Archive Filled"]

        # - Save the summary along with the csv version of the archive
        # -- Make directory
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
                        self.bcs,
                        self.include_diversity
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

    def _get_latent_seeds(self, batch_size, fxd_til_archive):

        # - Get the random initial states. Essenitally each seed is
        # 2D array where each cell contains int encoding tile type
        # Since we may have multiple seeds, the result is a 3D array
        init_states = np.random.randint(
            low=0, high=self.n_tiles, size=(batch_size, self.grid_dim, self.grid_dim)
        )

        # - If certain tiles should be fixed,
        # generate semi-random fixed tiles (semi = still have to conform to game rules),
        # and adjust the init_states accordingly. Finally, add binary
        # channel that denotes which encodes the fixed tile positions
        if fxd_til_archive is not None:

            # -- Sample from the archive
            idx = np.random.randint(low=0, high=len(fxd_til_archive), size=batch_size)
            fixed_tiles_sample = fxd_til_archive[idx] # 3D array

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