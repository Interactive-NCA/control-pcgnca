"""
Module for automatic creation of markdown summaries about
the experiments' results.
"""

import json
import os
import pandas as pd


def get_experiment_settings_summary(stats, expids):

    # - Get the heading
    result = "#### 🔮 About experiment(s)\n\n---\n\n"

    # - Get settings names
    settings_names = list(stats[expids[0]].keys())

    # - Collect the stats to dict which is then turned into pandas df
    data = dict()

    for i, settings_name in enumerate(settings_names):
        row = []
        for expid in expids:
            v = stats[expid][settings_name]
            v = v if v is not None else "0"
            row.append(v)
        data[settings_name] = row

    columns = [f"Experiment {i}" for i in expids] 
    df = pd.DataFrame.from_dict(data, orient='index', columns=columns)

    return result + df.to_markdown() + "\n"

def get_eval_summary(stats):

    sec1 = "#### 📊 General Evaluation Stats\n"
    sec1_expl = "Each model from the training archive is evaluated in two ways. First, on the latent seeds seen during training. Second, on 20 randomly generated seeds.\n"
    expids = [1, 2] if "experiment2" in stats.keys() else [1]
    sec1_data = dict()

    sec1_stats = ["archive size", "% fresh train archive full", "eval QD score", "% elites maintained", "% QD score maintained"]
    sec1_row_names = ["Archive Size", "Perc Of Archive Filled", "QD Score", "Perc Elites Maintained", "Perc QD Score Maintained"]
    for i, stat in enumerate(sec1_stats):
        row = []
        for expid in expids:
            expname = f"experiment{expid}"
            row.extend([stats[expname]["train"][stat], stats[expname]["eval"][stat]])
        row = [item*100 for item in row] if "perc" in sec1_row_names[i].lower() else row
        sec1_data[f"{sec1_row_names[i]}"] = row

    sec1_stats = ["playability", "reliability", "diversity"]
    for i, stat in enumerate(sec1_stats):
        row = []
        for expid in expids:
            row.extend([stats[expname]["train"][stat]["mean"], stats[expname]["eval"][stat]["mean"]])
        sec1_data[f"{stat}-mean"] = row

    columns = ["Exp1 Train", "Exp1 Eval", "Exp2 Train", "Exp2 Eval"] if len(expids) > 1 else ["Exp1 Train", "Exp1 Eval"]
    sec1_df = pd.DataFrame.from_dict(sec1_data, orient='index', columns=columns)
    return sec1 + sec1_expl + sec1_df.to_markdown() + "\n"

def get_training_process_stats(stats):
    sec0 = "#### 🔖 Training Process Stats\n"
    sec0_expl = "Summary about the trained archive. Note that QD score is just a sum of all objective values of models in the archive.\n"
    expids = [1, 2] if "experiment2" in stats.keys() else [1]
    sec0_data = {
        "# of Generations" : [stats[f"experiment{i}"]["generations completed"] for i in expids],
        "Perc of Archive Filled": [100*stats[f"experiment{i}"]["% train archive full"] for i in expids],
        "QD Score": [stats[f"experiment{i}"]["QD score"] for i in expids],
        "Mean objective": [stats[f"experiment{i}"]["objective"]["mean"] for i in expids]
    }

    sec0_df = pd.DataFrame.from_dict(sec0_data, orient='index', columns=[f"Experiment {i}" for i in expids])
    return sec0 + sec0_expl + sec0_df.to_markdown() + "\n"

def get_viz(path):

    # Adjust the path so it is relative to where the summary will be stored
    path = "../.." + path.split("assets")[1]

    names = ["fitness_eval", "diversity", "playability", "reliability"]
    train_names = [f"![]({path}/{name}_fixLvls.png)" for name in names]
    eval_names = [f"![]({path}/{name}.png)" for name in names]
    data = {
        "training" : train_names,
        "eval": eval_names
    }
    df = pd.DataFrame.from_dict(data, orient='index', columns=names)
    return df.to_markdown() + "\n"

def get_experiments_summary(experiment_ids, experiments_path, save_path):

    # - Based on IDs, get paths of experiment to evaluate
    paths = []
    all_experiments = os.listdir(experiments_path)
    for exp_filename in all_experiments:
        for expid in experiment_ids:
            if f"ExperimentId-{expid}" in exp_filename:
                path = os.path.join(experiments_path, exp_filename)
                paths.append((expid, path,))
                break
    
    # - Get experiment settings summary
    # -- Collect the data about settings first
    data = dict()
    for expid, path in paths:

        # --- Load the settings into a dict
        settings_path = os.path.join(path, "settings.json")
        with open(settings_path) as f:
            d = json.load(f)

        # --- Save it to our data dict
        data[expid] = d
    
    settings_summary = get_experiment_settings_summary(data, experiment_ids)

    # - Save the markdown file
    filename = os.path.join(save_path, "summary_of_exps_" + "_".join([str(expid) for expid in experiment_ids]) + ".md")
    with open(filename, "w") as f:
        f.write(settings_summary)