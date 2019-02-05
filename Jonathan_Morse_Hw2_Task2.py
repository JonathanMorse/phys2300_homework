import numpy as np
import math as m
import matplotlib.pyplot as plt

# Function to calculate projectile motion
def position_x(position,velocity,time,accel):
       """
       Calculates the position of x and y values
       """
       return position + velocity*time + 0.5*accel*time**2

# Function to plot data
def plot_data(x_initial_position, velocity_x_initial, y_initial, velocity_y_Initial):
       """
       plots the data on the graph
       """
       #constants     
       accel_x = 0.0
       accel_y = -9.8
       time = 0;
       delt = 0.1
       x = []
       y = []

       intervals = 170

       for i in range(intervals):
              x.append(position_x(x_initial_position,velocity_x_initial,time,accel_x))
              y.append(position_x(y_initial,velocity_y_Initial,time,accel_y))
              time = time + delt

       #if y[i + 1] > 0.0:
       # break
       plt.xlabel("x")
       plt.ylabel("y")
       plt.plot(x, y)
       plt.show()

# "Main" Function
def main():
       """
       Gets input from user then
       passes it to get plotted
       """   
       #User input
       x_initial_position = float(input("Enter initial x positon "))
       velocity_x_initial = float(input("Enter initial velocity in x direction "))
       y_initial = float(input("Enter initial y position "))
       velocity_y_Initial = float(input("Enter initial velocity in y direction "))  

       plot_data(x_initial_position, velocity_x_initial, y_initial, velocity_y_Initial)    

main()