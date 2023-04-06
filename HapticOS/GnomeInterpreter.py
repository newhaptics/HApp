# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:00:14 2023

@author: Derek Joslin

"""


class GnomeInterpreter():
    
    def __init__(self, gnomeFilePath):
        # read in the gnome file
        gnomes = open(gnomeFilePath)
        gnomeString = gnomes.read()
        
        # split into multiple gnomes
        gnomeList = gnomeString.split("\n\n:gnome:")
        gnomeList = gnomeList[1:]

        # create the gnome dictionary
        self.gnomeDictionary = {}
        workingGnome = []
        for gnome in gnomeList:
            workingGnome = gnome.split("\n:ASSISTANT:\n")
            firstResponse = workingGnome[1]
            workingGnome = workingGnome[0].split("\n:USER:\n")
            firstQuery = workingGnome[1]
            workingGnome = workingGnome[0].split('\n', 1)
            gnomeKey = workingGnome[0]
            gnomeContent = workingGnome[1]
            gnomeMember = (gnomeContent, firstQuery, firstResponse)
            
            self.gnomeDictionary[gnomeKey] = gnomeMember

    def getGnome(self, gnomeKey):
        return self.gnomeDictionary[gnomeKey]
    
    def __getitem__(self, gnomeKey):
        return self.getGnome(gnomeKey)
        
    def getGnomeKeys(self):
        return list(self.gnomeDictionary.keys())
    
    def addGnome(self, gnomeMember):
        self.gnomeDictionary[gnomeMember[0]] = gnomeMember[1]
        
    def __setitem__(self, gnomeKey, gnome):
        self.gnomeDictionary[gnomeKey] = gnome
        
        
#LLMGnome = GnomeInterpreter("C://Users//derek//Documents//HApp//HAppKernal//gnomes//LLMOS.gnome")
        
# Dialectic
# seizure
# intention
# understanding
# extension