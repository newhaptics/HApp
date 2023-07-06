# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:54:08 2023

@author: Derek Joslin

"""
from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td

Display = td.TactileDisplay("testDisplay")
Display.connect("COM6")
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
   
input("Scene 1: Exploring HapticOS")     
# Scene 1
Engine.addBraille((0,0), "HapticOS is on press enter to begin")

refreshDisplay()

input("Scene 2: Navigating the HApp Manager")
# Scene 2
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
# Scene 3
# Notepad entry
Engine.addBraille((0,0), "Test Writing")

# context dialog
Engine.addBraille((0,4), "Notepad")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 4: Natural Language Command Line mode")
# Scene 4
Engine.addBraille((0,0), "Close and Exit Notepad")

# context dialog
Engine.addBraille((0,4), "Exit")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 5: Opening Slides application")
# Scene 5
Engine.addBraille((0,0), "Open Slides")

# context dialog
Engine.addBraille((0,4), "Opened")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 6: Drawing a basic imager")
# Scene 6.1
Engine.addTriangle([(0, 0), (0, 10), (40, 1)], 3)

# context dialog
Engine.addBraille((0,4), "")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 6.2")
# Scene 6.2
Engine.addBraille((0,0), "Save Slide and turn off slides")

# context dialog
Engine.addBraille((0,4), "Closed")

# modal inteface
Engine.addBraille((13,4), "N")

refreshDisplay()

input("Scene 7: Selecting HApp Manager Mode")
# Scene 7
# happ manager
Engine.addBraille((1,0), "Slides")
Engine.addBraille((1,1), "Notepad")
Engine.addBraille((1,2), "Avalanche")

# context dialog
Engine.addBraille((0,4), "Manager")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 8: Opening the game Avalanche")
# Scene 8
# happ manager
Engine.addBraille((1,0), "Slides")
Engine.addBraille((1,1), "Notepad")
Engine.addBraille((1,2), "Avalanche")

# context dialog
Engine.addBraille((0,4), "Manager")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()

input("Scene 9: Playing and closing the game")
# Scene 9
Engine.addLine((0, 17), (5, 17), 3)
Engine.addLine((0, 0), (1, 2), 3)

# context dialog
#Engine.addBraille((0,4), "Avalanche")

# modal inteface
Engine.addBraille((12,4), "H")

refreshDisplay()