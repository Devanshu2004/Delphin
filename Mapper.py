from pyntcloud import PyntCloud
import numpy as np

# raw algorithm
# Load point cloud data from a PCD file
cloud = PyntCloud.from_file("path/to/your/point_cloud.pcd")

# Extract depth values (Z-coordinate) from the point cloud
depth_values = cloud.points["z"]

# Extract width values (X-coordinate) from the point cloud
width_values = cloud.points["x"]

# Perform further processing on depth and width values
average_depth = np.mean(depth_values)  # Calculate average depth
min_depth = np.min(depth_values)       # Find minimum depth
max_depth = np.max(depth_values)       # Find maximum depth

average_width = np.mean(width_values)  # Calculate average width
min_width = np.min(width_values)       # Find minimum width
max_width = np.max(width_values)       # Find maximum width

# Print or use the computed depth and width values
print("Depth Information:")
print("Average Depth:", average_depth)
print("Minimum Depth:", min_depth)
print("Maximum Depth:", max_depth)

print("\nWidth Information:")
print("Average Width:", average_width)
print("Minimum Width:", min_width)
print("Maximum Width:", max_width)
