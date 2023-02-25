# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:02:45 2023

@author: Derek Joslin

"""


import PeripheralManager as pm
import TouchscreenPeripheral as tp
import numpy as np
from scipy.signal import butter, filtfilt

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
        
        # filtered data matrix
        self.filteredDataMatrix = np.ones([self.nSensorRows, self.nSensorColumns])
        
        
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
        #print(self.nSensors)
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
         
    """ function that creates a new filtered matrix from raw and current data matrix values """
                
    def processDataValues(self, rawDataMatrix, currentDataMatrix):
        
        
        rawDataMatrix = rawDataMatrix.astype(int)
        currentDataMatrix = currentDataMatrix.astype(int)
        
        # apply low-pass filtering to raw data
        #filteredRawDataMatrix = self.lowPassFilter(rawDataMatrix)
        
        # apply exponential smoothing to filtered raw data
        filteredDataMatrix = self.exponentialSmoothing(currentDataMatrix, rawDataMatrix, 0.1)
        
        filteredDataMatrix = filteredDataMatrix.astype(int)
        
        self.integratedDataMatrix = filteredDataMatrix
        
    
    def exponentialSmoothing(self, currentDataMatrix, filteredRawDataMatrix, alpha):
        filteredDataMatrix = alpha * filteredRawDataMatrix + (1 - alpha) * currentDataMatrix
        return filteredDataMatrix
    
    
    def printTheDataMatrix(self):
        print("TouchOut:")
        rowString = "|"
        for row in self.integratedDataMatrix:
            for element in row:
                rowString += "{} ".format(element)
            print("{}|".format(rowString))
            rowString = "|"
        print("\n")
