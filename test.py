import csv
import numpy as np
import open3d as o3d

distances = []

with open("TestData.csv", "r") as test_data:
    reader = csv.reader(test_data)
    for line in reader:
        row = line[0]
        if " cm" in row:
            row = row.replace(" cm", '')
        distances.append(row)

for distance in distances:
    distance = float(distance)

x_axis[len(distances)]

print(distances)
for i in range(len(distances)):
    x_axis[i] = distances[i]

for i in range(len(distances)):
    y_axis[i] = distances[i]

for i in range(len(distances)):
    z_axis[i] = distances[i]

point_data = np.stack([x_axis, y_axis, z_axis], axis=0).transpose((1, 0))

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
