# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:40:31 2022

@author: Derek Joslin

"""


import RomAPI as rs

class SlidesKeyboardHandles(rs.RomKeyboardHandles):
    
    def __init__(self, MasterModel):
        super().__init__()
        self.MasterModel = MasterModel
       
        # get the tool flag
        self.ToolFlag = self.MasterModel.Controller.HAppControlCenter.getFlag("ToolFlag")
 
        # check if the touchscreen is attached or not
        VisualizerOperator = self.MasterModel.Controller.HAppControlCenter.getOperation("TouchVisualizerRefreshOperation")
        if VisualizerOperator is not None:
            self.VisualizerOperator = VisualizerOperator
        else:
            print("no touch screen attached")
            
        VisualizerOperator = self.MasterModel.Controller.HAppControlCenter.getOperation("StateVisualizerRefreshOperation")
        if VisualizerOperator is not None:
            self.VisualizerOperator = VisualizerOperator
        else:
            print("no device attached")

    def KeyLeftHandler(self):
        # perform cursor movement left
        self.MasterModel.CanvasNavigation.moveLeft()
        self.MasterModel.updateViewSpace()

    def KeyUpHandler(self):
        # perform cursor movement up
        self.MasterModel.CanvasNavigation.moveUp()
        self.MasterModel.updateViewSpace()

    def KeyRightHandler(self):
        # perform cursor movement right
        self.MasterModel.CanvasNavigation.moveRight()
        self.MasterModel.updateViewSpace()

    def KeyDownHandler(self):
        # perform cursor movement down
        self.MasterModel.CanvasNavigation.moveDown()
        self.MasterModel.updateViewSpace()

    def KeyWHandler(self):
        # move the cursor around
        if self.MasterModel.cursor[0] > 0:
            self.MasterModel.cursor[0] -= 1
            print("current cursor position {}".format(self.MasterModel.cursor))
        else:
            print("hit the bottom edge of screen")

    def KeyAHandler(self):
        if self.MasterModel.cursor[1] > 0:
            self.MasterModel.cursor[1] -= 1
            print("current cursor position {}".format(self.MasterModel.cursor))
        else:
            print("hit the left edge of screen")

    def KeySHandler(self):
        if self.MasterModel.cursor[0] < self.MasterModel.displaySize[0]:
            self.MasterModel.cursor[0] += 1
            print("current cursor position {}".format(self.MasterModel.cursor))
        else:
            print("hit the top edge of screen")

    def KeyDHandler(self):
        if self.MasterModel.cursor[1] < self.MasterModel.displaySize[1]:
            self.MasterModel.cursor[1] += 1
            print("current cursor position {}".format(self.MasterModel.cursor))
        else:
            print("hit the right edge of screen")

    def KeySpaceHandler(self):
        # Space bar event for visualizer operator
        # self.VisualizerOperator.clickSelect(xCoordinate, yCoordinate)
        pass
# =============================================================================
#         pinSelected = self.VisualizerOperator.getPinPosition()
#         print(pinSelected)
#         self.MasterModel.parameterClicked([int(pinSelected[1]), int(pinSelected[0])])
# =============================================================================
        
    def Key1Handler(self):
        self.MasterModel.selectTool("drawDot")

    def Key2Handler(self):
        self.MasterModel.selectTool("drawLine")

    def Key3Handler(self):
        self.MasterModel.selectTool("drawCurve")

    def Key5Handler(self):
        self.MasterModel.selectTool("drawRectangle")

    def Key6Handler(self):
        self.MasterModel.selectTool("drawTriangle")

    def Key7Handler(self):
        self.MasterModel.selectTool("drawPolygon")

    def Key8Handler(self):
        self.MasterModel.selectTool("selectClear")

    def KeyTabHandler(self):
        self.VisualizerOperator.changeDisplay()

    def KeyPageUpHandler(self):
        self.MasterModel.loadNextSlide()

    def KeyPageDownHandler(self):
        self.MasterModel.loadPreviousSlide()

    def KeyF6Handler(self):
        # decrease stroke
        oldStroke = self.MasterModel.TactileDisplay.width
        if oldStroke > 1:
            self.MasterModel.TactileDisplay.stroke(oldStroke - 1)
            print("stroke decreased to {}".format(oldStroke - 1))
        
    def KeyF7Handler(self):
        # increase stroke
        oldStroke = self.MasterModel.TactileDisplay.width
        self.MasterModel.TactileDisplay.stroke(oldStroke + 1)
        print("stroke increased to {}".format(oldStroke + 1))

    def KeyCapsLockHandler(self):
        #if self.MasterModel.isTouchConnected:
        if self.ToolFlag.autoExecute:
            print("auto execute off")
            self.ToolFlag.autoExecute = 0
            self.MasterModel.endAutoExecuteParameters()
        else:
            print("auto execute on")
            self.ToolFlag.autoExecute = 1
            self.MasterModel.beginAutoExecuteParameters()

    def Key0Handler(self):
        #if self.MasterModel.isTouchConnected:
        if self.ToolFlag.autoClear:
            print("auto clear off")
            self.ToolFlag.autoClear = 0
        else:
            print("auto clear on")
            self.ToolFlag.autoClear = 1

    def KeyShiftHandler(self):
        # get the current cursor position
        if self.MasterModel.isTouchConnected:
            print("registering touch")
            self.MasterModel.getTouchPoints()
            self.MasterModel.registerTouchParameters()
        else:
            # use generic cursor
            self.MasterModel.cursorClicked()