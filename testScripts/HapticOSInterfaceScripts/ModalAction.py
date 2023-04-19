# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:51:04 2023

@author: Derek Joslin

"""


from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td
from pynput import keyboard

Display = td.TactileDisplay("testDisplay")
Display.connect("COM4")
Engine = GraphicsEngine((41, 19))

mode = 0
cursor = 0

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

def HAppManager():
    # happ manager
    Engine.addBraille((1,0), "Avalanche")
    Engine.addBraille((1,1), "Slides")
    Engine.addBraille((1,2), "Notepad")

    # context dialog
    Engine.addBraille((0,4), "HApps")

    # modal inteface
    Engine.addBraille((12,4), "H")
    
def moveCursor():
    global cursor
    
    Engine.addBraille((0,cursor), "Y")
    
def CommandLine():
    # context dialog
    Engine.addBraille((0,4), "Command")

    # modal inteface
    Engine.addBraille((13,4), "N")

""" Keyboard related functions """

def onPress(key):
    global mode
    global cursor
    
    if key == keyboard.Key.up:
        if cursor > 0:
            cursor -= 1
            moveCursor()
            if not mode:    
                HAppManager()
            else:
                CommandLine()
            refreshDisplay()
        
    elif key == keyboard.Key.down:
        if cursor < 3:
            cursor += 1
            moveCursor()
            if not mode:
                HAppManager()
            else:
                CommandLine()
            refreshDisplay()
    
    if key == keyboard.Key.ctrl_l:
        if mode:
            mode = 0
            # modal inteface
            moveCursor()
            HAppManager()
            refreshDisplay()
        else:
            mode = 1
            cursor = 0
            moveCursor()
            # modal inteface
            CommandLine()
            refreshDisplay()


key_listener = keyboard.Listener(on_press=onPress)
key_listener.start()