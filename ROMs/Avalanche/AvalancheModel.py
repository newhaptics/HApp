# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:49:54 2023

@author: Derek Joslin

"""

import time
import random
import AvalancheOperations as ao

class AvalancheModel:
    
    def __init__(self, HAppControlCenter, difficultySetting, debug):
        """ initializing rom resources """
        
        self.HAppControlCenter = HAppControlCenter
        self.TactileDisplay = self.HAppControlCenter.getPeripheral("NewHaptics Display SarissaV1")
        #displaySize = self.TactileDisplay.return_displaySize()
        self.nRows = 19#displaySize[0]
        self.nColumns = 41#displaySize[1]
        
        self.difficultySetting = difficultySetting
        
        self.startNewGame()
        
        # game settings
        self.echo = debug

# =============================================================================
#     def startMenu(self):
#         self.TactileDisplay.clear()
#         print("press space key to start")
#         self.TactileDisplay.braille((0,0),"press space key to start")
#         self.TactileDisplay.desired()
#         self.TactileDisplay.refresh()
#         self.TactileDisplay.state()
#         self.startNewGame()
# =============================================================================
        
    def mainGameLoop(self):
        
        self.gameDifficultyCalculation()
        
        self.gamePhysics()
        
        self.timingControls()
                       
        #self.peripheralCommunication()
        
        self.timingCalculations()
        
        #self.debugInfo()

    def gamePhysics(self):
        """ game physics """
        pongPosition = self.GameFlag.pongPosition
        cursorPosition = self.GameFlag.cursorPosition
        if (self.currentTime) > (self.avalancheTimer):
            pongPosition = self.avalanchePhysics(pongPosition, cursorPosition)
            self.GameFlag.setPongPosition(pongPosition)
            
        
        """
        if difficulty < 4 and (currentTime) > (avalancheTimer + 0.2):
            pong2Position = avalanchePhysics(pong2Position, cursorPosition)
        """
    
    def gameDifficultyCalculation(self):
        """ game difficulty calculation """
        
        if self.GameFlag.difficultyIncrement%5 == 0:
            #increase difficulty and display score
            self.GameFlag.difficultyIncrement = 1
            if self.GameFlag.difficulty > 1:
                self.GameFlag.difficulty = self.GameFlag.difficulty - 0.5
                print("difficulty increased to {}".format(self.GameFlag.difficulty))
                
        #print("Game Difficulty: {}".format(self.GameFlag.difficulty))

    
    def gameControlsUpdate(self):
        """ game controls update """
        pass
        #self.keyboardControl()
        #self.TactileDisplay.setCursorPosition(self.GameFlag.cursorPosition)

    
    def gameGraphicsRender(self):
        """ game graphics render """
        self.TactileDisplay.clear()
        self.TactileDisplay.line((self.GameFlag.pongPosition[1] - 2,self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1] - 2,self.GameFlag.pongPosition[0] + 2))
        self.TactileDisplay.line((self.GameFlag.pongPosition[1] - 1,self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1] - 1,self.GameFlag.pongPosition[0] + 2))
        self.TactileDisplay.line((self.GameFlag.pongPosition[1],self.GameFlag.pongPosition[0]), (self.GameFlag.pongPosition[1],self.GameFlag.pongPosition[0] + 2))
        
        self.TactileDisplay.line((self.GameFlag.cursorPosition[1], self.GameFlag.cursorPosition[0] - 2), (self.GameFlag.cursorPosition[1], self.GameFlag.cursorPosition[0] + 6))
        self.TactileDisplay.line((self.GameFlag.cursorPosition[1] + 1,self.GameFlag.cursorPosition[0] - 2), (self.GameFlag.cursorPosition[1] + 1,self.GameFlag.cursorPosition[0] + 6))

        
        """
        if difficulty < 4:
            self.TactileDisplay.line((self.pong2Position[1] - 2,self.pong2Position[0]), (self.pong2Position[1] - 2,self.pong2Position[0] + 2))
            self.TactileDisplay.line((self.pong2Position[1] - 1,self.pong2Position[0]), (self.pong2Position[1] - 1,self.pong2Position[0] + 2))
            self.TactileDisplay.line((self.pong2Position[1],self.pong2Position[0]), (self.pong2Position[1],self.pong2Position[0] + 2))
        """
        if self.echo:    
            print(self.GameFlag.pongPosition)
       
    
    def peripheralCommunication(self):
        """ communicate with peripherals """
        self.TactileDisplay.desired()
        self.TactileDisplay.refresh()
        
        self.TactileDisplay.state()
        
    def timingCalculations(self):
        """ timing calculations """
        self.toc = time.perf_counter()
        self.currentTime = self.toc - self.tic
        if self.echo:
            print(self.currentTime)
            
    def debugInfo(self):
        """ debug info """
        if self.echo:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("{0},{1}".format(self.GameFlag.cursorPosition[0],self.GameFlag.cursorPosition[1]))
            print(self.toc - self.tic)

    def timingControls(self):
        """ Timing Controls """
        if (self.currentTime) > (self.avalancheTimer):
            self.avalancheTimer += 0.2 + self.GameFlag.difficulty*0.2
            
        #print("timing controls: {}".format(self.avalancheTimer))
            
    def exitScreen(self):
        """ exit screen  """
        pass
# =============================================================================
#         print("You Lose!")
#         print("score is {}".format(self.score))
#         self.TactileDisplay.braille((0,0),"you lose score is {}".format(self.score))
#         self.TactileDisplay.desired()
#         self.TactileDisplay.refresh()
#         self.TactileDisplay.state()
# =============================================================================
        
    def scoreScreen(self):
        """ displays score """
        #self.TactileDisplay.clear()
        print("score is {}".format(self.score))
        x = -3
        y = 0
        for i in range(0,self.score):
            x += 3
            if x > 41:
                x = 0
                y += 4
            #self.TactileDisplay.rect((y,x),(y+2,x+1))
# =============================================================================
#         self.TactileDisplay.desired()
#         self.TactileDisplay.refresh()
#         self.TactileDisplay.state()
# =============================================================================
# =============================================================================
#         while not (keyboard.is_pressed(' ') or keyboard.is_pressed('o')):
#             pass
# =============================================================================

    def startNewGame(self):
        """ initializing game settings """
        self.GameFlag = ao.GameStateFlag("Game State Flag", self.difficultySetting)
        self.HAppControlCenter.addFlag(self.GameFlag)
# =============================================================================
#         """ establishing game mechanics """
#         self.xIncrement = 0
#         self.yIncrement = 1
#         self.GameFlag.difficultyIncrement = 1
#         self.score = 0
#         
#         """ initializing game physics """
#         self.tic = 0
#         self.GameFlag = ao.gameStateFlag("Game State Flag")
# =============================================================================
# =============================================================================
#         self.GameFlag.pongPosition = [0,0]
#         self.pong2Position = [0,0]
#         self.GameFlag.startPosition = [0,0]
#         
#         """ initializing controls """
#         self.GameFlag.cursorPosition = [1,1]
#         self.GameFlag.startPosition[0] = self.GameFlag.cursorPosition[0]
#         self.GameFlag.startPosition[1] = self.GameFlag.cursorPosition[1]
# =============================================================================

        """ initialize timers """
        self.tic = time.perf_counter()
        self.avalancheTimer = 0
        # self.keyboardTimer = 0
        self.toc = time.perf_counter()
        self.currentTime = self.toc - self.tic
        
    def exitRom(self):
        pass
        #self.TactileDisplay.disconnect()
        
    """ user input movement actions """
        
    def moveUp(self):
        pongPosition = self.GameFlag.pongPosition
        if pongPosition[1] > 0:
            pongPosition[1] -= 1
            self.GameFlag.setPongPosition(pongPosition)
        else:
            pass
        
    def moveDown(self):
        pongPosition = self.GameFlag.pongPosition
        if pongPosition[1] < 17:
            pongPosition[1] += 1
            self.GameFlag.setPongPosition(pongPosition)
        else:
            pass        
        
    def moveRight(self):
        cursorPosition = self.GameFlag.cursorPosition
        if cursorPosition[0] < 37:
            cursorPosition[0] += 3
            self.GameFlag.setCursorPosition(cursorPosition)
        else:
            pass
            
    def moveLeft(self):
        cursorPosition = self.GameFlag.cursorPosition
        if cursorPosition[0] > 0:
            cursorPosition[0] -= 3
            self.GameFlag.setCursorPosition(cursorPosition)
        else:
            pass
        
        
    """ Game Calculations """
        
    def createPaddles(self):
        
        #self.TactileDisplay.stroke(2)
        for paddleRow in range(0,int(self.GameFlag.difficulty),4):
            pass
            #self.TactileDisplay.line((18 - paddleRow,self.GameFlag.cursorPosition[0] - 4), (18 - paddleRow,self.GameFlag.cursorPosition[0] + 5))
        #self.TactileDisplay.stroke(1)
        """
        try:
            if cursorPosition[0] > 4:
                engine.line((16,cursorPosition[0]-3),(16,cursorPosition[0]-4))
            if cursorPosition[1] < 41:
                engine.line((16,cursorPosition[0]+3),(16,cursorPosition[0]+4))
        except:
            if echo:
                print("out of bounds")
                
        """
    def avalanchePhysics(self, position, cursorPosition):
        lineValues = [i for i in range(self.GameFlag.cursorPosition[0] - 4, self.GameFlag.cursorPosition[0] + 4)]
        yValues =  [17 - i for i in range(0,int(self.GameFlag.difficulty),4)]
        pongX = position[0]
        pongY = position[1]
        
        if pongX >= (self.nColumns):
            self.GameFlag.xIncrement = -1 
        
        if pongY >= (self.nRows):
            self.GameFlag.yIncrement = 0
        
        if pongX < 0:
            self.GameFlag.xIncrement = 1
            
        if pongY < 0:
            self.GameFlag.yIncrement = 1
            
        if (pongY in yValues) and (pongX in lineValues):
            pongX = random.randint(0,13)*3
            pongY = 0
            """
            if difficulty == 3:
                if pongX > 20:
                    xIncrement = -1
                else:
                    xIncrement = 1
            """
            self.GameFlag.score = self.GameFlag.score + 1
            self.GameFlag.difficultyIncrement = self.GameFlag.difficultyIncrement + 1
            
        newX = pongX + self.GameFlag.xIncrement
        newY = pongY + self.GameFlag.yIncrement
        if newY%4 is 0:
            newY = newY + self.GameFlag.yIncrement
        if newX%3 is 0:
            newX = newX + self.GameFlag.xIncrement
        
        return [newX,newY]


# =============================================================================
# #create the rom object with inputs
# #comport for the arduino tactile display
# #controls how fast avalanches fall 5-1
# #classic debug toggle 1-on 0-off
# 
# rom = romTemplate(engineComport, difficulty, echo)
# endRom = 0
# 
# while not keyboard.is_pressed('o') and (endRom is 0):
#     rom.startMenu()
#     rom.mainGameLoop()
#     rom.scoreScreen()
# else:
#     rom.exitScreen()
#     rom.exitRom()
# =============================================================================
