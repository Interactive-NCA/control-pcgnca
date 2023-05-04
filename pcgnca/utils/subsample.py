# --------------------- External libraries imports
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import pickle
import os

# --------------------- Public functions
def subsample(settings, n_models, method="basic", k=100):
    """Subsample trained archive along with the training seeds.
    """

    if method == "basic":
        # - Subsample archive ...
        _subsample_archive(settings["save_path"], n_models)
    elif method == "kmeans":
        # - Subsample archive using K-means clustering
        _subsample_archive_k_means(settings["save_path"], n_models, k)

    # - ... and also the corresponing training seeds
    _subsample_training_seeds(settings["save_path"])

# --------------------- Private functions
def _subsample_archive_k_means(folder_path, n_models, k):
    """
    Subsample the archive to the first n_models, using K-means clustering
    to select a diverse set of models based on behavior characteristics.

    Args:
        folder_path (str): Path to the folder containing the archive
        n_models (int): Number of models to subsample
        k (int): Number of clusters to use for K-means clustering
    """
    # Load the archive
    archive_path = os.path.join(folder_path, "trained_archive.csv")
    df = pd.read_csv(archive_path)

    # Select columns for behavior characteristics and standardize them
    behavior_cols = ["measure_0", "measure_1"]
    scaler = StandardScaler()
    X = scaler.fit_transform(df[behavior_cols])

    # Perform K-means clustering on the behavior characteristics
    kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

    # Find the indices of the models in each cluster
    cluster_indices = [np.where(kmeans.labels_ == i)[0] for i in range(k)]

    # Select top n_models//k models with the largest objective value from each cluster
    top_indices = []
    for indices in cluster_indices:
        cluster_models = df.iloc[indices]
        sorted_models = cluster_models.sort_values("objective", ascending=False)
        top_indices.extend(sorted_models.index[:n_models//k])

    # Select the models with the top indices
    df_subsample = df.loc[top_indices]

    # Sort the subsample by "objective" column in descending order
    df_subsample = df_subsample.sort_values("objective", ascending=False)

    # Filter
    df_filter = df_subsample[df_subsample["measure_1"] > 0] # Solution path length > 0

    # Save the new DataFrame to a CSV file in the same folder
    save_path = os.path.join(folder_path, "trained_archive_subsampled.csv")
    df_filter.to_csv(save_path, index=False)


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

    subsampled_seeds = {}
    for k, v in train_seeds.items():
        if k in generations:
            subsampled_v = {}
            subsampled_v['init_states'] = v['init_states'][:10]
            if v['binary_mask'] is not None:
                subsampled_v['binary_mask'] = v['binary_mask'][:10]
                subsampled_v['fixed_states'] = v['fixed_states'][:10]
            subsampled_seeds[k] = subsampled_v

    # Save the new training seeds to a pickle file
    training_seeds_path_subsample = os.path.join(folder_path, "training_seeds_subsampled.pkl")
    with open(training_seeds_path_subsample, "wb") as f:
        pickle.dump(subsampled_seeds, f)
 