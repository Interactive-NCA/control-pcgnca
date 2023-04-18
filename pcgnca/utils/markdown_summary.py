"""
Module for automatic creation of markdown summaries about
the experiments' results. The idea is that you can summarise
one or more experiments at once.
"""

# --------------------- External libraries import
import json
import os
import re
import glob
import pandas as pd

from PIL import Image

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
    
    # - Sort paths based on id
    paths = sorted(paths, key=lambda x: x[0])

    # ------------- MAIN SECTION
    final_result = ""

    # -------- EXPERIMENT SETTINGS SUMMARY
    # - Heading
    heading = "### 🔮 About experiment(s)\n\n---\n\n"
    # - Collect the data about settings first
    data = _load_experiment_results(paths, "settings.json")
    # - Include only the settings to log
    data = {k : d["settings_to_log"] for k, d in data.items()}
    # - Get the markdown summary 
    final_result += (heading + _get_experiment_results_summary(data, experiment_ids))

    # -------- TRAINING RESULTS SUMMARY
    # - Define proper heading
    heading = "### 🔖 Training Process Summary\n\n---\n\n"
    # - Collect the data about settings first
    data = _load_experiment_results(paths, os.path.join("training_summary", "objective_stats.json"))
    # - Also the figures
    figures = _add_figures(paths, [os.path.join("training_summary", "objective.png")], experiment_ids)
    # - And gifs
    # -- Generate gifs
    timeline_fold_paths = sorted([os.path.join(base, "archive_snaps") for _, base in paths])
    gif_paths = [_add_archive_timeline(fold_path) for fold_path in timeline_fold_paths]

    # -- Only add gifs if all experiments have them
    if None not in gif_paths:
        gifs = _add_figures(paths, [os.path.join("archive_snaps", "timeline.gif")], experiment_ids)
    else:
        gifs = ""

    # - Get the markdown summary
    final_result += (heading + _get_experiment_results_summary(data, experiment_ids) + figures + gifs)

    # -------- HISTORY OF OBJs and BCs
    history_summary = _summarise_obj_bcs_history(paths)
    if history_summary != "Not possible":
        final_result += f"### 👀 Training differences in Objs and BCs trained and evaluated on seeds with and without fixed seeds\n\n---\n\n"
        final_result += history_summary

    # -------- INDIVIDUAL metrics
    # - Define the section's structure
    subsections = [("fixed_tiles_evaluation_summary", "WITH"), ("evaluation_summary", "WITHOUT")]
    subsubsections = ["objective", "playability", "reliability"]

    # - Create the section 
    for subsec_folder, subsec_title in subsections:
        # -- Define heading
        final_result += f"### 🎯 Evaluation on seeds {subsec_title} Fixed tiles\n\n---\n\n"

        for subsec_file in subsubsections:

            # --- Add subheading
            final_result += f"👉 **{subsec_file.upper()}**\n\n"

            # --- Collect the data
            data = _load_experiment_results(paths, os.path.join(subsec_folder, f"{subsec_file}_stats.json"))
            
            # --- Also the figures
            figures = _add_figures(paths, [os.path.join(subsec_folder, f"{subsec_file}.png")], experiment_ids)

            # --- Get the markdown summary 
            final_result += (_get_experiment_results_summary(data, experiment_ids) + figures)

    # -------- SAVE THE RESULTING MD DOC
    # - Save the markdown file
    filename = os.path.join(save_path, "summary_of_exps_" + "_".join([str(expid) for expid in experiment_ids]) + ".md")
    with open(filename, "w") as f:
        f.write(final_result)

# --------------------- Private functions
def _summarise_obj_bcs_history(paths):

    # - Collect the stats
    raw = dict()
    row_names = ["bc0_diff", "bc1_diff", "obj_diff"]
    for i, path in paths:

        # -- Compute the differences
        filepath = os.path.join(path, "objs_bcs_history.csv")
        if not os.path.exists(filepath):
            return "Not possible"
        df = pd.read_csv(filepath)
        df[row_names[0]] = abs(df.iloc[:, 0] - df.iloc[:, 3])
        df[row_names[1]] = abs(df.iloc[:, 1] - df.iloc[:, 4])
        df[row_names[2]] = abs(df.iloc[:, 2] - df.iloc[:, 5])
        
        # -- Compute summary statistics of the resulting three columns
        stats = df.iloc[:, -3 : ].describe()

        # -- Save the selected summary stats
        selected = ["mean", "min", "25%", "50%", "75%", "max"] 
        for sel in selected:
            if raw.get(sel):
                raw[sel].append([list(stats.loc[sel])])
            else:
                raw[sel] = [list(stats.loc[sel])]

    # - Turn the raw collected data into pd df that can be turn into markdown
    n = len(paths)
    final_data = []
    for i, row_name in enumerate(row_names):
        data = dict()
        for row_stat, values in raw.items():
            data[f"{row_name} {row_stat}"] = [values[j][i] for j in range(n)]
        final_data.append((row_name, data,))

    # - Create the markdowns and return them
    result = ""
    columns = [f"Experiment {i}" for i,_ in paths]
    for name, data in final_data:
        final_result = pd.DataFrame.from_dict(data, orient='index', columns=columns)
        result += (f"👉 **{name}**\n\n" + final_result.to_markdown() + "\n\n\n")
    
    return result

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

    return result + "\n\n<br/>\n\n"

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

def _get_ngens_num(path):
    match = re.search(r'ngens_(\d+)\.png', path)
    if match:
        return int(match.group(1))
    else:
        raise Exception("Incorrect format of snapshot of the archive!")

def _add_archive_timeline(frame_folder):

    # Get pngs paths and 
    paths = sorted(glob.glob(f"{frame_folder}/*.png"), key=_get_ngens_num)

    frames = [Image.open(image) for image in paths]
    duration = 20*int(len(frames)/1)
    if len(frames) > 0:
        frame_one = frames[0]
        path = os.path.join(frame_folder, "timeline.gif")
        frame_one.save(path, format="GIF", append_images=frames, save_all=True, duration=duration, loop=0)
        return path
    else:
        return None
