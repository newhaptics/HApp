# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:47:56 2023

@author: Derek Joslin

"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QWidget, QGridLayout, QLabel
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc
import VisualizationManager as vm
import PyQt5.QtCore as qc
import numpy as np
from scipy import ndimage
import math

class IntegratedTouchscreenVisualizer(vm.Visualization):
    
    def __init__(self, name, IntegratedTouchscreen):
        super().__init__(name)
        self.touchPointList = []

        # assign the touch screen an object
        self.integratedTouchscreen = IntegratedTouchscreen
        
        # sets the title of the view window
        self.setWindowTitle("Integrated Touch Screen Window")
     
        # create the grid to the lay the touch values inside
        self.gridLayout = QGridLayout(self)
        #self.setStyleSheet("background: transparent;")
        # create the pyqt components
        self.sensorList = []
        
        # get window width and height to properly create layer 2
        self.pixWidth = self.width()
        self.pixHeight = self.height()
        
        print(self.pixWidth)
        print(self.pixHeight)
        
        # generate a grid layout of touch sensors the size of the touchscreen
        for iSensor in range(0, self.integratedTouchscreen.nSensors):
            sensor = QLabel()
            sensor.setStyleSheet("background: transparent;")
            sensor.setFixedSize(50,50)
            self.sensorList.append(sensor)
            sensor.setAlignment(qc.Qt.AlignCenter)
            self.gridLayout.addWidget(sensor, iSensor // self.integratedTouchscreen.nSensorColumns, iSensor % self.integratedTouchscreen.nSensorColumns)
        
        # create layer 2 dot layer
        self.touchOverlay = touchWindowView(self)
        self.touchOverlay.setGeometry(0,0,self.pixWidth*3, self.pixHeight)
        
        # Create a QTimer that calls collect_sensor_data() every 1000 ms
        self.timer = qc.QTimer(self)
        self.timer.timeout.connect(self.getDeltaValues)
        self.timer.start(1)
        
    def getDeltaValues(self):
        self.integratedTouchscreen.writeDeltaCommand()
        self.integratedTouchscreen.getDeltaValues()
        self.setSensorValues()
        
    def setSensorValues(self):
        iRow = 0
        iColumn = 0
        for i,sensor in enumerate(self.sensorList):            
            try:                
                if iRow == self.integratedTouchscreen.nSensorRows:
                    break
                #sensor.setText(sensorValues[i])
                sensorValue = self.integratedTouchscreen.integratedDataMatrix[iRow][iColumn]
                emptyPalette = qg.QPalette()
                emptyPalette.setColor(qg.QPalette.Window, qg.QColor("transparent"))
                
                sensor.setPalette(emptyPalette)

                sensor.setText('{}'.format(sensorValue))
                
                iColumn += 1
                if iColumn % self.integratedTouchscreen.nSensorColumns == 0:
                    iColumn = 0
                    iRow += 1
                    
            except Exception as e:
                print(e)
         
        #self.generateTouchPointList()
        self.generateRedDots()
                
        
    def generateRedDots(self):
        self.generateTouchPointList()
        
        # needs to be improved by creating a layer 2
        triggeredList = np.argwhere(self.integratedTouchscreen.integratedDataMatrix > 4)
        
        
        
        # create red dot for each point in center of mass
        for point in triggeredList:
            # get the Qlabel at the index
            redDot = self.gridLayout.itemAtPosition(int(point[0]),int(point[1]))
            redDot = redDot.widget()
            redDot.setStyleSheet("border: 5 px solid red")
            # Set the background color to red
            palette = qg.QPalette()
            palette.setColor(qg.QPalette.Background, qg.QColor("lightgray"))
            redDot.setAutoFillBackground(True)
            redDot.setPalette(palette)
        
    def generateTouchPointList(self):
        # get the center of mass of the integratedDataMatrix
        dataMatrix = self.integratedTouchscreen.integratedDataMatrix
        
        def lessThan(x):
            if x < 5:
                return 0
            else:
                return x
        
        dataMatrix = np.vectorize(lessThan)(dataMatrix)
        #print(dataMatrix)
        lbl = ndimage.label(dataMatrix)[0]
        rawTouchPointList= [(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)]
        for iCenterOfMass in range(0,10):
            rawTouchPointList[iCenterOfMass] = (ndimage.center_of_mass(dataMatrix, lbl, iCenterOfMass))
            #print(self.touchPointList[-1])
            
        # remove NaNs from list
        for iPoint,point in enumerate(rawTouchPointList):
            if np.isnan(point[0]):
                # get the current position 
                rawTouchPointList[iPoint] = (-1, -1)
        
        self.checkDistance(rawTouchPointList)#self.exponentialSmoothing(self.touchOverlay.touchPointList, rawTouchPointList, 0.7)
        #print(rawTouchPointList)
        #centerOfMass = ndimage.center_of_mass(dataMatrix)
        
        
    def checkDistance(self, newValueList):
        for i in range(0,10):
            oldValue = self.touchOverlay.touchPointList[i]
            newValue = newValueList[i]
            
            # use distance formula to find the distance
            distance = math.sqrt((newValue[0] - oldValue[0])**2 + (newValue[1] - oldValue[1])**2)
            
            if distance > 0.04:
                self.touchOverlay.touchPointList[i] = newValue

# =============================================================================
#     def lowPassFilter(self, newTouchPoints):
#         # remove the oldest set of points and add a new one
#         print(self.touchOverlay.touchPointHistory)
#         self.touchOverlay.touchPointHistory.pop()
#         self.touchOverlay.touchPointHistory.insert(0,newTouchPoints)
#         
#         meanElements = []
# 
#         for i in range(0,10):
#         
#             first_elements = [sub_list[i] for sub_list in self.touchOverlay.touchPointHistory]
#         
#             
#             meanElements.append(statistics.mean(first_elements))
#     
#         
#         return meanElements
# =============================================================================
    def exponentialSmoothing(self, currentDataList, filteredRawDataList, alpha):
        
# =============================================================================
#         # if new data is nothing just pop
#         for iPoint,point in enumerate(filteredRawDataList):
#             if point[0] == -1:
#                 # if the new data is empty then set to -1
#                 if len(currentDataList) > 0:
#                     try:
#                         currentDataList.pop(iPoint)
#                     except:
#                         pass
#             else:
#                 
#                 # if there is a value there 
#                 if len(currentDataList) > iPoint:
#                     pass
#                 
#                 # if no value exists add it
#                 else:
#                 
#                     currentDataList.append(filteredRawDataList[iPoint])
# =============================================================================
        shouldSmooth = False        


        for iPoint,point in enumerate(currentDataList):
            if point[0] == -1:
                # if the old data is empty then set to new data
                currentDataList[iPoint] = (filteredRawDataList[iPoint][0],filteredRawDataList[iPoint][1]) 


        

        # print an error if a -1 makes it through
        for iPoint,point in enumerate(currentDataList):
            if point[0] == -1:
                # if the new data is empty then set to -1
                pass
            else:
                shouldSmooth = True
                

        if shouldSmooth:
                
            currentDataMatrix = np.array(currentDataList)
            filteredRawDataMatrix = np.array(filteredRawDataList)
            
            # implement if -1 then just set to -1
            
            filteredDataMatrix = alpha * filteredRawDataMatrix + (1 - alpha) * currentDataMatrix
            filteredDataList = filteredDataMatrix.tolist()
            
        else:
            filteredDataList = currentDataList

        for iPoint,point in enumerate(filteredRawDataList):
            if point[0] == -1:
                # if the new data is empty then set to -1
                filteredDataList[iPoint] = (-1,-1) 
        
        
        
        return filteredDataList
    
        
class touchWindowView(QGraphicsView):
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # initialize settings for the graphics window
        self.setRenderHint(qg.QPainter.Antialiasing)        
        self.setInteractive(True)
        self.setStyleSheet("background: transparent;")
        
        # create the scene and set the view with it
        scene = QGraphicsScene(self)
        self.setScene(scene)
        
        # set the Overlay to be transparent so that it lays on top of the other window
        self.setAttribute(qc.Qt.WA_TranslucentBackground)
        
        # create the list of touch points
        self.touchPointList = [(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)]
        
# =============================================================================
#         self.touchPointHistory = []
#         for i in range(0,4):
#             self.touchPointHistory.append([(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1),(-1,-1)])
# =============================================================================

    def paintEvent(self, event):
        # paint the blueDots into the graphics view
        painter = qg.QPainter(self.viewport())
        painter.setRenderHint(qg.QPainter.Antialiasing)
        
        # clear the screen
        # fill the entire widget with a background color
        painter.eraseRect(self.rect())#, qg.QColor("white"))
        
        painter.setPen(qg.QPen(qc.Qt.red, 3))
        
        for point in self.touchPointList:
            newPoint = qc.QPointF(point[1]*57.75 + 10,point[0]*68 + 10)
            if point[0] != -1:
                painter.drawPoint(newPoint)
        
        painter.end()
        self.update()
        
        
        
        