# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:52:11 2023

@author: Derek Joslin

"""

import RomReader as rr
import RomVisualization as rv

class RomLauncher():

    def __init__(self, HapticsEngine, romDictionary):

        # add the haptics engine
        self.HapticsEngine = HapticsEngine

        # create the Rom List
        self.romDictionary = romDictionary

    def launchRom(self, romFilePath):
        self.RomReader = rr.RomReader(romFilePath)
        self.RomReader.romSettings["HapticsEngineAddress"] = id(self.HapticsEngine)
        self.romDictionary[romFilePath] = self.RomReader

    def startRom(self, romString):
        # gets the path of the rom to start
        # launches that rom using the rom reader
        self.launchRom(self.romDictionary[romString])
        print(self.RomReader.romSettings["HapticsEngineAddress"])
        
        if romString == "Slides":
            self.RomVisualization = rv.RomVisualization("RomVisualizer", self.HapticsEngine)
            self.RomVisualization.show()
            self.HapticsEngine.addVisualization(self.RomVisualization)
            #print("Starting the {} ROM".format(romString))
        self.RomReader.stopEvent.set()
        self.RomReader.executeRom()

    def endRom(self):
        # ends the rom and closes everything related to the rom freeing up resources
        print("Ending the ROM")
        self.HapticsEngine.exitEvent = 1