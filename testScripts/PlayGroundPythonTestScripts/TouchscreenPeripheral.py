# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:24:40 2023

@author: Derek Joslin

"""

import PeripheralManager as pm
import numpy as np
import serial

class TouchScreenPeripheral(pm.PeripheralDevice):
    
    def __init__(self, name):
        super().__init__(name)
        
        # size of sensor array
        self.nSensorRows = 5
        self.nSensorColumns = 7 
        
        # intialize touchscreen data matrix to a default size
        self.sensorDataMatrix = np.ones([self.nSensorRows, self.nSensorColumns])    
        
        # get the list of touch points
        self.touchPointList = []

        # command to get touch values
        self.deltaCommand = bytearray([1, 2, 3, 0, 2, 4, 35, 0, 3, 2, 1])

        # touch screen buffer
        self.comportBuffer = []
        
        
    def connect(self, comString):
        # Connect to the specified comport
        baudrate = 115200  # Set the baud rate to use for the serial connection
        timeout = 1  # Set the timeout for reading from the serial connection

        # assign the serial port of the touchscreen
        self.serialPort = serial.Serial(comString, baudrate, timeout=timeout)
    
    def writeDeltaCommand(self):
        # write the command for the delta values to the port
        self.serialPort.write(self.deltaCommand)
    
    def getDeltaValues(self):
        
        sensorValues = []
        if self.serialPort.in_waiting > 44: #44 before  # Check if there are bytes in the input buffer
            # read all bytes
            while self.serialPort.in_waiting > 0:
                # keep reading until no bytes
                try:
                        
                    byte = self.serialPort.read(45) #45  # Read a single byte from the serial port
                    print(byte)
                    self.comportBuffer = list(bytearray(byte))  # Add the byte to the list
                except Exception as e:
                    print(e)
            
            # put bytes from comportBuffer into the data matrix
            self.processTheRecieveByte()
            
    def processTheRecieveByte(self):
        # check that the delta values are available on the comport buffer
        if len(self.comportBuffer) == 45: #45 before
            # throw out the extreneous bytes
            self.comportBuffer[0:7] = [] # 7 before
            self.comportBuffer[-3:-1] = [] # 3 before
            self.comportBuffer.pop()
            iRow = self.nSensorRows - 1
            iColumn = self.nSensorColumns - 1
            for byte in self.comportBuffer:
                # assign each byte of delta value to its proper place in the data matrix
                self.sensorDataMatrix[iRow][iColumn] = byte
                iRow -= 1
                if iRow == -1:
                    iRow = self.nSensorRows - 1
                    iColumn -= 1
            
            # clear the comport buffer to recieve the next command
            self.comportBuffer.clear()
            #print(self.sensorDataMatrix)
    def printDeltaValues(self):
        print(self.name)
        print(self.sensorDataMatrix)

# =============================================================================
# Touchscreen = TouchScreenPeripheral("test touch")
# 
# Touchscreen.connect("COM7")
# 
# Touchscreen.writeDeltaCommand()
# 
# Touchscreen.getDeltaValues()
# 
# Touchscreen.printDeltaValues()
# 
# =============================================================================
