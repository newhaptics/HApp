# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:21:03 2023

@author: Derek Joslin

"""

import Imprint as im
#import VoiceSynthesizer as vs
import HapticsEngine as he
import RomLauncher as rl

class LLMOS(im.Imprint):

    def __init__(self, openAIKey, elevenLabsKey):
        # create the imprint of llmOS
        super().__init__(openAIKey, "C://Users//derek//Documents//HApp//HAppKernal//gnomes//LLMOS.gnome")

        # create the control center for llmOS resources
        self.HapticsEngine = he.HapticsEngine()
        
        self.PeripheralManager = self.HapticsEngine.PeripheralManager
        self.FileManager = self.HapticsEngine.FileManager

        # create the cave johnson voice
        #self.Voice = vs.VoiceSynthesizer(elevenLabsKey)

        # create the RomLauncher
        self.romDictionary = self.FileManager.createRomDirectory()
        self.RomLauncher = rl.RomLauncher(self.HapticsEngine, self.romDictionary)
        
        self.openGnome("StartRom")
        
    def addMainWindow(self, MainWindow):
        # pass in the MainWindow and calculate the coordinates
        MainWindow.show()
        self.MainWindow = MainWindow
        
    def speakCommand(self, command):
        genericResponse = self.generateResponse(command)
        genericResponse = self.decodeResponse()
        
        tempgnome = self.gnome
        
        # turn the response into Cave Johnson
        self.openGnome("Cave Johnson")

        userString = "User-" + command
        AIString = "AI assistant-" + genericResponse[1]

        voiceResponse = self.generateResponse(userString + "\n" + AIString)

        print(voiceResponse)
        self.gnome = tempgnome
        self.Voice.synthVoice(voiceResponse)
        self.Voice.playSound()

        return genericResponse, voiceResponse

    def llmOSCommand(self, prompt):
        genericResponse,voiceResponse = self.speakCommand(prompt)

# =============================================================================
#         print(genericResponse)
#         print(voiceResponse)
# =============================================================================
        inputCommand = "RomControl {}".format(genericResponse[0])
        # only the Rom Control commands are available for now
        self.osDecider(inputCommand)

    def osDecider(self, instruction):
        # decide the class of command
        components = instruction.split(" ")
        
        
        if components[0] == "RomControl":
            # enact the commands for rom control
            self.RomControl(instruction)

        elif components[0] == "PeripheralManagement":
            # enact the commands for connecting peripherals
            self.PeripheralManagement(instruction)

        else:
            print("{0} instruction class not recognized".format(components[0]))

    def RomControl(self, instruction):
        components = instruction.split(" ")

        print(components)

        if "StartRom" == components[1]:
            # add the rom to the path
            romFile = self.romDictionary[components[2]]
            romFolder = romFile.split("//{}.rom".format(components[2]))
            print(romFolder)
            self.FileManager.addDirectory(romFolder[0])
            
            self.RomLauncher.startRom(components[2])
            # open the appropriate gnome
            self.openGnome("EndRom")

        elif "EndRom" == components[1]:
            print("llmos endRom")
            self.RomLauncher.endRom()
            
            # open the appropriate gnome
            self.openGnome("StartRom")
            
        else:
            print("{} is not a valid instruction".format(components[1]))

    def PeripheralManagement(self, instruction):

        components = instruction.split(" ")

        if "Connect" == components[1]:
            self.PeripheralManager.connectPeripheral(components[2], components[3], components[4:])
            
            if components[2] == "Display":
                self.MainWindow.renderDisplay(self.PeripheralManager.TactileDisplay)
                
                
            if components[2] == "Touchscreen":
                Touchscreen = self.HapticsEngine.getPeripheral(components[3])
                Touchscreen.touchAlgorithm = "center of mass"
                y = Touchscreen.nSensorRows - 1
                x = Touchscreen.nSensorColumns - 1
                self.HapticsEngine.addCoordinateSystem("Touchscreen", (x,y))
                print(self.HapticsEngine.CoordinateSystem.boundedRegions)
                
                # add the touchscreen to the TactileDisplayVisualizerRenderer
                displayRender = self.HapticsEngine.getOperation("TactileDisplayVisualizerRenderer")
                displayRender.addTouchscreen(Touchscreen)

        elif "Disconnect" == components[1]:
            self.PeripheralManager.disconnectPeripheral(components[2])

        else:
            print("{} is not a valid instruction".format(components[1]))


# =============================================================================
#     def connectTouchscreen(self, comString):
#         self.TactileDisplay.connectTouch("NewHaptics Touchscreen KausiaV1", comString)
#         
#         # get the dimensions of the display
#         state = self.TactileDisplay.state()
#         displaySize = self.TactileDisplay.size()
#         
#         if self.called == 0:
#             # Create the real time visualizer
#             self.TouchVisualizer = tsv.TouchVisualizer("TouchVisualizer", state, displaySize)
#             
#             # create an operation to constantly refresh the visualizer and add it to the controller
#             self.TouchVisualizerRefreshOperation = tsv.TouchVisualizerOperation("TouchVisualizerRefreshOperation", self.MousePeripheral, self.TactileDisplay, self.TouchVisualizer, self.margins)
#             
#             # Build a HApp keyboard
#             self.HAppKeyboardHandles = hk.HAppKeyboardHandles(self.TouchVisualizerRefreshOperation)
#             self.KeyboardPeripheral.setDefaultHandler(self.HAppKeyboardHandles)
#             
#             # Build a HApp mouse
#             self.HAppMouseHandles = hm.HAppMouseHandles(self.TouchVisualizerRefreshOperation)
#             self.MousePeripheral.setDefaultHandler(self.HAppMouseHandles)
#             
#             # remove the state visualizer
#             self.HAppControlCenter.killOperation("StateVisualizerRefreshOperation")
#             self.HAppControlCenter.removeVisualization("StateVisualizer")
#             
#             # add it as a visualization to the control center
#             self.HAppControlCenter.addVisualization(self.TouchVisualizer)
#             self.HAppControlCenter.addOperation(self.TouchVisualizerRefreshOperation)
#             
#             # set the mouse and keyboard handlers inside main window
#             self.TouchVisualizerKeyboardHandles = tsv.TouchVisualizerKeyboardHandles(self.HAppControlCenter)
#             self.TouchVisualizerMouseHandles = tsv.TouchVisualizerMouseHandles(self.HAppControlCenter)
#             
#             # assign the touchvisualizer keyboard handles
#             self.KeyboardPeripheral.setDefaultHandler(self.TouchVisualizerKeyboardHandles)
#             self.MousePeripheral.setDefaultHandler(self.TouchVisualizerMouseHandles)
#             
#             # update the ARCS status label
#             #self.ARCSLabel.setText(self.HAppControlCenter.debugPrintAllResources())
#             
#             self.setCentralWidget(self.TouchVisualizer)
#             self.called = 1
#         else:
#             # remove the state visualizer
#             self.HAppControlCenter.killOperation("TouchVisualizerRefreshOperation")
#             self.HAppControlCenter.removeVisualization("TouchVisualizer")
#             
#             # Build a HApp keyboard
#             self.HAppKeyboardHandles = hk.HAppKeyboardHandles(self.TouchVisualizerRefreshOperation)
#             self.KeyboardPeripheral.setDefaultHandler(self.HAppKeyboardHandles)
#             
#             # Build a HApp mouse
#             self.HAppMouseHandles = hm.HAppMouseHandles(self.TouchVisualizerRefreshOperation)
#             self.MousePeripheral.setDefaultHandler(self.HAppMouseHandles)
#             
#             # Create the real time visualizer
#             self.TouchVisualizer = tsv.TouchVisualizer("TouchVisualizer", state, displaySize)
#             
#             # create an operation to constantly refresh the visualizer and add it to the controller
#             self.TouchVisualizerRefreshOperation = tsv.TouchVisualizerOperation("TouchVisualizerRefreshOperation", self.MousePeripheral, self.TactileDisplay, self.TouchVisualizer, self.margins)
#             
#             # add it as a visualization to the control center
#             self.HAppControlCenter.addVisualization(self.TouchVisualizer)
#             self.HAppControlCenter.addOperation(self.TouchVisualizerRefreshOperation)
#             
#             # set the mouse and keyboard handlers inside main window
#             self.TouchVisualizerKeyboardHandles = tsv.TouchVisualizerKeyboardHandles(self.HAppControlCenter)
#             self.TouchVisualizerMouseHandles = tsv.TouchVisualizerMouseHandles(self.HAppControlCenter)
#             
#             # assign the touchvisualizer keyboard handles
#             self.KeyboardPeripheral.setDefaultHandler(self.TouchVisualizerKeyboardHandles)
#             self.MousePeripheral.setDefaultHandler(self.TouchVisualizerMouseHandles)
#             
#             # update the ARCS status label
#             #self.ARCSLabel.setText(self.HAppControlCenter.debugPrintAllResources())
#             
#             self.setCentralWidget(self.TouchVisualizer)
#     
# =============================================================================
