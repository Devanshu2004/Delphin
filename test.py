import csv
import numpy as np
import open3d as o3d

# List of distances from the sensor
distances = []

with open("DelphinTEST1.csv", "r") as test_data:
    reader = csv.reader(test_data)

    # Removing redundances from the input csv file
    for line in reader:
        row = line[0]
        print(row)
        if " cm" in row: 
            row = row.replace(" cm", '')
        if "Distance: " in row:
            row = row.replace("Distance: ", '')
        if "ï»¿" in row:
            row = row.replace("ï»¿", '')
        distances.append(row)

print(type(distances[2]))

# Conversion from string into float
distances = [float(x) for x in distances]

print(type(distances[2]))

x_axis = distances
y_axis = [x + 24.32 for x in distances]
z_axis = [x - 90.84 for x in distances]

print(distances)

point_data = np.stack([x_axis, y_axis, z_axis], axis=0).transpose((1, 0))

# Plotting
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
