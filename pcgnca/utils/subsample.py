# --------------------- External libraries imports
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
import os

# --------------------- Public functions
def subsample(settings, n_models, method="basic", k=30):
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
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)

    # Find the closest model in the original DataFrame to each centroid
    closest_model_indices = []
    for centroid in centroids:
        distances = ((df[behavior_cols] - centroid)**2).sum(axis=1)
        closest_model_indices.append(distances.idxmin())

    # Select top n_models/k models closest to each centroid
    df_subsample = pd.DataFrame()
    for i, idx in enumerate(closest_model_indices):
        cluster_members = df[df.index == idx].append(df.iloc[df[behavior_cols].sub(centroids[i]).pow(2).sum(1).nsmallest(n_models//k - 1).index])
        df_subsample = pd.concat([df_subsample, cluster_members])

    # Sort the subsample by "objective" column in descending order
    df_subsample = df_subsample.sort_values("objective", ascending=False)

    # Save the new DataFrame to a CSV file in the same folder
    save_path = os.path.join(folder_path, "trained_archive_subsampled.csv")
    df_subsample.to_csv(save_path, index=False)

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
 