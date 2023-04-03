# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:02:45 2023

@author: Derek Joslin

"""


import PeripheralDevice as pm
import TouchscreenPeripheral as tp
import numpy as np
import touchAlgorithms as ta
from scipy.interpolate import griddata
import sys

class IntegratedTouchscreenPeripheral(pm.PeripheralDevice):

    def __init__(self, name):
        # import the various touchscreens which will compose the integrated unit
        super().__init__(name)
        
        # store touchsreen sensor size
        self.nSensorRows = 0
        self.nSensorColumns = 0
        self.nSensors = 0
        
        # list to store the various touch screens
        self.TouchscreenList = []
        
        # create the integrated data matrix
        self.integratedDataMatrix = np.ones([self.nSensorRows, self.nSensorColumns])
        
        # delta value list
        self.deltaValueList = []
        
        # touch algorithm selected
        self.touchAlgorithm = ""
        
        # interpolated matrix
        self.interpolatedDataMatrix = []
        
        # filter settings

    def connectNewTouchscreen(self, comport):
        # create a new touch screen and add it to the list
        Touchscreen = tp.TouchScreenPeripheral(comport)
        Touchscreen.connect(comport)
        
        # add it to the touch screen list
        self.TouchscreenList.append(Touchscreen)
        
        # recalculate the integrated touch size
        self.nSensorRows = 0
        self.nSensorColumns = 0
        for Touchscreen in self.TouchscreenList:
            self.nSensorRows = Touchscreen.nSensorRows
            self.nSensorColumns += Touchscreen.nSensorColumns

        self.nSensors = self.nSensorRows * self.nSensorColumns

        # resize the integrated Data matrix
        self.integratedDataMatrix = np.ones([self.nSensorRows, self.nSensorColumns])

    def writeDeltaCommand(self):
        # write the delta command for each touchscreen
        for Touchscreen in self.TouchscreenList:
            Touchscreen.writeDeltaCommand()

    def getDeltaValues(self):

        rawDataMatrix = 0

        # loop through each touch and collect their Deltas
        for i,Touchscreen in enumerate(self.TouchscreenList):
            Touchscreen.getDeltaValues()
            
            # add data to the integrated touchscreen data matrix
            if i > 0:
                rawDataMatrix = np.hstack((rawDataMatrix, Touchscreen.sensorDataMatrix))
            else:
                rawDataMatrix = Touchscreen.sensorDataMatrix

        # process the recieved delta values
        self.processDataValues(rawDataMatrix, self.integratedDataMatrix)

        self.deltaValueList.append(self.integratedDataMatrix)

        if len(self.deltaValueList) > 100:
            self.deltaValueList.pop(0)

    """ function that creates a new filtered matrix from raw and current data matrix values """

    def processDataValues(self, rawDataMatrix, currentDataMatrix):

        #rawDataMatrix = rawDataMatrix.astype(int)
        #currentDataMatrix = currentDataMatrix.astype(int)
        
        # apply low-pass filtering to raw data
        #filteredRawDataMatrix = self.lowPassFilter(rawDataMatrix)
        
        # apply exponential smoothing to filtered raw data
        #filteredDataMatrix = rawDataMatrix
        filteredDataMatrix = self.exponentialSmoothing(currentDataMatrix, rawDataMatrix, 0.1)
        
        #filteredDataMatrix = rawDataMatrix
        
        #print(self.interpolatedDataMatrix)
        
        filteredDataMatrix[filteredDataMatrix > 30] = 0
        
        #sys.exit()
        self.integratedDataMatrix = filteredDataMatrix

    def getInterpolation(self, resolution):
        # generate the interpolation matrix for the data
        
        # Define x and y values for interpolation
        newX = np.linspace(0, self.integratedDataMatrix.shape[1] - 1, resolution[0])
        newY = np.linspace(0, self.integratedDataMatrix.shape[0] - 1, resolution[1])
        
        self.interpolatedDataMatrix = self.interpolate(self.integratedDataMatrix, newX, newY)

    def interpolate(self, arr, x, y):
        # Generate a meshgrid of x and y values
        x_mesh, y_mesh = np.meshgrid(x, y)
    
        # Generate a meshgrid of indices for the input array
        ix_mesh, iy_mesh = np.meshgrid(np.arange(arr.shape[1]), 
                                       np.arange(arr.shape[0]))
    
        # Stack the flattened array and its indices
        points = np.vstack((arr.ravel(), ix_mesh.ravel(), iy_mesh.ravel())).T
    
        # Interpolate the flattened array using griddata
        interp_arr = griddata(points[:, 1:], points[:, 0], 
                              (x_mesh, y_mesh), method='cubic')

        return interp_arr
    
    def exponentialSmoothing(self, currentDataMatrix, rawDataMatrix, alpha):
        filteredDataMatrix = alpha * rawDataMatrix + (1 - alpha) * currentDataMatrix
        return filteredDataMatrix

    def findTouchPoints(self):
        # using either the delta values determine the touch points
        
        if self.touchAlgorithm == "center of mass":
            return ta.centerOfMass(self.integratedDataMatrix)
        
        elif self.touchAlgorithm == "kalman filter":
            return 1
        else:
            return 0

    def printTheDataMatrix(self):
        print("TouchOut:")
        rowString = "|"
        for row in self.integratedDataMatrix:
            for element in row:
                rowString += "{} ".format(element)
            print("{}|".format(rowString))
            rowString = "|"
        print("\n")
