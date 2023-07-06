# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:50:55 2023

@author: Derek Joslin

"""

import RomAPI as rs
import time

class AvalancheGraphicsRender(rs.RomOperation):

    def __init__(self, name, GraphicsEngine, GameFlag):
        super().__init__(name)

        # inputs to the operation
        self.GameFlag = GameFlag
        self.inputDictionary["Game Flag"] = self.GameFlag

        self.GraphicsEngine = GraphicsEngine
        self.outputDictionary["Graphics Engine"] = self.GraphicsEngine

        executionParameters = {
            "executeOnFlags": [self.GameFlag], # a set of flag dependencies that when met start executing the Operation
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
        }

        self.setExecutionParameters(executionParameters)

        # provide a description
        self.description = "This operation refreshs the display when physics are updated. It's execution is interuppt based."

        self.executable = self.execute

        self.createDebugString()

    def checkFlagConditions(self):
        # grab the state of ToolFlag
        updateState = self.GameFlag.state

        if updateState:
            # compare the flag matrix to the current state of the Tactile Display
            self.GameFlag.setState(0)
            return True
        else:
            # if they are not the same then return false
            return False

    def execute(self):

        if self.GameFlag.gameState == "Start Menu":
            self.renderStartMenu()

        elif self.GameFlag.gameState == "Game":
            # render the graphics on the display
            self.renderIcicle()

            self.renderUserBar()

        elif self.GameFlag.gameState == "Score Menu":
            self.renderScoreScreen()
        else:
            self.renderExitScreen()

    def renderIcicle(self):
        self.GraphicsEngine.clearFeatures()
        # render the avalanche object
        #self.GraphicsEngine.addLine((self.GameFlag.pongPosition[0],self.GameFlag.pongPosition[1] - 2), (self.GameFlag.pongPosition[0] + 2,self.GameFlag.pongPosition[1] - 2), 1)
        self.GraphicsEngine.addLine((self.GameFlag.pongPosition[0],self.GameFlag.pongPosition[1] - 1), (self.GameFlag.pongPosition[0] + 1,self.GameFlag.pongPosition[1] - 2), 1)
        self.GraphicsEngine.addLine((self.GameFlag.pongPosition[0],self.GameFlag.pongPosition[1]), (self.GameFlag.pongPosition[0] + 2,self.GameFlag.pongPosition[1]), 1)

    def renderUserBar(self):
        # render the cursor as a line
        self.GraphicsEngine.addLine((self.GameFlag.cursorPosition[0] - 1, self.GameFlag.cursorPosition[1]), (self.GameFlag.cursorPosition[0] + 7, self.GameFlag.cursorPosition[1]), 1)
        self.GraphicsEngine.addLine((self.GameFlag.cursorPosition[0] - 1,self.GameFlag.cursorPosition[1] + 1), (self.GameFlag.cursorPosition[0] + 7,self.GameFlag.cursorPosition[1] + 1), 1)

    def renderStartMenu(self):
        self.GraphicsEngine.clearFeatures()
        print("press space key to start")
        self.GraphicsEngine.addBraille((0,0),"press space key")
        self.GraphicsEngine.addBraille((0,1),"to start")
    def renderExitScreen(self):
        """ exit screen  """
        print("You Lose!")
        print("score is {}".format(self.GameFlag.score))
        self.GraphicsEngine.addBraille((0,0),"you lose score")
        self.GraphicsEngine.addBraille((0,1),"is {}".format(self.GameFlag.score))
    def renderScoreScreen(self):
        """ displays score """
        self.GraphicsEngine.clearFeatures()
        #print("score is {}".format(self.GameFlag.score))
        x = -3
        y = 0
        for i in range(0,self.GameFlag.score):
            x += 3
            if x > self.GameFlag.nColumns:
                x = 0
                y += 4
            self.GraphicsEngine.addRectangle((x,y),(x+1,y+2), 1)

    def stopOperation(self):
        # delete the timer for the operation by running the super class function
        super().stopOperation()

        # mark isStopped as false so the function is not killed
        self.isStopped = False

class GameStateFlag(rs.RomFlag):

    def __init__(self, name, difficulty):
        super().__init__(name)
        self.debugString = "This flag indicates where the pong and cursor is."
        self.gameState = "Start Menu"
        self.defaultDifficulty = difficulty
        self.resetGame()

        # store the display size
        self.nColumns = 0
        self.nRows = 0

    def resetGame(self):

        """ establishing game mechanics """
        self.xIncrement = 0
        self.yIncrement = 1
        self.difficultyIncrement = 1
        self.difficulty = self.defaultDifficulty
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

    def setGameState(self, stateString):
        self.gameState = stateString

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
        gameStateString = "current Game State: {}".format(self.gameState)
        scoreString = "current Score: {}".format(self.score)

        self.debugString = cursorString + "\n" + pongString + "\n" + gameStateString + "\n" + scoreString

    def setState(self, state):
        super().setState(state)
        self.createDebugString()
