# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:13:11 2022

@author: Derek Joslin
"""

from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

import NewKeyboardHandles as nkh
import NewRomVisualizationHandles as nrv
import BasicRomVisualizationHandles as brh

#import TextEditor as te

import RomReader as rr
import RomVisualization as rv

import time

""" another class responsible for controlling and starting the rom """

class RomRunner():
    
    def __init__(self, HAppControlCenter):
        
        #An instance of the haptics engine will already exist
        self.HAppControlCenter = HAppControlCenter
        self.NewKeyboardHandles = nkh.NewKeyboardHandles()
        
        #self.Editor = te.TextEditor()
        
        
    def getRomData(self, filename):
        self.ThisRom = rr.RomReader(filename)
        
        self.interruptDictionary = self.ThisRom.createInterruptDictionary()
        self.romSettings = self.ThisRom.getSettings()
        self.romComments = self.ThisRom.getDescriptions()
        
        #need to ask rom how it wants to be displayed
        #TBD
        
        
    def passValuesToRom(self):
        OperationsControlAddress = id(self.HAppControlCenter)
        self.romSettings['OperationsControlAddress'] = OperationsControlAddress
        self.ThisRom.setSettings(self.romSettings)
        
        
    def startRom(self):
        
        #create the visualization for the rom and pass in the required values
        #self.TextEditor = BrailleEdit(self.BrailleDisplay)
        KeyboardPeripheral = self.HAppControlCenter.getPeripheral("Master Keyboard")
        KeyboardPeripheral.setNewKeyboardHandler(self.NewKeyboardHandles)
        
        self.ThisRom.setSettings(self.romSettings)
        
        self.ThisRom.executeRom()
        
        self.RomVisualization = rv.RomVisualization("RomVisualizer", self.interruptDictionary)
        
        print("loading visual")
        self.RomVisualization.show()
        
        self.HAppControlCenter.addVisualization(self.RomVisualization)
        
        #self.NewRomVisualizationHandles = brh.BasicRomVisualizationHandles(self.interruptDictionary, self.RomVisualization.RomExplorer)
        #self.HAppControlCenter.setVisualizationHandler("RomVisualization", self.NewRomVisualizationHandles)
        #self.ViewUpdater = RomViewUpdater(self)
        
        #self.TextEditor.show()
        #self.RomVisualization.controlDialog.show()


#create a note pad for running functions takes in text as a pyqt script
class BrailleEdit(qw.QTextEdit):
    
    def __init__(self):
        super().__init__()
        #fixedWidth = qt.QReal
        
        #self.setLineWrapColumnOrWidth(20)
        #self.setFixedWidth(20)
        courierFont = qg.QFont("Courier")
        courierFont.setPointSize(800)
        self.setFont(courierFont)
        self.show()
        
        #self.setPageSize(qc.QSize(200, 200))
        #self.engine = engine
        
    