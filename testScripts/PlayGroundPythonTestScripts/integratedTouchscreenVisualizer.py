# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:47:56 2023

@author: Derek Joslin

"""

import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QWidget, QGridLayout, QLabel
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc
import VisualizationManager as vm
import time
import numpy as np
import math

class IntegratedTouchscreenVisualizer(vm.Visualization):
    
    def __init__(self, name, IntegratedTouchscreen):
        super().__init__(name)
        self.touchPointList = []
        
        # assign the touch screen an object
        self.integratedTouchscreen = IntegratedTouchscreen
        
        # use the center of mass algorithm
        self.integratedTouchscreen.touchAlgorithm = "center of mass"
        
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
        
        # create figure with subplots
        # create figure with subplots
# =============================================================================
#         self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
#         x = np.arange(100)#self.integratedTouchscreen.nSensorColumns)
#         y = np.arange(100)#self.integratedTouchscreen.nSensorRows)
#         
#         Y, X = np.meshgrid(x,y)
#         
#         self.data = np.random.rand(100,100)
#         
#         self.surf = self.ax.plot_surface(X,Y, self.data, vmin=0, vmax=20, cmap=cm.tab10)
#         
#         # Add a color bar
#         self.fig.colorbar(self.surf, aspect=5)
#         
#         self.ax.set_zlim(0, 20)
#         self.ax.view_init(azim=-20, elev=45)
# =============================================================================
        
        #self.ani = animation.FuncAnimation(self.fig, self.animate, interval=10)
        self.x = 0
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
        
# =============================================================================
#         # This function is called periodically from FuncAnimation
#     def animate(self):
#     
#         # Draw x and y lists
#         self.ax.clear()
#         x = np.arange(self.integratedTouchscreen.nSensorColumns)
#         y = np.arange(self.integratedTouchscreen.nSensorRows)
#         
#         X, Y = np.meshgrid(x,y)
#         
#         self.data = self.integratedTouchscreen.integratedDataMatrix
#         
#         self.surf = self.ax.plot_surface(X,Y, self.data, cmap=cm.coolwarm)
#         self.ax.set_zlim(0, 40)
#         self.ax.view_init(azim=5, elev=85)
# =============================================================================
        
        
    def getDeltaValues(self):
        self.integratedTouchscreen.writeDeltaCommand()
        time.sleep(0.05)
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

                sensor.setText('{}'.format(str(round(sensorValue, 2))))
                
                iColumn += 1
                if iColumn % self.integratedTouchscreen.nSensorColumns == 0:
                    iColumn = 0
                    iRow += 1
                    
            except Exception as e:
                print(e)
         
        self.generateRedDots()
# =============================================================================
#         if self.x > 1:
#             self.createSurf(self.integratedTouchscreen.interpolatedDataMatrix)
#             self.x = 0
#         self.x += 1
# =============================================================================
            
    def createSurf(self, data):
        # create figure with subplots
        self.fig, self.ax = plt.subplots(subplot_kw={"projection": "3d"})
        x = np.arange(100)#self.integratedTouchscreen.nSensorColumns)
        y = np.arange(100)#self.integratedTouchscreen.nSensorRows)
        
        Y, X = np.meshgrid(x,y)
        
        self.surf = self.ax.plot_surface(X,Y, data, vmin=0, vmax=20, cmap=cm.tab10)
        
        # Add a color bar
        self.fig.colorbar(self.surf, aspect=5)
        
        self.ax.set_zlim(0, 20)
        self.ax.view_init(azim=-20, elev=45)
        plt.show()
        
        
    def update_plot(self, new_data):
        # Update the data array
        self.data[:] = new_data
    
        # Update the surface plot
        self.surf.set_array(self.data.ravel())
        self.fig.canvas.draw()
        self.ax.figure.canvas.draw_idle()
# =============================================================================
#         x = np.arange(100)#self.integratedTouchscreen.nSensorColumns)
#         y = np.arange(100)#self.integratedTouchscreen.nSensorRows)
#         
#         Y, X = np.meshgrid(x,y)
#         
#         self.surf = self.ax.plot_surface(X,Y, self.data, vmin=0, vmax=20, cmap=cm.tab10)
#         plt.draw()
#         plt.show()
# =============================================================================

        
    def generateRedDots(self):
        # find the touch points from the integrated touch screen
        self.touchOverlay.touchPointList = self.integratedTouchscreen.findTouchPoints()
        
        # needs to be improved by creating a layer 2
        triggeredList = np.argwhere(self.integratedTouchscreen.integratedDataMatrix > 0)
        
        # create red dot for each point in center of mass
        for point in triggeredList:
            # get the Qlabel at the index
            redDot = self.gridLayout.itemAtPosition(int(point[0]),int(point[1]))
            sensorValue = self.integratedTouchscreen.integratedDataMatrix[int(point[0])][int(point[1])]
            colorValue = int(255 - 255*(sensorValue*6/255))
            if colorValue > 250:
                colorValue = 255
            #print(colorValue)
            redDot = redDot.widget()
            redDot.setStyleSheet("border: 5 px solid red")
            # Set the background color to red
            palette = qg.QPalette()
            palette.setColor(qg.QPalette.Background, qg.QColor(colorValue, colorValue, colorValue))
            redDot.setAutoFillBackground(True)
            redDot.setPalette(palette)
        
    def checkDistance(self, newValueList):
        for i in range(0,len(newValueList)):
            oldValue = self.touchOverlay.touchPointList[i]
            newValue = newValueList[i]
            
            # use distance formula to find the distance
            distance = math.sqrt((newValue[0] - oldValue[0])**2 + (newValue[1] - oldValue[1])**2)
            
            if distance > 0.04:
                self.touchOverlay.touchPointList[i] = newValue
        
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

    def paintEvent(self, event):
        # paint the blueDots into the graphics view
        painter = qg.QPainter(self.viewport())
        painter.setRenderHint(qg.QPainter.Antialiasing)
        
        # clear the screen
        # fill the entire widget with a background color
        painter.eraseRect(self.rect())#, qg.QColor("white"))
        
        painter.setPen(qg.QPen(qc.Qt.red, 5))
        
        for point in self.touchPointList:
            newPoint = qc.QPointF(point[1]*57.75 + 10,point[0]*68 + 10)
            if point[0] != -1:
                painter.drawPoint(newPoint)
        
        painter.end()
        self.update()
        
        
        
        