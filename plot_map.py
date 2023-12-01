"""
This code is still for version 1 of delphin 
in which the left and right sensors are 
stationary as well, not on any motor.
"""

# Importing libraries
import csv
import numpy as np
import open3d as o3d
import math

# River file name
river_file_name = "test_data.csv"

# Variables as per the distance of the Delphin from water surface
Delphin_depth = 0
Delphin_dist_from_left_edge = 0 # Currently 0, else we need a formula, yet to be formulated
Delphin_dist_from_right_edge = 0 # Currently 0, else we need a formula, yet to be formulated
Delphin_speed = 1 # This is the speed to be maintained whatever the river current might be

# Mapping Sensor ID
front_mapping_sensor = 0
left_mapping_sensor = 1
right_mapping_sensor = 2

# Mapping Sensor Variables
readings_taken_per_sec = 10 # RTPS

'''
This function takes file name or path and the Sensor ID
as an input and returns a numpy stack for plotting data
from the sensor specified.

It also takes a parameter "rtps" which means the readings
taken per second by the specified sensor.

This function returns the stack as per the sensor informed
while using it, as some sensors might need to add some values
such as depth of Delphin and distance from edge.
'''
def mapping_sensor(file_name, mapping_sensor_id, rtps=10):
    
    radians = []
    
    with open(file_name, "r") as data:
        distances = []
        counter = 0
        
        # Turn 0 -> Going from bottom to top
        # Turn 1 -> Going from top to bottom
        turn = 0
        reader = csv.reader(data)
        
        # Removing redundances from the input csv file
        for line in reader:
            row = line[mapping_sensor_id]
            # print(row)
            if " cm" in row:
                row = row.replace(" cm", '')
            if "Distance: " in row:
                row = row.replace("Distance: ", '')
            if "ï»¿" in row:
                row = row.replace("ï»¿", '')
            if row == '':
                continue
            distances.append(row)
            radians.append(counter * (math.pi / 180))
            try:
                if turn == 0:
                    if 90 / counter == 1:
                        turn = 1
                        counter -= rtps
                    else:
                        counter += rtps
                else:
                    if 90 / counter != 1: 
                        counter -= rtps
            except ZeroDivisionError:
                turn = 0
                counter += rtps
    
    # Conversion from string into float
    distances = [float(x) for x in distances]
    distances = np.array(distances)
    
    if mapping_sensor_id == 0 or mapping_sensor_id == 2:
        
        # Convert distances and radians into numpy array to perform multiplication
        angles = [math.cos(radian) for radian in radians]
        angles = np.array(angles)
        
        x_axis = np.multiply(distances, angles)
        x_axis = x_axis.tolist()
    elif mapping_sensor_id == 1:
        angles = [0 - math.cos(radian) for radian in radians]
        angles = np.array(angles)
        
        x_axis = np.multiply(distances, angles)
        x_axis = x_axis.tolist()
    
    # Add depth of delphin to get accurate readings
    angles = [math.sin(-radian) for radian in radians]
    angles = np.array(angles)
    
    y_axis = np.multiply(distances, angles)
    y_axis = y_axis.tolist()
    
    y_axis = [Delphin_depth + x for x in y_axis]
    distances = distances.tolist()
    
    z_axis = []
    for i in range(len(distances)):
        coordinate = int(Delphin_speed * ((i + 1) / rtps))
        z_axis.append(coordinate)
    
    point_data = np.stack([x_axis, y_axis, z_axis], axis=0).transpose((1, 0))
    return point_data

test0 = mapping_sensor(river_file_name, mapping_sensor_id=0, rtps=readings_taken_per_sec)
test1 = mapping_sensor(river_file_name, mapping_sensor_id=1, rtps=readings_taken_per_sec)
test2 = mapping_sensor(river_file_name, mapping_sensor_id=2, rtps=readings_taken_per_sec)

print("Printing the data from front-sensor")
print(test0)

print("Printing the data from left-sensor")
print(test1)

print("Printing the data from right-sensor")
print(test2)

# Plotting
geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(mapping_sensor(river_file_name, front_mapping_sensor, readings_taken_per_sec))
geom.points = o3d.utility.Vector3dVector(mapping_sensor(river_file_name, left_mapping_sensor, readings_taken_per_sec))
geom.points = o3d.utility.Vector3dVector(mapping_sensor(river_file_name, right_mapping_sensor, readings_taken_per_sec))
o3d.visualization.draw_geometries([geom])
