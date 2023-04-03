# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:17:50 2022

@author: Derek Joslin

"""

import SlidesToolSelector as sts
import SlidesOperations as so
import SlidesMouse as sm
import SlidesKeyboard as sk
import SlidesCanvasNav as scn
import SlidesFileManagement as sfm

class SlidesMaster():

    def __init__(self, Controller):
        #contains all classes required to run a slides rom

        self.Controller = Controller

        self.TactileDisplay = self.Controller.HAppControlCenter.getPeripheral("Fourplex")
        self.displaySize = self.TactileDisplay.return_displaySize()

        # create a cursor
        self.cursor = [0,0]

        # create the ability to navigate and load slides
        self.FileManager = sfm.SlidesFileManagement(self.Controller.HAppControlCenter.FileManager)

        # Create the tool flag
        self.ToolFlag = so.ToolFlag("ToolFlag")
        self.Controller.HAppControlCenter.addFlag(self.ToolFlag)

        # Create the state flag
        self.DisplayFlag = so.DisplayFlag("DisplayFlag")
        self.Controller.HAppControlCenter.addFlag(self.DisplayFlag)

        # Create main operations
        self.ToolExecuterOperation = so.ToolExecutionOperation("ToolExecuterOperation", self.TactileDisplay, self.ToolFlag)
        self.Controller.HAppControlCenter.addOperation(self.ToolExecuterOperation)

        # Operation for opening and loading slides
        self.SlideOperation = so.LoadSlideOperation("SlideOperation", self.TactileDisplay, self.DisplayFlag)
        self.Controller.HAppControlCenter.addOperation(self.SlideOperation)

        #Create the handlers
        self.MouseHandles = sm.SlidesMouseHandles(self)
        self.KeyboardHandles = sk.SlidesKeyboardHandles(self)

        # initialize the super class with the toolKeyList and the toolParameterDictionary

        # Implement the panning feature for loading the csv
        self.CanvasNavigation = scn.SlidesCanvasNav((self.displaySize[0],self.displaySize[1]))

        # slide data storage
        self.nSlides = 0
        self.currentSlide = 0
        self.slidesDictionary = {}

        self.isTouchConnected = 0

    def touchscreenStartUp(self):
        # get the touchscreen
        self.Touchscreen = self.Controller.HAppControlCenter.getPeripheral("Touchscreen")

        self.TouchFlag = so.TouchFlag("TouchFlag")
        self.Controller.HAppControlCenter.addFlag(self.TouchFlag)

        # get the coordinate system
        self.CoordinateSystem = self.Controller.HAppControlCenter.CoordinateSystem
        self.isTouchConnected = 1

    def selectTool(self, toolKey):
        # clear all options on the tool
        self.ToolFlag.clearState()
        # set the state of the flag to the currently selected tool
        self.ToolFlag.setState(toolKey)

    def parameterClicked(self, parameter):
        # add the parameter to the Tool Flag
        if self.ToolFlag.state:
            self.ToolFlag.addParameter(parameter)
        else:
            print("no tool selected")

    def executeTool(self, selectedTool, parameterKwargs):
        print("{} has been executed with {}".format(selectedTool, parameterKwargs))

        # temporary function to make a tool operation with appropriate parameters and execute in the kernal

    def updateViewSpace(self):
        testMatrix = self.CanvasNavigation.extractViewSpace()

        self.DisplayFlag.setState(1)
        self.DisplayFlag.setMatrix(testMatrix)

    def beginAutoExecuteParameters(self):
        # launch the operation
        self.AutoExecuteParameterOperation = so.AutoExecuteParameterOperation("AutoExecuteParameterOperation", self, self.TouchFlag)
        self.Controller.HAppControlCenter.addOperation(self.AutoExecuteParameterOperation)

    def endAutoExecuteParameters(self):
        # launch the operation
        self.Controller.HAppControlCenter.killOperation(self.AutoExecuteParameterOperation)
        self.Controller.HAppControlCenter.removeOperation("AutoExecuteParameterOperation")

    def getTouchPoints(self):
        # get the touchpoints for the touchscreen
        touchPoints = self.Touchscreen.findTouchPoints()

        # convert to tactile coordinates
        pinPointList = []
        for touchPoint in touchPoints:
            if touchPoint[0] == -1:
                pass
            else:
                #print(touchPoint)
                scaledDict = self.CoordinateSystem.scale(touchPoint[1],touchPoint[0],"Touchscreen")
                
                xTouchPin = int(scaledDict["TactileDisplay"][0])
                yTouchPin = int(scaledDict["TactileDisplay"][1])
                
                touchPinPoint = (xTouchPin,yTouchPin)
                
                pinPointList.append(touchPinPoint)

        self.TouchFlag.state = pinPointList

    def registerTouchParameters(self):
        # get the touch points
        pinPointList = self.TouchFlag.state
        for pinPoint in pinPointList:
            self.parameterClicked((pinPoint[1], pinPoint[0]))

    def loadNextSlide(self):
        if self.currentSlide < self.nSlides:
            self.currentSlide += 1
            self.loadSlide(self.currentSlide)
        else:
            self.loadSlide(1)

    def loadPreviousSlide(self):
        if self.currentSlide > 1:
            self.currentSlide -= 1
            self.loadSlide(self.currentSlide)
        else:
            self.loadSlide(self.nSlides - 1)

    def loadSlide(self, slideNum):
        # grab a slide.csv from the cwd
        try:
            self.currentSlide = slideNum
            slideString = "Slide {}".format(slideNum)
            print(slideString)

            #print(self.currentSlide)
            canvas = self.FileManager.openSlide(slideString)

            # set the current canvas to the new slide
            self.CanvasNavigation.setCanvas(canvas)

            # update the braille display with the new canvas
            self.updateViewSpace()

        except Exception as e:
            print(e)
