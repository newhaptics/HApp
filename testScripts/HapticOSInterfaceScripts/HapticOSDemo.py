# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:13:11 2023

@author: Derek Joslin

"""
from PyQt5 import QtWidgets as qw
import sys

import HapticsEngine as he
from GraphicsEngine import *

import RomLauncher as rl
import TactileDisplay as td

import KeyboardPeripheral as kb
import DefaultKeyboardHandles as dk

from pynput import keyboard

from ModalAction import M od
alInterface
from AccessTreeTesting import *

HappManager = TreeNode("HApp Manager")
Notepad = TreeNode("Notepad")
  Slides = TreeNode("Slides")
Avalanche = TreeNode("Avalanche")

HappManager.addChild(Notepad)
Ha  ppManager.addChild(Slides)
HappManager.addChild(Avalanche)

 
# create the control center for llmOS resources
HapticsEngine = he.HapticsEngine()

# create the display to run the demo on
Display = td.TactileDisplay("Twoplex")
Display.connect("COM4")

# add the tactile display to the HapticsEngine
HapticsEngine.addPeripheral(Display)

# create a keyboard to use during the demo
DefaultKeyboardHandles = dk.DefaultKeyboardHandles()
KeyboardPeripheral = kb.KeyboardPeripheral("Master Keyboard", DefaultKeyboardHandles)
HapticsEngine.addPeripheral(KeyboardPeripheral)

# grab the file and peripheral manager
FileManager = HapticsEngine.FileManager
PeripheralManager = HapticsEngine.PeripheralManager

# create the RomLauncher
romDictionary = FileManager.createRomDirectory()
RomLauncher = rl.RomLauncher(HapticsEngine, romDictionary)

interface = ModalInterface(HapticsEngine.Graphics, RomLauncher, HappManager)

def onPress(key):
    global KeyboardPeripheral
    global interface
    if interface.mode:
        interface.onPress(key)
    else:
        interface.onPress(key)
        KeyboardPeripheral.handleKeyPressEvent(key)

def onRelease(key):
    global KeyboardPeripheral
    if not interface.mode:
        KeyboardPeripheral.handleKeyReleaseEvent(key)
    

if __name__ == '__main__':

    app = qw.QApplication([])

    # begin executing HApp operations
    HapticsEngine.startLaunchingOperations(0)
    
    # add the render operation
    HapticsEngine.addOperation(he.RenderOperation("render", HapticsEngine.Graphics, Display))
    

    key_listener = keyboard.Listener(on_press=onPress, on_release=onRelease)
    key_listener.start()
    
    sys.exit(app.exec_())