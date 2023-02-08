# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:40:31 2022

@author: Derek Joslin

"""


import RomAPI as rs

import DefaultKeyboardHandles as dh

class SlidesKeyboardHandles(dh.DefaultKeyboardHandles):
    
    def __init__(self, MasterModel):
        super().__init__()
        self.MasterModel = MasterModel
        #self.VisualizerOperator = self.MasterModel.Controller.OperationsController.getOperation("VisualizationRefreshOperation")


# =============================================================================
#     def KeySpaceHandler(self):
#         # Space bar event for visualizer operator
#         # self.VisualizerOperator.clickSelect(xCoordinate, yCoordinate)
#         
#         pinSelected = self.VisualizerOperator.getPinPosition()
#         
#         print(pinSelected)
#         
#         self.MasterModel.parameterClicked([int(pinSelected[1]), int(pinSelected[0])])
#         
#     def KeyF1Handler(self):
#         self.MasterModel.selectTool("drawDot")
#         
#     def KeyF2Handler(self):
#         self.MasterModel.selectTool("drawLine")
#         
#     def KeyF3Handler(self):
#         self.MasterModel.selectTool("drawCurve")
#         
# # =============================================================================
# #     def KeyF4Handler(self):
# #         self.MasterModel.selectTool("drawCircle")
# # =============================================================================
#         
#     def KeyF5Handler(self):
#         self.MasterModel.selectTool("drawRectangle")
# 
#     def KeyF6Handler(self):
#         self.MasterModel.selectTool("drawTriangle")
#         
#     def KeyF7Handler(self):
#         self.MasterModel.selectTool("drawPolygon")
# 
#     def KeyF8Handler(self):
#         self.MasterModel.selectTool("selectClear")
# 
#     def KeyTabHandler(self):
#         self.VisualizerOperator.changeDisplay()
# =============================================================================
