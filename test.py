import csv
import numpy as np
import open3d as o3d
import math

# List of distances from the sensor
distances = []
distances1 = []
distances2 = []
distances3 = []



with open("TESTDEMO4.csv", "r") as test_data:
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
# Conversion from string into float
distances = [float(x) for x in distances]
print(type(distances[2]))
x_axis = [math.cos(x) for x in distances]
y_axis = [math.sin(-x) for x in distances]
z_axis = [i for i in range(len(distances))]
print(distances)
point_data = np.stack([x_axis, y_axis, z_axis], axis=0).transpose((1, 0))









with open("TESTDEMO3.csv", "r") as test_data:
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
        distances1.append(row)
print(type(distances1[2]))
# Conversion from string into float
distances1 = [float(x) for x in distances1]
print(type(distances1[2]))
x_axis1 = [math.cos(x) for x in distances1]
y_axis1 = [math.sin(-x) for x in distances1]
z_axis1 = [i for i in range(len(distances1))]
print(distances)
point_data1 = np.stack([x_axis1, y_axis1, z_axis1], axis=0).transpose((1, 0))




with open("TESTDEMO2.csv", "r") as test_data:
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
        distances2.append(row)
print(type(distances2[2]))
# Conversion from string into float
distances2 = [float(x) for x in distances2]
print(type(distances2[2]))
x_axis2 = [math.cos(x) for x in distances2]
y_axis2 = [math.sin(-x) for x in distances2]
z_axis2 = [i for i in range(len(distances2))]
print(distances2)
point_data2 = np.stack([x_axis2, y_axis2, z_axis2], axis=0).transpose((1, 0))




# Plotting
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
geom.points = o3d.utility.Vector3dVector(point_data1)
geom.points = o3d.utility.Vector3dVector(point_data2)
o3d.visualization.draw_geometries([geom])
