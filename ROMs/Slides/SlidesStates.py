# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:40:30 2022

@author: Derek Joslin
"""


import RomAPI as rs
import SlidesOperations as no
import SlidesMaster as sm

class SlidesStartMenu(rs.RomState):

    def __init__(self, Controller):
        #user can make custom state intialization 
        super().__init__(Controller)

    def stepState(self):
        #redefined by user in the appropriate subclass
        print('state running')
        
    def startState(self):
        #display the start screen
        #self.Controller.addEngineFunction(self.bootMenu)
        print('Start Menu Began')
        
    def closeState(self):
        #clear the screen of all information and shut down start screen processes
        print('Start Menu Close')

    def getNextState(self):
        #get values for the truth table
        return 'Text Editor'
        
class SlidesTool(rs.RomState):
    
    def __init__(self, Controller):
        #user can make custom state intialization 
        super().__init__(Controller)
        self.BrailleDisplay = self.Controller.HAppControlCenter.getPeripheral("Fourplex")
        self.displayText = ""

    def stepState(self):
        #redefined by user in the appropriate subclass
        #print('Editor running')
        pass
            
    def startState(self):
        # create the slides object
        print('Slides Tools Begin')
        if len(self.Controller.HAppControlCenter.getAllPeripherals()) < 2:
            # touch screen not connected
            print("touchscreen not connected")
            self.MasterModel = sm.SlidesMaster(self.Controller)
            self.MasterModel.selectTool("drawDot")
        else:
            # touch screen connected
            print("touchscreen is connected")
            self.MasterModel = sm.SlidesMaster(self.Controller)
            self.MasterModel.touchscreenStartUp()
            self.MasterModel.selectTool("drawDot")

        # set the mouse handler for the rom
        MousePeripheral = self.Controller.HAppControlCenter.getPeripheral("Master Mouse")
        MousePeripheral.setNewMouseHandler(self.MasterModel.MouseHandles)

        # set the keyboard handler for the rom
        KeyboardPeripheral = self.Controller.HAppControlCenter.getPeripheral("Master Keyboard")
        KeyboardPeripheral.setNewKeyboardHandler(self.MasterModel.KeyboardHandles)

        # set the visualization for the rom
        self.UpdateSlidesGuiOperation = no.UpdateSlidesGuiOperation("Update Slides Operation", self.Controller, self.MasterModel)
        self.Controller.HAppControlCenter.addOperation(self.UpdateSlidesGuiOperation)

    def closeState(self):
        #clear the screen of all information and shut down start screen processes
        print('Slides Tools Close')
        self.Controller.HAppControlCenter.removeFlag(self.MasterModel.ToolFlag.name)
        self.Controller.HAppControlCenter.removeFlag(self.MasterModel.DisplayFlag.name)
        self.Controller.HAppControlCenter.killOperation("ToolExecuterOperation")
        self.Controller.HAppControlCenter.removeOperation("ToolExecuterOperation")
        self.Controller.HAppControlCenter.killOperation("SlideOperation")
        self.Controller.HAppControlCenter.removeOperation("SlideOperation")

    def getNextState(self):
        if self.Controller.HAppControlCenter.exitEvent:

            return 'Exit Rom'

        else:
            #continue with program execution

            return 'Text Editor'
        
class SlidesExitState(rs.RomState):
    
    def __init__(self, Controller):
        #user can make custom state intialization 
        super().__init__(Controller)

    def stepState(self):
        #redefined by user in the appropriate subclass
        pass
    
    def startState(self):
        #display the start screen
        print('Exit State Began')
        # visualization
        romVisualization = self.Controller.HAppControlCenter.getVisualization("RomVisualizer")
        romVisualization.close()
        self.Controller.HAppControlCenter.removeVisualization("RomVisualizer")
                
        # set the mouse handler for the rom
        MousePeripheral = self.Controller.HAppControlCenter.getPeripheral("Master Mouse")
        MousePeripheral.setNewMouseHandler(rs.RomMouseHandles())
        
        # reset keyboard handles
        KeyboardPeripheral = self.Controller.HAppControlCenter.getPeripheral("Master Keyboard")
        KeyboardPeripheral.setNewKeyboardHandler(rs.RomKeyboardHandles())

    def closeState(self):
        #clear the screen of all information and shut down start screen processes
        print('Exit State Close')

    def getNextState(self):
        #get values for the truth table
        
        return 'Exit Rom'
