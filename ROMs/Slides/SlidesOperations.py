# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:40:31 2022

@author: Derek Joslin

"""

import RomAPI as rs
import SlidesGui as sg
import SlidesTools as st

class ToolExecutionOperation(rs.RomOperation):
    
    def __init__(self, name, TactileDisplay, ToolFlag):
        super().__init__(name)
        self.Toolchain = st.SlidesTools(TactileDisplay)
        
        # inputs to the operation
        self.ToolFlag = ToolFlag
        self.inputDictionary[self.ToolFlag.name] = self.ToolFlag
        
        # outputs to the operation
        self.TactileDisplay = TactileDisplay
        self.outputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        # provide a description
        self.description = "This operation checks the ToolFlag to see if a tool may be executed."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeOnFlags": [self.ToolFlag], # a set of flag dependencies that when met start executing the Operation
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString()
        
    def checkFlagConditions(self):
        try:
            # grab the state of ToolFlag
            selectedTool = self.ToolFlag.state
            
            # grab the parameters of ToolFlag
            selectedParameters = self.ToolFlag.parameters
            
            # Using slidesTools determine the condition
            toolFunctions = self.Toolchain.toolFunctions
            
            toolKeyList = []
            for toolKey in toolFunctions:
                toolKeyList.append(toolKey)
            
            # full copy this
            toolParameterDictionary = self.Toolchain.toolParameters
            
            # if state is in toolKeyList it is a legitimate tool
            if selectedTool in toolKeyList:
                # tool is legitimate
                neededParameters = toolParameterDictionary[selectedTool]
                self.ToolFlag.neededParameters = len(neededParameters)
                if len(selectedParameters) == len(neededParameters):
                    # if there are enough porameters to execute the tool then execute
                    # if the number of tool execution parameters is greater than 0
                    return True
                elif len(selectedParameters) > len(neededParameters):
                    # check if the selected parameters are too numerous
                    print("error more parameters than needed")
                    
                    # auto clear the parameters
                    self.ToolFlag.parameters = []
                    return False
                else:
                    return False
            else:
                # tool is not legitimate
                return False
        except Exception as e:
            print(e)
            self.ToolFlag.parameters = []
        
    def stopOperation(self):
        # delete the timer for the operation by running the super class function
        super().stopOperation()
        
        # mark isStopped as false so the function is not killed
        self.isStopped = False
        
    def execute(self):
        try:
            # execute the proper tool
            # grab the state of ToolFlag
            selectedTool = self.ToolFlag.state
            
            # grab the parameters of ToolFlag
            selectedParameters = self.ToolFlag.parameters
            
            # Using slidesTools determine the condition
            toolFunctions = self.Toolchain.toolFunctions
            
            toolKeyList = []
            for toolKey in toolFunctions:
                toolKeyList.append(toolKey)
            
            # full copy this
            toolParameterDictionary = self.Toolchain.toolParameters
            
            parameterKeys = toolParameterDictionary[selectedTool]
            
            print("tool executed {}".format(self.ToolFlag.state))
            
            funcHandle = toolFunctions[selectedTool]
            toolParameterKwargs = dict(zip(parameterKeys, selectedParameters))
            
            # add in auto clear
            if self.ToolFlag.autoClear:
                clearHandle = toolFunctions["selectClear"]
                self.Toolchain.setTool(clearHandle, {})
                self.Toolchain.executeSelectedTool()
            
            
            self.Toolchain.setTool(funcHandle, toolParameterKwargs)
            
            self.Toolchain.executeSelectedTool()
    
            self.TactileDisplay.refresh()
            
            if len(selectedParameters) == 0:
                self.ToolFlag.clearState()
                self.ToolFlag.clearParameters()
            else:
                self.ToolFlag.clearParameters()
        except Exception as e:
            print(e)
            self.ToolFlag.parameters = []

class LoadSlideOperation(rs.RomOperation):
    
    def __init__(self, name, TactileDisplay, DisplayFlag):
        super().__init__(name)
        #self.Toolchain = st.SlidesTools()
        
        # inputs to the operation
        self.DisplayFlag = DisplayFlag
        self.inputDictionary[self.DisplayFlag.name] = self.DisplayFlag
        
        self.TactileDisplay = TactileDisplay
        self.outputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        # provide a description
        self.description = "This operation sends the update state to the braille display when necessary."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeOnFlags": [self.DisplayFlag], # a set of flag dependencies that when met start executing the Operation
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString()
        
    def checkFlagConditions(self):
        # grab the state of ToolFlag
        displayState = self.DisplayFlag.state
        
        # get the current state of the tactile display
        #currentState = self.TactileDisplay.return_currentState()
        if displayState:
            # compare the flag matrix to the current state of the Tactile Display
            print("load slides passed")
            return True
        else:
            # if they are not the same then return false
            return False
        
    def stopOperation(self):
        # delete the timer for the operation by running the super class function
        super().stopOperation()
        
        # mark isStopped as false so the function is not killed
        self.isStopped = False
        
    def execute(self):
        # load the slide which is selected
        try:
            flagMatrix = self.DisplayFlag.matrix

            self.TactileDisplay.setMat(flagMatrix)
            self.TactileDisplay.refresh()

            self.DisplayFlag.clearState()
        except Exception as e:
            print(e)
        
class UpdateSlidesGuiOperation(rs.RomOperation):
    
    def __init__(self, name, Controller, MasterModel):
        super().__init__(name)
        self.Controller = Controller
        self.MasterModel = MasterModel
        
        # inputs to the operation
        self.TactileDisplay = self.Controller.HAppControlCenter.getPeripheral("Fourplex")
        self.inputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        # outputs to the operation
        self.RomVisualization = self.Controller.HAppControlCenter.getVisualization("RomVisualizer")
        self.outputDictionary[self.RomVisualization.name] = self.RomVisualization
        
        # provide a description
        self.description = "This operation creates the slides visualizer window."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
            "executeContinuously": False, # a boolean value that determines if the Operation will execute forever    
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString()
        
    def execute(self):
        print("Loading ROM visualizations...")
        self.RomVisualizer = self.Controller.HAppControlCenter.getVisualization("RomVisualizer")
        self.VisualizationWindow = self.RomVisualizer.RomExplorer
        
        # need to only run once
        self.SlidesVisualizationHandles = sg.SlidesVisualizationHandles(self.VisualizationWindow, self.MasterModel)
        
        self.RomVisualization.VisualizationHandler.setNewRomVisualizationHandler(self.SlidesVisualizationHandles)
        
        # create the visualization for the slides rom
        self.SlidesVisualizationHandles.createSlideButtons(self.MasterModel.FileManager.currentNumSlides())

        self.RomVisualization.show()

class AutoExecuteParameterOperation(rs.RomOperation):

    def __init__(self, name, MasterModel, TouchFlag):
        super().__init__(name)
        
# =============================================================================
#         # inputs to the operation
#         self.MasterModel = MasterModel
#         self.inputDictionary[self.MasterModel.name] = self.MasterModel
# =============================================================================
        self.MasterModel = MasterModel        

# =============================================================================
#         # inputs to the operation
#         self.Touchscreen = Touchscreen
#         self.inputDictionary[self.Touchscreen.name] = self.Touchscreen
# =============================================================================
        
        self.oldTouchPoints = self.MasterModel.getTouchPoints()
        
        # outputs to the ToolFlag
        self.TouchFlag = TouchFlag
        self.outputDictionary[self.TouchFlag.name] = self.TouchFlag
        
        # provide a description
        self.description = "checks if the touch inputs have changed and then sets tool parameters to those changed touch inputs."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeOnFlags": [self.TouchFlag], # a set of flag dependencies that when met start executing the Operation
            "executeDelay": 0, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString() 
        
        
    def checkFlagConditions(self):
        # grab the state of TouchFlag
        self.MasterModel.getTouchPoints()
        
        # get the current state of the tactile display
        #currentState = self.TactileDisplay.return_currentState()
        if self.TouchFlag.state != self.oldTouchPoints:
            # compare the flag matrix to the current state of the Tactile Display
            self.oldTouchPoints = self.TouchFlag.state
            print(self.oldTouchPoints)
            return True
        else:
            # if they are not the same then return false
            return False

    def stopOperation(self):
        # delete the timer for the operation by running the super class function
        super().stopOperation()
        
        # mark isStopped as false so the function is not killed
        self.isStopped = False

    def execute(self):
        # execute the touch points
        self.MasterModel.registerTouchParameters()


class TouchFlag(rs.RomFlag):
    
    def __init__(self, name):
        super().__init__(name)
        self.debugString = "create this flag to store the touch points of the touch screen as pin points"
        self.state = []

class ToolFlag(rs.RomFlag):
    
    def __init__(self, name):
        super().__init__(name)
        self.debugString = "This flag indicates the state of the selected tool and tool parameters"
        self.neededParameters = 0
        self.parameters = []
        self.autoClear = 0
        
        # auto execute mode
        self.autoExecute = 0
        
    def clearState(self):
        self.state = 0
        self.parameters.clear()
        self.debugString = "parameters: {}".format(self.parameters)        
        self.debugString += "\nparameter # {}".format(self.neededParameters)
        
    def clearParameters(self):
        self.parameters.clear()
        self.debugString = "parameters: {}".format(self.parameters)        
        self.debugString += "\nparameter # {}".format(self.neededParameters)

    def addParameter(self, param):
        self.parameters.append(param)
        self.debugString = "parameters: {}".format(self.parameters)
        self.debugString += "\nparameter # {}".format(self.neededParameters)

        
class DisplayFlag(rs.RomFlag):
    
    def __init__(self, name):
        super().__init__(name)
        self.debugString = "This flag indicates to send the state"
        self.matrix = 0
        
    def clearState(self):
        super().clearState()
        self.matrix = 0
        
    def setMatrix(self, state):
        self.matrix = state