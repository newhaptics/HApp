# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:25:46 2022

@author: Derek Joslin

"""

import RomAPI as rs

class SlidesMouseHandles(rs.RomMouseHandles):
    
    def __init__(self, MasterModel):
        super().__init__()
        
        self.MasterModel = MasterModel
        #self.VisualizerOperator = self.MasterModel.Controller.HAppControlCenter.getOperation("StateVisualizerRefreshOperation")
        self.VisualizerOperator = self.MasterModel.Controller.HAppControlCenter.getOperation("TouchVisualizerRefreshOperation")
        
    def LeftButtonHandler(self, xCoordinate, yCoordinate):
        # Mouse click event for visualizer operator
        scaler = self.VisualizerOperator.scaler
        
        # get the pin position from GUI coordinate
        scaledDict = scaler.scale(xCoordinate, yCoordinate, "visualizer")
         
        # get the pin coordinate to highlight
        xPinCoordinate = scaledDict["pin"][0]
        yPinCoordinate = scaledDict["pin"][1]
                
        #self.MasterModel.parameterClicked([int(pinSelected[1]), int(pinSelected[0])])
        self.MasterModel.parameterClicked([int(yPinCoordinate), int(xPinCoordinate)])
        
# =============================================================================
#     def MoveHandler(self, xCoordinate, yCoordinate):
#         # Turn off the touch screen tracker
#         #self.VisualizerOperator.moveAction(xCoordinate, yCoordinate)
# =============================================================================