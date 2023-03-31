# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:44:29 2022

@author: Derek Joslin

"""

from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc

import VisualizationManager as vm

import OperationsManager as om

import qrc_resources

class TactileDisplayVisualizer(vm.Visualization):

    def __init__(self, name, displaySize, parent=None):

        super().__init__(name)

        # mouse tracking ability
        self.setMouseTracking(True)
        self.setAttribute(qc.Qt.WA_TransparentForMouseEvents, True)

        self.setStyleSheet("border: 1px dotted black;")
        self.uniformDot = True
        self.highlightPin = (0,0)
        self.dotSize = 20
        self.BrailleSize = 20
        self.setMouseTracking(True)
        # create display size and state stuff
        self.nRows = displaySize[0]
        self.nColumns = displaySize[1]
        self.blank = qg.QPixmap(":dot")
        self.blank = self.blank.scaled(qc.QSize(self.dotSize * 0.9,self.dotSize * 0.9))
        self.emptyPin = qg.QPixmap(":emptyPin")
        self.emptyPin = self.emptyPin.scaled(qc.QSize(self.dotSize * 0.9,self.dotSize * 0.9))
        self.filledPin = qg.QPixmap(":filledPin")
        self.filledPin = self.filledPin.scaled(qc.QSize(self.dotSize * 0.9,self.dotSize * 0.9))
        self.grid = qw.QGridLayout()
        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        self.pinList = []

        self.grid.setHorizontalSpacing(0)
        self.grid.setVerticalSpacing(0)
        for iRow in range(0,displaySize[0]):
            for iColumn in range(0,displaySize[1]):
                if ((iRow + 1) % self.BrailleSize == 0) or ((iColumn + 1) % 3 == 0) or self.uniformDot:
                    pinImage = qw.QLabel()
                    pinImage.setFixedSize(qc.QSize(self.dotSize,self.dotSize))
                    #pinImage.setPixmap(self.blank)
                    self.pinList.append(pinImage)
                    self.grid.addWidget(self.pinList[-1],iRow,iColumn)
                    self.grid.setRowStretch(iRow, 1)
                    self.grid.setColumnStretch(iColumn, 1)
                    self.grid.setColumnMinimumWidth(iColumn, 10)
                    self.grid.setRowMinimumHeight(iRow, 10)
                else:
                    pinImage = qw.QLabel()
                    pinImage.setPixmap(self.emptyPin)
                    self.pinList.append(pinImage)
                    self.grid.addWidget(self.pinList[-1],iRow,iColumn)
                    self.grid.setRowStretch(iRow, 1)
                    self.grid.setColumnStretch(iColumn, 1)
                    self.grid.setColumnMinimumWidth(iColumn, 10)
                    self.grid.setRowMinimumHeight(iRow, 10)

        self.setLayout(self.grid)
        #self.setGeometry(50,50,320,200)
        self.setWindowTitle("Real Time State Visualizer")

    def resizeOutput(self):
        #to be implemented in order to resize the display
        pass
        
    def refreshPins(self, state):
        self.state = state
        iPin = 0
        for iRow,rowList in enumerate(state):
            for iColumn,iElement in enumerate(rowList):
                if ((iRow + 1) % self.BrailleSize == 0) or ((iColumn + 1) % 3 == 0) and not self.uniformDot:
                    self.pinList[iPin].clear()
                else:
                    if not iElement:
                        self.pinList[iPin].setPixmap(self.emptyPin)
                    else:
                        self.pinList[iPin].setPixmap(self.filledPin)
                        
                if int(self.highlightPin[0]) == iColumn and int(self.highlightPin[1]) == iRow:
                    self.pinList[iPin].setPixmap(self.blank)
                    
                for point in self.touchPoints:
                    if int(point[1]) == iRow and int(point[0]) == iColumn:
                        self.pinList[iPin].setPixmap(self.blank)
                iPin += 1

    def getCoordinateSystem(self):
        return self.size()
    
    def addTouchOverlay(self):
        # create layer 2 dot layer\
        self.pixWidth = self.width()
        self.pixHeight = self.height()
        self.touchOverlay = touchWindowView(self)
        print(self.pixWidth)
        print(self.pixHeight)
        self.touchOverlay.setGeometry(0,0,self.pixWidth, self.pixHeight)
        self.touchOverlay.show()
        
        self.touchPoints = []
    
    def setTouchPoints(self, touchPoints):
        self.touchPoints = touchPoints
        
class touchWindowView(qw.QGraphicsView):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        self.StateVisualizer = parent
        
        # initialize settings for the graphics window
        self.setRenderHint(qg.QPainter.Antialiasing)        
        self.setInteractive(True)
        self.setStyleSheet("background: transparent;")
        
        # create the scene and set the view with it
        scene = qw.QGraphicsScene(self)
        self.setScene(scene)
        
        # set the Overlay to be transparent so that it lays on top of the other window
        self.setAttribute(qc.Qt.WA_TranslucentBackground)
        
        # create the list of touch points
        self.touchPointList = [(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)]

    def paintEvent(self, event):
        # paint the blueDots into the graphics view
        painter = qg.QPainter(self.viewport())
        painter.setRenderHint(qg.QPainter.Antialiasing)
        
        # clear the screen
        # fill the entire widget with a background color
        painter.eraseRect(self.rect())#, qg.QColor("white"))
        
        painter.setPen(qg.QPen(qc.Qt.black, 10))
        
        for point in self.touchPointList:
            newPoint = qc.QPointF(point[0], point[1])
            if point[0] != -1:
                painter.drawPoint(newPoint)
                    
        painter.end()
        self.update()

class TactileDisplayVisualizerRenderer(om.Operation):
    
    def __init__(self, name, MousePeripheral, TactileDisplay, CoordinateSystem, StateVisualizer):
        super().__init__(name)
        
        # inputs to the operation
        self.MousePeripheral = MousePeripheral
        self.inputDictionary[self.MousePeripheral.name] = self.MousePeripheral
        
        self.TactileDisplay = TactileDisplay
        self.inputDictionary[self.TactileDisplay.name] = self.TactileDisplay
        
        # outputs to the operation
        self.StateVisualizer = StateVisualizer
        self.outputDictionary[self.StateVisualizer.name] = self.StateVisualizer
        
        self.isTouch = 0
        self.CoordinateSystem = CoordinateSystem
        
        # provide a description
        self.description = "This operation collects the current state of the braille display from memory and updates the state visualizer with it."
        
        # execute the function continuously until otherwise
        executionParameters = {
            "executeDelay": 2500, # a delay in milliseconds that starts the execution of the Operation after the flag dependencies have been met
            "executeContinuously": True, # a boolean value that determines if the Operation will execute forever
            "executionIntervalTime": 1, # an interval in milliseconds that determines the time between execution
        }
        
        self.setExecutionParameters(executionParameters)
        
        self.executable = self.execute
        
        self.createDebugString()
        
        
    def addTouchscreen(self, Touchscreen):
        # add a touchscreen to the render
        self.Touchscreen = Touchscreen
        self.inputDictionary[self.Touchscreen.name] = self.Touchscreen
        self.isTouch = 1
# =============================================================================
#     def startOperation(self):
#         pass
#         # "Real GUI" Size
#         self.realGuiWidth =  829#self.StateVisualizer.frameGeometry().width() #- leftMargin*2#(self.dotSize + 1) * self.nColumns
#         self.realGuiHeight = 390#self.StateVisualizer.frameGeometry().height() #- topMargin*2#(self.dotSize + 1) * self.nRows
#     
#         pinWidth = 41
#         pinHeight = 19
#         
#         # create a coordinate scaler
#         regions = { "pin" : (pinWidth, pinHeight),
#                     "visualizer" : (self.realGuiWidth, self.realGuiHeight)
#                    }
#         
#         self.scaler = cs.CoordinateScaler(regions)
# =============================================================================
        
    def execute(self):
        # get the state from the firmware
        #state = self.TactileDisplay.state()
        state = self.TactileDisplay.return_currentState()
        
        # update the pin position 
        xCursorCoordinate = self.MousePeripheral.xCoordinate
        yCursorCoordinate = self.MousePeripheral.yCoordinate
        
        if xCursorCoordinate < 10:
            xCursorCoordinate = 0
        else:
            xCursorCoordinate -= 10
            
        if yCursorCoordinate < 10:
            yCursorCoordinate = 0
        else:
            yCursorCoordinate -= 10        # get the pin position from visualizer coordinate
        #scaledDict = self.scaler.scale(xCursorCoordinate, yCursorCoordinate, "visualizer")
        scaledDict = self.CoordinateSystem.scale(xCursorCoordinate, yCursorCoordinate, "TactileDisplayVisualizer")
        
        # get the pin coordinate to highlight
        xPinCoordinate = scaledDict["TactileDisplay"][0]
        yPinCoordinate = scaledDict["TactileDisplay"][1]
        
        self.StateVisualizer.highlightPin = (xPinCoordinate, yPinCoordinate)
        
        # if there is a touch screen render the touch cursor
        if self.isTouch:
            
            self.Touchscreen.writeDeltaCommand()
            self.Touchscreen.getDeltaValues()
            touchSensorList = self.Touchscreen.findTouchPoints()
            
            touchVisualizerList = []
            touchPinList = []
            for touchPoint in touchSensorList:
                if touchPoint[0] == -1:
                    #touchVisualizerList.append(touchPoint)
                    pass
                else:
                    # convert from a sensor block coordinate to TactileDisplayVisualizer coordinate
                    scaledDict = self.CoordinateSystem.scale(touchPoint[1], touchPoint[0], "Touchscreen")
                    
                    # get the pin coordinate to highlight
                    xTouchCoordinate = scaledDict["TactileDisplayVisualizer"][0] + 10
                    yTouchCoordinate = scaledDict["TactileDisplayVisualizer"][1] + 10
                    
                    touchVisualizerPoint = (xTouchCoordinate,yTouchCoordinate)
                    
                    touchVisualizerList.append(touchVisualizerPoint)
                    
                    xTouchPin = scaledDict["TactileDisplay"][0]
                    yTouchPin = scaledDict["TactileDisplay"][1]
                    
                    touchVisualizerPoint = (xTouchPin,yTouchPin)
                    touchPinList.append(touchVisualizerPoint)
            
            self.StateVisualizer.setTouchPoints(touchPinList)
            self.StateVisualizer.touchOverlay.touchPointList = touchVisualizerList#self.Touchscreen.findTouchPoints()
        
        #print(self.StateVisualizer.highlightPin)
        # refresh the visualizer state
        self.StateVisualizer.refreshPins(state)
        
    def changeDisplay(self):
        if self.StateVisualizer.BrailleSize == 4:
            self.StateVisualizer.BrailleSize = 5
        elif self.StateVisualizer.BrailleSize == 5:
            self.StateVisualizer.uniformDot = True
            self.StateVisualizer.BrailleSize = 20
        else:
            self.StateVisualizer.uniformDot = False
            self.StateVisualizer.BrailleSize = 4                