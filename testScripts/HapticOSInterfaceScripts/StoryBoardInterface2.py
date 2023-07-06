# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:29:29 2023

@author: derek
"""

import pygame
from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td

pygame.mixer.init()

Display = td.TactileDisplay("testDisplay")
Display.connect("COM4")
Engine = GraphicsEngine((41, 19))

def refreshDisplay():
    Engine.drawFeatures()

    mat = Engine.retrieveList()
    # set the desired to the edited
    Display.set_desiredState(mat)
    print("num: {}".format(0))
    print('---------------------------\n')
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                 for row in mat]))
    print('---------------------------\n')
    # push the desired into current
    Display.push_desiredState()
    Engine.clearFeatures()
   
    
pygame.mixer.music.load("Cave2/Cave1.mp3")
pygame.mixer.music.play()

input("Scene 1: Exploring HapticOS")     
pygame.mixer.music.load("Cave2/Cave2.mp3")
pygame.mixer.music.play()
# Scene 1
Engine.addBraille((0,0), "HapticOS is on press enter to begin")

refreshDisplay()

input("Scene 2: Navigating the HApp Manager")
pygame.mixer.music.load("Cave2/Cave3.mp3")
pygame.mixer.music.play()

# Scene 2
Engine.addLine((0, 0), (1, 2), 3)
# happ manager
Engine.addBraille((1,0), "Avalanche")
Engine.addBraille((1,1), "Slides")
Engine.addBraille((1,2), "Notepad")

# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 2.1: opening")
pygame.mixer.music.load("Cave2/Cave4.mp3")
pygame.mixer.music.play()

# Scene 2
Engine.addLine((0, 6), (2, 9), 3)

# happ manager
Engine.addBraille((1,0), "Avalanche")
Engine.addBraille((1,1), "Slides")
Engine.addBraille((1,2), "Notepad")

# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 3: Creating a new document")
pygame.mixer.music.load("Cave2/Cave5.mp3")
pygame.mixer.music.play()

# Scene 3
Engine.addLine((0, 0), (1, 2), 3)
# Notepad entry
# context dialog
Engine.addBraille((0,4), "Notepad")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 3.1: typing out document")
pygame.mixer.music.load("Cave2/Cave6.mp3")
pygame.mixer.music.play()

# Scene 3
# Notepad entry
Engine.addBraille((0,0), "Test Writing")

# context dialog
Engine.addBraille((0,4), "Notepad")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 4: Natural Language Command Line mode")
pygame.mixer.music.load("Cave2/Cave7.mp3")
pygame.mixer.music.play()
# Scene 4
Engine.addLine((0, 0), (1, 2), 3)

# context dialog
Engine.addBraille((0,4), "Exit")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 4.1: closing notepad")
pygame.mixer.music.load("Cave2/Cave8.mp3")
pygame.mixer.music.play()

# Scene 4
Engine.addBraille((0,0), "Close and Exit Notepad")

# context dialog
Engine.addBraille((0,4), "Exit")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 5: Opening Slides application")
pygame.mixer.music.load("Cave2/Cave9.mp3")
pygame.mixer.music.play()
# Scene 5
Engine.addBraille((0,0), "Open Slides")

# context dialog
Engine.addBraille((0,4), "Opened")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 6: in slides")
pygame.mixer.music.load("Cave2/Cave10.mp3")
pygame.mixer.music.play()
# Scene 6.1


# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 6.1: Using Slides application")
pygame.mixer.music.load("Cave2/Cave11.mp3")
pygame.mixer.music.play()

Engine.addTriangle([(0, 0), (0, 10), (40, 1)], 3)

# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 6.2: Closing Slides application")
pygame.mixer.music.load("Cave2/Cave12.mp3")
pygame.mixer.music.play()

# Scene 6.2
Engine.addBraille((0,0), "Save Slide and turn off slides")

# context dialog
Engine.addBraille((0,4), "Closed")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 7: back to happ")
pygame.mixer.music.load("Cave2/Cave13.mp3")
pygame.mixer.music.play()
# Scene 7
# happ manager
Engine.addBraille((1,0), "Slides")
Engine.addBraille((1,1), "Notepad")
Engine.addBraille((1,2), "Avalanche")

# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 7.1: Avalanche")
pygame.mixer.music.load("Cave2/Cave14.mp3")
pygame.mixer.music.play()
# Scene 7
# happ manager
Engine.addBraille((1,0), "Slides")
Engine.addBraille((1,1), "Notepad")
Engine.addBraille((1,2), "Avalanche")

# context dialog
Engine.addBraille((0,4), "HApps")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()


input("Scene 8: Opening Avalanche application")
pygame.mixer.music.load("Cave2/Cave15.mp3")
pygame.mixer.music.play()

Engine.addLine((0, 17), (5, 17), 3)
Engine.addLine((0, 0), (1, 2), 3)

# context dialog
#Engine.addBraille((0,4), "Avalanche")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 9: Closing Avalanche application")
pygame.mixer.music.load("Cave2/Cave16.mp3")
pygame.mixer.music.play()
refreshDisplay()