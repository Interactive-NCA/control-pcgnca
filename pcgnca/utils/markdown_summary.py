"""
Module for automatic creation of markdown summaries about
the experiments' results. The idea is that you can summarise
one or more experiments at once.
"""

# --------------------- External libraries import
import json
import os
import pandas as pd

# --------------------- Public functions
def get_experiments_summary(experiment_ids, experiments_path, save_path):

    # -------- SETUP
    # - Based on IDs, get paths of experiment to evaluate
    paths = []
    all_experiments = os.listdir(experiments_path)
    for exp_filename in all_experiments:
        for expid in experiment_ids:
            if f"ExperimentId-{expid}" in exp_filename:
                path = os.path.join(experiments_path, exp_filename)
                paths.append((expid, path,))
                break

    # ------------- MAIN SECTION
    final_result = ""

    # -------- EXPERIMENT SETTINGS SUMMARY
    # - Heading
    heading = "### 🔮 About experiment(s)\n\n---\n\n"
    # - Collect the data about settings first
    data = _load_experiment_results(paths, "settings.json")
    # - Get the markdown summary 
    final_result += (heading + _get_experiment_results_summary(data, experiment_ids))

    # -------- TRAINING RESULTS SUMMARY
    # - Get experiment settings summary
    heading = "### 🔖 Training Process Summary\n\n---\n\n"
    # - Collect the data about settings first
    data = _load_experiment_results(paths, os.path.join("training_summary", "objective_stats.json"))
    # - Also the figures
    figures = _add_figures(paths, [os.path.join("training_summary", "objective.png")], experiment_ids)
    # - Get the markdown summary 
    final_result += (heading + _get_experiment_results_summary(data, experiment_ids) + figures)

    # -------- SAVE THE RESULTING MD DOC
    # - Save the markdown file
    filename = os.path.join(save_path, "summary_of_exps_" + "_".join([str(expid) for expid in experiment_ids]) + ".md")
    with open(filename, "w") as f:
        f.write(final_result)

# --------------------- Private functions
def _add_figures(exp_paths, figure_paths, expids):
    # - Save the paths of figures to data dict
    data = dict()

    # - Collect the data
    for fig_path in figure_paths:

        # -- Get the path of figures in the given row
        row = []
        for expid, exp_path in exp_paths:
            p = f"![]({os.path.join('..', exp_path, fig_path)})"
            row.append(p)

        # -- Get the name of the row
        row_name = fig_path.split(os.sep)[-1][:-4]
        data[row_name] = row
    
    # - Convert the df to markdown
    columns = [f"Experiment {i}" for i in expids]  
    result = pd.DataFrame.from_dict(data, orient='index', columns=columns).to_markdown()

    return result + "\n\n"

def _load_experiment_results(experiment_paths, result_path):

    data = dict()
    for expid, exp_path in experiment_paths:

        # --- Load the settings into a dict
        final_path = os.path.join(exp_path, result_path)
        with open(final_path) as f:
            d = json.load(f)

        # --- Save it to our data dict
        data[expid] = d

    return data

def _extract_nested_results(nested_results, expids):

    # - Save the results in dict where each key is row name
    # and each values includes row values
    result = dict()

    # - Go over all nested results
    for high_level_name, results in nested_results.items():

        # -- Extract the the row names
        result_names = list(results[expids[0]].keys())
        for i, result_name in enumerate(result_names):
            row = []

            # -- Finally, check the value of the result in each experiment
            for expid in expids:
                v = results[expid][result_name]
                v = v if v is not None else "0"
                row.append(v)
            result[high_level_name.upper() + " " + result_name] = row

    return result

def _get_experiment_results_summary(stats, expids):

    # - Save the data into a dict
    # where key is row name and values are row values
    data = dict()

    # - Get result names
    result_names = list(stats[expids[0]].keys())

    # - Collect nested results for later evaluation
    nested_results = dict()

    # - Do first round of parsing
    for i, result_name in enumerate(result_names):
        row = []
        for expid in expids:

            # -- Extract the value
            v = stats[expid][result_name]

            # -- Perform further actions
            # --- Nested result - save for later processing
            if type(v) == dict:
                if nested_results.get(result_name) is None:
                    nested_results[result_name] = {expid : v}
                else:
                    nested_results[result_name][expid] = v
            # --- Normal, save it straight away
            else:
                v = v if v is not None else "0"
                row.append(v)

        # - Only the row is non emtpy
        if len(row) > 0:
            data[result_name] = row

    # - Do second round of parsing
    data.update(_extract_nested_results(nested_results, expids))

    # - Turn the data into markdown via pandas 
    columns = [f"Experiment {i}" for i in expids] 
    final_result = pd.DataFrame.from_dict(data, orient='index', columns=columns).to_markdown()

    return final_result + "\n\n"