import open3d as o3d
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np

# Load point cloud data
pcd = o3d.io.read_point_cloud("river_point_cloud.pcd")


# Remove outliers
pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Convert point cloud to a numpy array
points = np.asarray(pcd.points)

# Cluster the points using DBSCAN
clustering = DBSCAN(eps=0.2, min_samples=10).fit(points)

# Extract cluster labels
cluster_labels = clustering.labels

# Plot point cloud with cluster labels
plt.scatter(points[:, 0], points[:, 1], c=cluster_labels, cmap='viridis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
