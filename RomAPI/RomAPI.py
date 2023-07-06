# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:18:01 2022

@author: Derek Joslin
"""

import ctypes
import time
import DefaultKeyboardHandles as dk
import DefaultMouseHandles as dm
import DefaultRomVisualizationHandles as dr
import OperationsManager as om
import FlagManager as fm

class RomController():

    def __init__(self, HapticsEngineAddress, stopEvent):
        # define the state objects (user reimplements this and adds to dictionary)
        # current state of rom (user can intialize a default state)
        self.stateKey = ''

        # available states for the rom
        self.romStateDictionary = {}

        print(HapticsEngineAddress)
        # load in the haptics engine
        self.HAppControlCenter = ctypes.cast(HapticsEngineAddress, ctypes.py_object).value

        self.stopEvent = stopEvent

    def startCurrentState(self):
        #get the current rom that is running and run its step function
        currentState = self.getCurrentState()

        currentState.startState()

    def stepCurrentState(self):
        #get the current rom that is running and run its step function
        currentState = self.getCurrentState()

        currentState.stepState()

    def decideNextState(self):

        #get the rom's current state
        currentState = self.getCurrentState()
        oldStateKey = self.stateKey

        #calculate which state to go to next from current state
        newStateKey = currentState.getNextState()

        #if new State Key is rom exit exit rom immediately
        #switch to the next rom state or if the same state do nothing
        if oldStateKey == newStateKey:
            pass

        else:
            #close all operations of the current state
            currentState.closeState()

            #initialize all of the operations of the next state
            nextState = self.romStateDictionary[newStateKey]
            nextState.startState()

            #switch to the next state
            self.switchState(newStateKey)

    def getCurrentState(self):
        return self.romStateDictionary[self.stateKey]

    def switchState(self, stateKey):
        self.stateKey = stateKey

    def exitRom(self):
        pass

    def runRom(self):
        # Main loop of the Rom
        shouldRomEnd = self.HAppControlCenter.exitEvent
        currentState = self.getCurrentState()
        currentState.startState()
        while shouldRomEnd == 0:

            #always step one tick into the current state
            self.stepCurrentState()

            #decide if peripheral communication is going to occur
            #Put NHAPI functions in here
            #self.runEngineBuffer()

            #decide the next state to move into
            self.decideNextState()

            time.sleep(0.001)
            self.stopEvent.wait()

            shouldRomEnd =  self.HAppControlCenter.exitEvent#something which can change from main loop

        else:
            #decide the next state to move into
            self.decideNextState()
            self.stepCurrentState()
            self.exitRom()
            self.HAppControlCenter.exitEvent = 0

class RomState():

    def __init__(self, Controller):
        #pass the rom controller into the state
        self.Controller = Controller

    def stepState(self):
        #redefined by user in the appropriate subclass
        pass

    def startState(self):
        #display the start screen
        #self.Controller.addEngineFunction(self.bootMenu)
        pass

    def closeState(self):
        #clear the screen of all information and shut down start screen processes
        pass

    def getNextState(self, RomController):
        #get values for the truth table
        pass

class RomKeyboardHandles(dk.DefaultKeyboardHandles):

    def __init__(self):
        super().__init__()

class RomMouseHandles(dm.DefaultMouseHandles):

    def __init__(self):
        super().__init__()

class RomOperation(om.Operation):

    def __init__(self, name):
        super().__init__(name)

class RomFlag(fm.Flag):

    def __init__(self, name):
        super().__init__(name)

class RomVisualizationHandles(dr.DefaultRomVisualizationHandles):

    def __init__(self):
        super().__init__()
