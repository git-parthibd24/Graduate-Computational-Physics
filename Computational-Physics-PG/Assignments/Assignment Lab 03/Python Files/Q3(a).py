#Question 3(a)
#Calculate the velocity and acceleration of the object using finite difference approximation of coordinates and time using the gps data from the csv file

import numpy as np
import pandas as pd

#Reading the data from the csv file (Use raw string to specify path and avoid backslash error, otherwise python interprets it as escape character)
datafile_1000=pd.read_csv(r'S:\Documents\Github\Computational-Physics-PG\Assignment Lab 03/Python Files/gps_data.csv',header=0,usecols=["Coordinate (m)","Time (s)"])
coordinate_array=datafile_1000["Coordinate (m)"].to_numpy()
time_array=datafile_1000["Time (s)"].to_numpy()
#We can also load a txt data file using np.loadtxt(data_file.txt,skiprows=0) function which creates a multidimensional array consisting of different column data of the file as columns in the array


#Calculating the velocity and acceleration using finite difference approximation
def kinematics(i,x,t):
    v=(x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    a=(2/((t[i+1]-t[i-1])))*((x[i+1]-x[i])/(t[i+1]-t[i])-(x[i]-x[i-1])/(t[i]-t[i-1]))
    return v,a

for i in range(1,len(coordinate_array)-1):         #we have to exclude last 2 elements. Last one is already excluded as i goes upto len(coordinate_array)-1 by default. 2nd last one is manually excluded by subtracting 1
    v,a=kinematics(i,coordinate_array,time_array)
    print("Velocity between time t =",time_array[i-1],'s and time',time_array[i+1],"s is",np.round(v,3),'m/s')
    print("Acceleration between time t =",time_array[i],'s and time',time_array[i+1],"s is",np.round(a,3),'m/s^2')
    print()
