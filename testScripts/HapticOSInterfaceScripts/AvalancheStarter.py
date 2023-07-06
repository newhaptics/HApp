# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:47:29 2023

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

# create the control center for llmOS resources
HapticsEngine = he.HapticsEngine()

# create the display to run the demo on
Display = td.TactileDisplay("Twoplex")
Display.connect("COM8")

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


def onPress(key):
    global KeyboardPeripheral
    KeyboardPeripheral.handleKeyPressEvent(key)
    
def onRelease(key):
    global KeyboardPeripheral
    KeyboardPeripheral.handleKeyReleaseEvent(key)

if __name__ == '__main__':

    app = qw.QApplication([])

    # begin executing HApp operations
    HapticsEngine.startLaunchingOperations(0)
    
    # add the render operation
    HapticsEngine.addOperation(he.RenderOperation("render", HapticsEngine.Graphics, Display))
    
    RomLauncher.startRom("Avalanche")
    key_listener = keyboard.Listener(on_press=onPress, on_release=onRelease)
    key_listener.start()
    sys.exit(app.exec_())