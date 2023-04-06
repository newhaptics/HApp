# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:45:42 2023

@author: Derek Joslin

"""

import OperationsManager as om
from GraphicsEngine import *

class GraphicsRenderOperation(om.Operation):
    
    def __init__(self, name, TactileDisplay):
        super().__init__(name)
        # outputs to the operation
        self.engine = GraphicsEngine((83, 19))
        
        # outputs to the operation
        self.TactileDisplay = TactileDisplay
        self.outputDictionary[TactileDisplay.name] = self.TactileDisplay

        # provide a description
        self.description = "Engine for rendering graphics on the tacitile display."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeDelay": 500, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
            "executeContinuously": True, # a boolean value that determines if the Operation will execute forever
            "executionIntervalTime": 1, # an interval in milliseconds that determines the time between execution
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString()
    
    def execute(self):
        # draw the features on the tactile display
        self.engine.drawFeatures()
        output = self.engine.retrieveList()
        self.TactileDisplay.set_desiredState(output)
        self.TactileDisplay.push_desiredState()