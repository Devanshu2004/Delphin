import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
#raw algorithm
z_scores = np.abs(stats.zscore(point_cloud_data))
threshold = 3
outliers = np.where(z_scores > threshold)
plt.figure(figsize=(10, 6))
plt.scatter(point_cloud_data[:, 0], point_cloud_data[:, 1], c='b', label='Inliers', s=10)
plt.scatter(point_cloud_data[outliers, 0], point_cloud_data[outliers, 1], c='r', label='Outliers', s=30)
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Point Cloud Outliers')
plt.show()
Q1 = np.percentile(point_cloud_data, 25, axis=0)
Q3 = np.percentile(point_cloud_data, 75, axis=0)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = np.where((point_cloud_data < lower_bound) | (point_cloud_data > upper_bound))
