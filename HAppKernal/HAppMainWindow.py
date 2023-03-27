# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:18:57 2022

@author: Derek Joslin

"""

from PyQt5 import QtWidgets as qw
from PyQt5 import QtGui as qg
from PyQt5 import QtCore as qc


import KeyboardPeripheral as kb
import HAppKeyboardHandles as hk
import DefaultKeyboardHandles as dk

import MousePeripheral as mh
import HAppMouseHandles as hm
import DefaultMouseHandles as dm

import RomVisualizationHandler as rh
import DefaultRomVisualizationHandles as drvh

import TouchStateVisualizer as tsv
import RealTimeStateVisualizer as rtsv

import HapticsEngine as he
import RomOperation as ro

import RomVisualization as rv


import LLMOS as llm

import RomLauncher as rl

""" HApp MainWindow """

class HAppMainWindow(qw.QMainWindow):

    """ intialization functions """

    def __init__(self, HapticOS, parent = None):
        
        self.flashSplash()
        super().__init__(parent)
        
        # create the llmOS
        self.HapticOS = HapticOS
        self.HapticOS.addMainWindow(self)

        self.HapticsEngine = self.HapticOS.HapticsEngine

        # create a dock widget to communicate with Cave
        self.commandBox = qw.QTextEdit()
        self.commandDock = qw.QDockWidget("llmOS Commands", self, qc.Qt.Widget)
        self.commandDock.setWidget(self.commandBox)
        self.addDockWidget(qc.Qt.LeftDockWidgetArea, self.commandDock, qc.Qt.Vertical)
        
        # set the mouse cursor to always be tracked
        self.setMouseTracking(True)
        self.setAttribute(qc.Qt.WA_TransparentForMouseEvents, True)
        
        # Set the cursor to be a red dot
        pixmap = qg.QPixmap(7.5, 7.5)
        pixmap.fill(qg.QColor(255, 0, 0))
        self.setCursor(qg.QCursor(pixmap))
        
        # get the margin for cursor tracking
        self.margins = self.layout().contentsMargins()
        
        # an extra widget
        self.ARCSLabel = qw.QLabel(self)
        
        self.ARCSDock = qw.QDockWidget("ARCS Monitor", self, qc.Qt.Widget)
        self.ARCSDock.setWidget(self.ARCSLabel)
        self.addDockWidget(qc.Qt.RightDockWidgetArea, self.ARCSDock, qc.Qt.Vertical)
        
        # display and define logo
        FCIcon = qg.QIcon(":main_symbol")
        HELogo = qg.QPixmap(":HE_logo")
        HELogo = HELogo.scaled(175,175, qc.Qt.KeepAspectRatio)
        
        # self.color = style
        self.setStyleSheet("border: 1px solid blue;")
        
        # Create window
        self.setWindowTitle("HApp Main Window")
        self.setWindowIcon(FCIcon)
        
        # Create status bar with the status and haptic engine
        self.statusBar = qw.QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Build a default keyboard
        self.DefaultKeyboardHandles = dk.DefaultKeyboardHandles()
        self.KeyboardPeripheral = kb.KeyboardPeripheral("Master Keyboard", self.DefaultKeyboardHandles)
        
        # add the Keyboard to the control center
        self.HapticsEngine.addPeripheral(self.KeyboardPeripheral)
        
        # Build a default mouse
        self.DefaultMouseHandles = dm.DefaultMouseHandles()
        self.MousePeripheral = mh.MousePeripheral("Master Mouse", self.DefaultMouseHandles)
        
        # add the Mouse to the control center
        self.HapticsEngine.addPeripheral(self.MousePeripheral)
        
# =============================================================================
#         # create window elements
#         self.__createActions()
#         self.__createMenuBar()
# =============================================================================
        
        # update the ARCS status label
        self.UpdateMonitorOperation = he.UpdateMonitorOperation("UpdateMonitorOperation", self.HapticsEngine, self.ARCSLabel)
        self.HapticsEngine.addOperation(self.UpdateMonitorOperation)
        
        # begin executing HApp operations
        self.HapticsEngine.startLaunchingOperations(2)
        
        qc.QTimer.singleShot(1000, lambda: self.quickConnect())
        
    def quickConnect(self):
        # ease of use
        self.HapticOS.osDecider("PeripheralManagement Connect Display Fourplex COM14")
        #self.HapticOS.osDecider("RomControl StartRom Notepad")
# =============================================================================
#         self.HapticOS.osDecider("RomControl EndRom Notepad")
#         self.HapticOS.osDecider("RomControl StartRom Avalanche")
#         self.HapticOS.osDecider("RomControl EndRom Avalanche")
# =============================================================================
        #ARCSLayout = self.HapticsEngine.debugGetResourceLabels()
        #self.ARCSLabel.setLayout(ARCSLayout)
        
    def flashSplash(self):
        FCLogo = qg.QPixmap(":main_logo")
        FCLogo = FCLogo.scaled(1000,1000)
        
        self.splash = qw.QSplashScreen(FCLogo)

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        qc.QTimer.singleShot(2000, self.splash.close)

    """ Keyboard related functions """

    def keyPressEvent(self, event):
        event.ignore()

        if event.key() == qc.Qt.Key_F1:
            prompt = self.commandBox.toPlainText()
            print(prompt)
            self.HapticOS.llmOSCommand(prompt)
            self.commandBox.clear()
            
        if event.key() == qc.Qt.Key_F2:
            prompt = self.commandBox.toPlainText()
            print(prompt)
            self.HapticOS.osDecider(prompt)
            self.commandBox.clear()

        # Connect to KeyboardPeripheral class key press event
        self.KeyboardPeripheral.handleKeyPressEvent(event)

    def keyReleaseEvent(self, event):
        event.ignore()
        
        # Connect to KeyboardPeripheral class key release event
        self.KeyboardPeripheral.handleKeyReleaseEvent(event)
        
    """ Mouse related functions """
    
    def mouseMoveEvent(self, event):
        event.ignore()
        
        # Handle mouse movements using the event handlers assigned to the peripheral
        self.MousePeripheral.handleMouseMoveEvent(event)

    def mousePressEvent(self, event):
        event.ignore()
        
        # Handle the mouse press event using the handlers in the peripheral
        self.MousePeripheral.handleMouseEvent(event)

    """ actions which can be performed when selecting options """

# =============================================================================
#     def __createActions(self):
#         self.saveDesired = qw.QAction("Save Desired State", self)
#         self.saveDesired.triggered.connect(lambda: self.FileManager.saveFile())
#         
#         self.load = qw.QAction("Load", self) #self.load.triggered.connect(lambda: self.__toolSelected("setMat","({matrix})"))
#         self.load.triggered.connect(lambda: self.FileManager.loadFile()) #self.load.triggered.connect(lambda: self.__optionUpdated("matrix", loadFile()))
#         
#         #control actions
#         self.clear = qw.QAction(eraseIcon, "Clear", self)
#         self.clear.triggered.connect(lambda: self.__toolSelected("clear","()"))
#         
#         self.Fclear = qw.QAction(FclearIcon, "Force clear", self)
#         self.Fclear.triggered.connect(lambda: self.__toolSelected("Fclear","()"))
#         
#         self.times = qw.QAction("Times", self)
#         self.times.triggered.connect(lambda: self.__toolSelected("times","({now})"))
#         
#         self.setMat = qw.QAction("Set Matrix", self)
#         self.setMat.triggered.connect(lambda: self.__toolSelected("setMat","({matrix})"))
# 
#         #board actions
#         self.connect = qw.QAction("Connect", self)
#         self.connect.triggered.connect(lambda: self.HapticOS.osDecider("Peripheral Management","({com})"))
#         
#         self.connectTouch = qw.QAction("Connect Touch", self)
#         self.connectTouch.triggered.connect(lambda: self.__toolSelected("connectTouch","({com})"))
#         self.disconnect = qw.QAction("Disconnect", self)
#         self.disconnect.triggered.connect(lambda: self.__toolSelected("disconnect","()"))
#         self.disconnectTouch = qw.QAction("Disconnect Touch", self)
#         self.disconnectTouch.triggered.connect(lambda: self.__toolSelected("disconnectTouch","()"))
# 
#         #help actions
#         self.settings = qw.QAction("Settings", self)
#         self.settings.triggered.connect(lambda: self.__toolSelected("settings","()"))
#         self.frames = qw.QAction("Frames", self)
#         self.frames.triggered.connect(lambda: self.__toolSelected("frames","()"))
# 
#         #misc actions
#         self.BoardIntializer = qw.QAction("Initialize Board", self)
#         self.BoardIntializer.triggered.connect(lambda: self.intializeBoard())
#         
#     """ menu related functions to loading roms """
#     
#     def __createMenuBar(self):
#         
#         menuBar = qw.QMenuBar(self)
#         self.setMenuBar(menuBar)
#         #create menu bars
#         #file menu
#         fileMenu = qw.QMenu("&File", self)
#         
#         #load and save actions
#         fileMenu.addAction(self.load)
#         
#         saveMenu = qw.QMenu("Save", self)
#         saveMenu.addAction(self.saveDesired)
#         
#         fileMenu.addMenu(saveMenu)
#         
#         #edit menu
#         editMenu = qw.QMenu("&Edit", self)
#         editMenu.addAction(self.clear)
#         editMenu.addAction(self.Fclear)
#         
#         #help menu
#         helpMenu = qw.QMenu("&Help", self)
#         helpMenu.addAction(self.settings)
#         
#         #control menu
#         controlMenu = qw.QMenu("Control",self)
#         controlMenu.addAction(self.refresh)
#         controlMenu.addAction(self.setMat)
#         
#         #board menu
#         boardMenu = qw.QMenu("Board", self)
#         
#         #create submenu for connect with dynamic com ports
#         self.DisplayConnectMenu = qw.QMenu("Connect Display", self)
#         self.TouchConnectMenu = qw.QMenu("Connect Touch", self)
#         self.called = 0
# =============================================================================
    
        #make a function to check the com ports create a list of com actions and add them to the connect Menu
        
    # TBD add a reworked peripheral connection gui
# =============================================================================
#     #get list of com ports
#     self.comList = cf.serial_ports()
#     
#     #delete existing actions
#     self.DisplayConnectMenu.clear()
#     self.TouchConnectMenu.clear()
#    
#     self.displayActionList = [displayConnector(self.comList[i], self) for i in range(len(self.comList))]
#     self.touchActionList = [touchConnector(self.comList[i], self) for i in range(len(self.comList))]
# 
#     for action in self.displayActionList:
#         self.DisplayConnectMenu.addAction(action)
#         
#     for action in self.touchActionList:
#         self.TouchConnectMenu.addAction(action)
#         
#         self.getCOMS = qw.QAction("getcoms",self)
#         self.getCOMS.triggered.connect(lambda: findComs())
#         boardMenu.aboutToShow.connect(findComs)
#     
#         print(self.DisplayConnectMenu.actions())
#         print(self.TouchConnectMenu.actions())
#         
#         boardMenu.addMenu(self.DisplayConnectMenu)
#         boardMenu.addMenu(self.TouchConnectMenu)
#     
#         boardMenu.addAction(self.disconnect)
#         boardMenu.addAction(self.disconnectTouch)
#         boardMenu.addAction(self.refresh)
#         boardMenu.addAction(self.BoardIntializer)
#     
#         # create submenu for direct
#         directMenu = qw.QMenu("Direct", self)
#         directMenu.addAction(self.directOff)
#         directMenu.addAction(self.directOn)
#     
#         boardMenu.addMenu(directMenu)
#     
#         # add menu bars
#         menuBar.addMenu(fileMenu)
#         menuBar.addMenu(editMenu)
#         menuBar.addMenu(helpMenu)
#         menuBar.addMenu(controlMenu)
#         menuBar.addMenu(boardMenu)
# =============================================================================

    """ connect the display and touch """
    def renderDisplay(self, TactileDisplay):
    
        
        # get the dimensions of the display
        state = TactileDisplay.return_currentState()
        displaySize = TactileDisplay.size()
        
        # Construction of visualization
        self.StateVisualizer = rtsv.StateVisualizer("StateVisualizer", state, displaySize)
        
        # Construction of Operation
        self.StateVisualizerRefreshOperation = rtsv.StateVisualizerOperation("StateVisualizerRefreshOperation",  self.MousePeripheral, TactileDisplay, self.StateVisualizer)
        
        # Reimplement Keyboard
        self.HAppKeyboardHandles = hk.HAppKeyboardHandles(self.StateVisualizerRefreshOperation)
        self.KeyboardPeripheral.setDefaultHandler(self.HAppKeyboardHandles)
        
        # Reimplement Mouse
        self.HAppMouseHandles = hm.HAppMouseHandles(self.StateVisualizerRefreshOperation)
        self.MousePeripheral.setDefaultHandler(self.HAppMouseHandles)
        
        # add it as a visualization to the control center
        self.HapticsEngine.addVisualization(self.StateVisualizer)
        self.HapticsEngine.addOperation(self.StateVisualizerRefreshOperation)
        
        # update the ARCS status label
        #self.ARCSLabel.setText(self.HapticsEngine.debugPrintAllResources())
        
        self.setCentralWidget(self.StateVisualizer)
    


# =============================================================================
#     """ connection subroutines """
#     
# 
# class displayConnector(qw.QAction):
#     
#     def __init__(self, comString, parent):
#         super().__init__(comString, parent)
#         self.MainWindow = parent
#         self.comString = comString
#         self.triggered.connect(self.connectDisplay)
#     
#     def connectDisplay(self):
#         # connects the tactile display and adds a real time visualization
# # =============================================================================
# #         # Create the real time visualizer
# #         ComString = self.comList[comIndex]
# # =============================================================================
#         print("disp com" + self.comString)
#         
#         self.MainWindow.connectDisplay(self.comString)
#         
#         
#     
# class touchConnector(qw.QAction):
# 
#     def __init__(self, comString, parent):
#         super().__init__(comString, parent)
#         self.MainWindow = parent
#         self.comString = comString
#         self.triggered.connect(self.connectTouchscreen)
#         
#     def connectTouchscreen(self):
#         # connects the touch screen and adds a touch visualization
#         print("touch com" + self.comString)
#         
#         self.MainWindow.connectTouchscreen(self.comString)
# =============================================================================
