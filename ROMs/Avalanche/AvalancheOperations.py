# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:50:55 2023

@author: Derek Joslin

"""

import RomAPI as rs
import time

class AvalancheGraphicsRender(rs.RomOperation):
    
    def __init__(self, name, TactileDisplay, AvalancheModel):
        super().__init__(name)
        
        # inputs to the operation
        self.GameFlag = AvalancheModel.GameFlag
        self.inputDictionary["Game Flag"] = self.GameFlag
        
        self.AvalancheModel = AvalancheModel
        self.inputDictionary["AvalancheModel"] = self.AvalancheModel
        
        # outputs to the operation
        self.TactileDisplay = TactileDisplay
        self.outputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        executionParameters = {
            "executeOnFlags": [self.GameFlag], # a set of flag dependencies that when met start executing the Operation
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
        }
        
        # provide a description
        self.description = "This operation refreshs the display when physics are updated. It's execution is interuppt based."
        
        self.executable = self.execute
        
        self.createDebugString()
        
    def checkFlagConditions(self):
        # grab the state of ToolFlag
        updateState = self.GameFlag.state
        print(updateState)
        
        # get the current state of the tactile display
        #currentState = self.TactileDisplay.return_currentState()
        if updateState:
            # compare the flag matrix to the current state of the Tactile Display
            print("need to update the display")
            self.GameFlag.setState(0)
            return True
        else:
            # if they are not the same then return false
            return False
        
    def stopOperation(self):
        # delete the timer for the operation by running the super class function
        super().stopOperation()
        
        # mark isStopped as false so the function is not killed
        self.isStopped = False
        
    def execute(self):
        
        self.TactileDisplay.clear()
        # render the avalanche object
        self.TactileDisplay.line((self.GameFlag.pongPosition[1] - 2,self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1] - 2,self.GameFlag.pongPosition[0] + 2))
        self.TactileDisplay.line((self.GameFlag.pongPosition[1] - 1,self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1] - 1,self.GameFlag.pongPosition[0] + 2))
        self.TactileDisplay.line((self.GameFlag.pongPosition[1],self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1],self.GameFlag.pongPosition[0] + 2))
        
        # render the cursor as a line
        self.TactileDisplay.line((self.GameFlag.cursorPosition[1], self.GameFlag.cursorPosition[0] - 2), (self.GameFlag.cursorPosition[1], self.GameFlag.cursorPosition[0] + 6))
        self.TactileDisplay.line((self.GameFlag.cursorPosition[1] + 1,self.GameFlag.cursorPosition[0] - 2), (self.GameFlag.cursorPosition[1] + 1,self.GameFlag.cursorPosition[0] + 6))

        
        self.AvalancheModel.peripheralCommunication()
        
        
class GameStateFlag(rs.RomFlag):
    
    def __init__(self, name, difficultySetting):
        super().__init__(name)
        self.debugString = "This flag indicates where the pong and cursor is."
        
        """ initializing game settings """
        self.difficulty = difficultySetting
        
        """ establishing game mechanics """
        self.xIncrement = 0
        self.yIncrement = 1
        self.difficultyIncrement = 1
        self.score = 0
        
        """ initializing game physics """
        self.pongPosition = [0,0]
        self.pong2Position = [0,0]
        self.startPosition = [0,0]
        
        """ initializing controls """
        self.cursorPosition = [1,17]
        self.startPosition[0] = self.cursorPosition[0]
        self.startPosition[1] = self.cursorPosition[1]
        
        self.createDebugString()
        
    def setCursorPosition(self, newPosition):
        self.cursorPosition = newPosition
        self.state = 1
        self.createDebugString()
        
    def setPongPosition(self, newPosition):
        self.pongPosition = newPosition
        self.state = 1
        self.createDebugString()
        
    def createDebugString(self):
        cursorString = "cursor position: {}".format(self.cursorPosition)
        pongString = "pong position: {}".format(self.pongPosition)
        self.debugString = cursorString + "\n" + pongString
        
    def setState(self, state):
        super().setState(state)
        self.createDebugString()