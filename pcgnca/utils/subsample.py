# --------------------- External libraries imports
import pandas as pd
import pickle
import os

# --------------------- Public functions
def subsample(settings, n_models):
    """Subsample trained archive along with the training seeds.
    """

    # - Subsample archive ...
    _subsample_archive(settings["save_path"], n_models)

    # - ... and also the corresponing training seeds
    _subsample_training_seeds(settings["save_path"])

# --------------------- Private functions
def _subsample_archive(folder_path, n_models):
    """
    Subsample the archive to the first n_models

    Args:
        archive_path (str): Path to the archive
        n_models (int): Number of models to subsample
    """

    # - Load the archive
    archive_path = os.path.join(folder_path, "trained_archive.csv")
    df = pd.read_csv(archive_path)

    # - Sort the DataFrame based on "objective" column in descending order
    df_sorted = df.sort_values("objective", ascending=False)

    # - Filter
    df_filter = df_sorted[df_sorted["measure_1"] > 0] # Solution path length > 0

    # - Select the first n_models rows of the sorted DataFrame
    df_top = df_filter.head(n_models).copy()

    # Save the new DataFrame to a CSV file in a folder
    save_path = os.path.join(folder_path, "trained_archive_subsampled.csv")
    df_top.to_csv(save_path, index=False)

def _subsample_training_seeds(folder_path):
    """
    Subsample the training seeds to match the subsampled archive 

    Args:
      archive_path
      training_seeds_path
    """

    # - Load the training seeds
    training_seeds_path = os.path.join(folder_path, "training_seeds.pkl")
    with open(training_seeds_path, "rb") as f:
        train_seeds = pickle.load(f)

    # - Load the subsampled archive
    subsample_archive_path = os.path.join(folder_path, "trained_archive_subsampled.csv")
    df = pd.read_csv(subsample_archive_path)

    # - Subsample the training seeds
    generations = df["metadata"].unique()
    subsampled_seeds = {k: v for k, v in train_seeds.items() if k in generations}

    # Save the new training seeds to a pickle file
    training_seeds_path_subsample = os.path.join(folder_path, "training_seeds_subsampled.pkl")
    with open(training_seeds_path_subsample, "wb") as f:
        pickle.dump(subsampled_seeds, f)
 