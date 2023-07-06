# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:51:04 2023

@author: Derek Joslin

"""

import pygame

from GraphicsEngine import *
import Features as f
import numpy as np
from pynput import keyboard


class ModalInterface():
    
    def __init__(self, GraphicsEngine, RomLauncher, node):

        self.Engine = GraphicsEngine
        self.currentNode = node
        self.RomLauncher = RomLauncher
        pygame.mixer.init()

        self.voice = "Boring"
        self.mode = 0
        self.cursor = 0
        self.romOn = 0

    def refreshDisplay(self):
        self.Engine.drawFeatures()
        
        mat = self.Engine.retrieveList()
        # set the desired to the edited
        self.Display.set_desiredState(mat)
        print("num: {}".format(0))
        print('---------------------------\n')
        print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                     for row in mat]))
        print('---------------------------\n')
        # push the desired into current
        self.Display.push_desiredState()
        self.Engine.clearFeatures()
    
    def drawHAppManager(self):
        # happ manager
        nColumns = self.Engine.dimensions[0]
        self.Engine.clearFeatures()
        self.Engine.addBraille((0,self.cursor), "Y")
        self.Engine.addBraille((1,0), "Notepad")
        self.Engine.addBraille((1,1), "Slides")
        self.Engine.addBraille((1,2), "Avalanche")
    
        # context dialog
        self.Engine.addBraille((0,4), "HApps")
    
        # modal inteface
        self.Engine.addBraille((int(nColumns/3)-1,4), "H")
        #self.refreshDisplay()
        
    def drawCommandLine(self):
        # context dialog
        nColumns = self.Engine.dimensions[0]

        self.Engine.clearFeatures()
        self.Engine.addBraille((0,self.cursor), "Y")
        self.Engine.addBraille((0,4), "Command")
    
        # modal inteface
        self.Engine.addBraille((int(nColumns/3),4), "C")
        #self.refreshDisplay()
    
    """ Keyboard related functions """
    
    def onPress(self, key):
        

        if key == keyboard.Key.up:
            if self.cursor > 0:
                self.cursor -= 1
                print(self.cursor)
            
        elif key == keyboard.Key.down:
            if self.cursor < 3:
                self.cursor += 1
                print(self.cursor)
        
        if key == keyboard.Key.ctrl_l:
            if self.mode:
                print("HApp Mode")
                self.mode = 0
                pygame.mixer.music.load("{}/HAppMode.mp3".format(self.voice))
                pygame.mixer.music.play()
                if self.romOn:
                    self.RomLauncher.resumeRom("Avalanche")
                
            else:
                print("Command Line Mode")
                self.mode = 1
                self.cursor = 0
                pygame.mixer.music.load("{}/CommandLineMode.mp3".format(self.voice))
                pygame.mixer.music.play()
                if self.romOn:
                    self.RomLauncher.pauseRom("Avalanche")
                
        if key == keyboard.Key.enter:
            if self.mode == 1:
                pass
            elif self.mode == 0:
                # draw current node
                
                if not self.romOn:
                    if self.cursor == 0:
                        print("running notepad")
                        # launch the notepad
                        pygame.mixer.music.load("{}/RunningNotepad.mp3".format(self.voice))
                        pygame.mixer.music.play()
                        self.currentHApp = "Notepad"
                    elif self.cursor == 1:
                        print("running slides")
                        pygame.mixer.music.load("{}/RunningSlides.mp3".format(self.voice))
                        pygame.mixer.music.play()
                        self.currentHApp = "Slides"
                    elif self.cursor == 2:
                        print("running avalanche")
                        pygame.mixer.music.load("{}/RunningAvalanche.mp3".format(self.voice))
                        pygame.mixer.music.play()
                        self.RomLauncher.startRom("Avalanche")
                        self.currentHApp = "Avalanche"
                        self.romOn = 1
                        
        if key == keyboard.Key.esc:
            if self.romOn:
              if self.currentHApp == "Notepad":
                  print("closing notepad")
                  # launch the notepad
                  pygame.mixer.music.load("{}/ClosingNotepad.mp3".format(self.voice))
                  pygame.mixer.music.play()
              elif self.currentHApp == "Slides":
                  print("closing slides")
                  pygame.mixer.music.load("{}/ClosingSlides.mp3".format(self.voice))
                  pygame.mixer.music.play()
              elif self.currentHApp == "Avalanche":
                  print("closing avalanche")
                  pygame.mixer.music.load("{}/ClosingAvalanche.mp3".format(self.voice))
                  pygame.mixer.music.play()
                  self.RomLauncher.endRom()
                  self.currentHApp = ""
                  self.romOn = 0
                    
        if key == keyboard.Key.tab:
            if self.voice == "CaveNav":
                self.voice = "Boring"
                pygame.mixer.music.load("{}/HI.mp3".format(self.voice))
                pygame.mixer.music.play()
            elif self.voice == "Boring":
                self.voice = "AbsolutelyDisgusting"
                pygame.mixer.music.load("{}/HI.mp3".format(self.voice))
                pygame.mixer.music.play()
            else:
                self.voice = "CaveNav"
                pygame.mixer.music.load("{}/HI.mp3".format(self.voice))
                pygame.mixer.music.play()
        
        if not self.romOn:
            if not self.mode:
                self.drawHAppManager()
            else:
                self.drawCommandLine()