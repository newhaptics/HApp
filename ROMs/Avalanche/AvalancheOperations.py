# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:50:55 2023

@author: Derek Joslin

"""

import RomAPI as rs
import time

class TactileDisplayRefreshOperation(rs.RomOperation):
    
    def __init__(self, name, TactileDisplay, TextEditor):
        super().__init__(name)
        
        # inputs to the operation
        self.TextEditor = TextEditor
        self.inputDictionary["Text Editor"] = self.TextEditor
        
        # outputs to the operation
        self.TactileDisplay = TactileDisplay
        self.outputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        # provide a description
        self.description = "This operation refreshs the display when keys are typed. It's execution is interupt based."
        
        self.executable = self.execute
        
        self.createDebugString()
        
    def execute(self):
        self.TactileDisplay.braille((0,0),self.TextEditor.editorMatrixOutput())
        
        self.TactileDisplay.refresh()
        
class positionFlag(rs.RomFlag):
    
    def __init__(self, name):
        super().__init__(name)
        self.debugString = "This flag indicates where the pong and cursor is."
        self.pongPosition = [0,0]
        self.pong2Position = [0,0]
        self.startPosition = [0,0]
        
        """ initializing controls """
        self.cursorPosition = [1,1]
        self.startPosition[0] = self.cursorPosition[0]
        self.startPosition[1] = self.cursorPosition[1]
        
    def setCursorPosition(self, state):
        self.cursorPosition = state
        
    def setPongPosition(self, state):
        self.pongPosition = state