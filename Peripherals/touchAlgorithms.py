# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:14:56 2023

@author: Derek Joslin

"""

from filterpy.kalman import KalmanFilter
import numpy as np
from scipy import ndimage


def centerOfMass(dataMatrix):
    
        # get the center of mass of the integratedDataMatrix

        def lessThan(x):
            if x < 5:
                return 0
            else:
                return x
        
        # clean up input data by removing values less than 5
        dataMatrix = np.vectorize(lessThan)(dataMatrix)
        
        # create label for finding the center of mass
        lbl = ndimage.label(dataMatrix)[0]
        
        # create a dummy set of rawTouch points
        rawTouchPointList= [(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)]
        
        # find 10 centers of mass
        for iCenterOfMass in range(0,10):
            rawTouchPointList[iCenterOfMass] = (ndimage.center_of_mass(dataMatrix, lbl, iCenterOfMass))
            
            
        # remove NaNs from list
        for iPoint,point in enumerate(rawTouchPointList):
            if np.isnan(point[0]):
                # get the current position 
                rawTouchPointList[iPoint] = (-1, -1)
        
        # return the rawTouch point list
        return rawTouchPointList
    
    
# =============================================================================
#     
# def kalmanFilter(dataMatrix):
#     # use the kalman filter class to filter the delta values?
#     kFilter = KFilter()
#     
#     
#     
#     
#     
#     
#     
#     
#     
#     pass
# =============================================================================
    
    
    
    
# =============================================================================
# class KFilter:
#     
#     def __init__(self):
#         # Define the Kalman filter
#         self.kf = KalmanFilter(dim_x=2, dim_z=2)
#         
#         # Set the initial state estimate and error covariance estimate
#         self.kf.x = np.array([0., 0.])
#         self.kf.P = np.array([[1., 0.], [0., 1.]])
#         
#         # Set the measurement noise covariance matrix R
#         self.kf.R = np.eye(2)
#         
#         # Set the process noise covariance matrix Q
#         self.kf.Q = np.array([[0.01, 0.], [0., 0.01]])
#         
#         # Set the state transition matrix A
#         self.kf.F = np.array([[1., 0.], [0., 1.]])
#         
#         # Set the observation matrix C
#         self.kf.H = np.array([[1., 0.], [0., 1.]])
#         
#     def doFilter(self, dataMatrix):
#         try:
#             touchPointLocations = []
#             
#             # Predict step
#             self.kf.predict()
#             
#             # Update step
#             self.kf.update(dataMatrix)
#             
#             touchPointLocations.append((kf.x[0], kf.x[1]))
#             
#             return touchPointLocations
#         
#         except Exception as e:
#             
#             print(e)
# =============================================================================
