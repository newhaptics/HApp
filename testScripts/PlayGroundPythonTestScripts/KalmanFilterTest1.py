# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:33:11 2023

@author: Derek Joslin
"""

from filterpy.kalman import KalmanFilter
import numpy as np
import random

def getSensorData():
    return random.randint(1,50)

# Initialize the Kalman filter
kf = KalmanFilter(dim_x=2, dim_z=1)

# Set the initial state estimate to 25 (the midpoint of the sensor range) and a rate of change of 0
kf.x = np.array([[25.], [0.]])

# Set the initial state covariance to 100 (a high uncertainty)
kf.P = np.array([100])

# Set the process noise covariance to 1 (a small random walk)
kf.Q = np.array([1])

# Set the measurement noise covariance to 25 (assuming a noise of 5)
kf.R = np.array([25])

# sensor data list
zList = []

# Loop through some sensor data and update the filter at each time step
for i in range(100):
    # Get a new sensor measurement
    z = np.array([[getSensorData()]])#, getSensorData()], [getSensorData(), getSensorData()]])
    print(z)
    print(z.shape)
    zList.append(z)
    
    # Predict the next state and covariance
    kf.predict()
    
    # Update the state and covariance based on the new measurement
    kf.update(z)
    
    # Print the current estimate of the true value
    print(kf.x[0])