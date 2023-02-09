# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:52:11 2023

@author: Derek Joslin

"""

import RomReader as rr
import RomVisualization as rv


class RomLauncher(rr.RomReader):
    
    def __init__(self, filename, HAppControlCenter):
        super().__init__(filename)
           
        
        # add the HApp control center to the class
        self.HAppControlCenter = HAppControlCenter
        
        #add the rom to the python path
        fileFolderList = filename.split("/")

        folderDirectory = ""

        for folder in fileFolderList[:-1]:
            folderDirectory = folderDirectory + folder + "//"
            
        print(folderDirectory)
        self.HAppControlCenter.PathManager.addDirectory(folderDirectory)
        
        
        
        
        # get the ROMs settings and description
        self.interruptDictionary = self.createInterruptDictionary()
        self.romSettings = self.getSettings()
        self.romComments = self.getDescriptions()
        
        # load the address of the Control center into the rom settings
        OperationsControlAddress = id(self.HAppControlCenter)
        self.romSettings['OperationsControlAddress'] = OperationsControlAddress
        

    def startRom(self):
        # passes all necessary values to the rom in order to start it
        self.setSettings(self.romSettings)
        
        self.RomVisualization = rv.RomVisualization("RomVisualizer", self.interruptDictionary)
        
        print("loading visual")
        self.RomVisualization.show()
        
        self.HAppControlCenter.addVisualization(self.RomVisualization)
        
        print("rom settings are {}".format(self.romSettings))
        
        self.executeRom()
        
        #self.RomVisualization = rv.RomVisualization("RomVisualizer", self.interruptDictionary)