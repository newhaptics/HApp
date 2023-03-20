# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 13:09:37 2023

@author: Derek Joslin

"""

from PyQt5.QtWidgets import QLabel
import serial.tools.list_ports
import PeripheralDevice as pd

# need to import the files for all the potential peripherals
import NHAPI as nh

class PeripheralManager:
    def __init__(self):
        self.peripheralDictionary = {}
        # create a list of available peripherals
        self.availablePeripherals = [ "NewHaptics Display", "NewHaptics Touchscreen" ]
        self.currentPeripheral = ""
        
    def addPeripheral(self, Peripheral):
        self.peripheralDictionary[Peripheral.name] = Peripheral
        
    def removePeripheral(self, peripheralName):
        del self.peripheralDictionary[peripheralName]
        
    def getDevice(self, peripheralName):
        return self.peripheralDictionary.get(peripheralName)
        
    def getAllDevices(self):
        return self.peripheralDictionary.values()
                
    def disconnectDevice(self, peripheralName):
        self.peripheralDictionary[peripheralName].disconnect()
    
    def connectAll(self):
        for peripheral in self.peripheralDictionary.values():
            peripheral.connect()
            
    def disconnectAll(self):
        for peripheral in self.peripheralDictionary.values():
            peripheral.disconnect()
            
    def getStatusAll(self):
        statuses = {}
        for peripheral in self.peripheralDictionary.values():
            statuses[peripheral.name] = peripheral.getStatus()
        return statuses
    
    def printAllPeripherals(self):
        peripheralDebugText = "ARCS Peripherals-\n"
        for Peripheral in self.peripheralDictionary.values():
            peripheralDebugText += "{}\n".format(Peripheral.name)
            peripheralDebugText += "{}\n".format(Peripheral.debugString)

        return peripheralDebugText
    
    def getPeripheralLabels(self):
        # Create a list of labels for the peripherals
        peripheralLabelList = []

        for Peripheral in self.peripheralDictionary.values():
            # For each peripheral make a label
            Label = QLabel(Peripheral.name)
            
            # Set the tooltip for this label to be the debug text of the peripheral
            Label.setToolTip(Peripheral.debugString)
            
            # Add the peripheral label to the list
            peripheralLabelList.append(Label)

        return peripheralLabelList
    
    # New additions for llmOS
    
    # List all the comports for the device
    def getAvailbleComports(self):
        connections = list(serial.tools.list_ports.comports())
        comportList = []
        for comport in connections:
            comportList.append(comport.device)
            
        return comportList
    
    def connectPeripheral(self, peripheralType, peripheralName, comPort):
            
            try:
                
                if peripheralType == "Display":

                    self.TactileDisplay = nh.NHAPI(peripheralName)

                    self.TactileDisplay.connect(comPort)

                    self.addPeripheral(self.TactileDisplay)

                elif peripheralType == "Touchscreen":
                    print("wow such touchscreen")

                else:
                    print("error no device named {}".format(peripheralName))
                    
            except Exception as e:
                print("unable to connect device {0} at comport {1}.".format(peripheralType, comPort))
                print(e)
                
    def disconnectPeripheral(self, peripheralName):
            
            try:
                self.disconnectDevice(peripheralName)
                self.removePeripheral(peripheralName)
                    
            except Exception as e:
                print("unable to disconnect device {0}.".format(peripheralName))
                print(e)