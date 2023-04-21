# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:21:03 2023

@author: Derek Joslin

"""

import Imprint as im
#import VoiceSynthesizer as vs
import HapticsEngine as he
import RomLauncher as rl
import CommandLine as cl

import KeyboardPeripheral as kb
#import HAppKeyboardHandles as hk
import DefaultKeyboardHandles as dk

import GraphicsRenderOperation as gro

import CommandLineKeyboardHandles as ck

from pynput import keyboard

class LLMOS(im.Imprint):

    def __init__(self, openAIKey, elevenLabsKey):
        # create the imprint of llmOS
        super().__init__(openAIKey, "C://Users//derek//Documents//HApp//HapticOS//gnomes//LLMOS.gnome")

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

        # Build a default keyboard
        self.currentHandler = dk.DefaultKeyboardHandles()
        self.KeyboardPeripheral = kb.KeyboardPeripheral("Master Keyboard", self.currentHandler)

        # add the Keyboard to the control center
        self.HapticsEngine.addPeripheral(self.KeyboardPeripheral)

        # add command window
        self.CommandLine = cl.CommandLine(self.HapticsEngine)

        # create input for command line
        self.CommandLineKeyboardHandles = ck.CommandLineKeyboardHandles(self.CommandLine)
        self.KeyboardPeripheral.setNewKeyboardHandler(self.CommandLineKeyboardHandles)

        # value to determine if in the command line mode
        self.commandLineMode = 1
        self.isDisplayConnected = 0

    def addMainWindow(self, MainWindow):
        # pass in the MainWindow and calculate the coordinates
        MainWindow.show()
        self.MainWindow = MainWindow


    def speakCommand(self, command):
        genericResponse = self.generateResponse(command)
        print(genericResponse)
        genericResponse = self.decodeResponse()
        print("llmos")

# =============================================================================
#         tempgnome = self.gnome
#
#         # turn the response into Cave Johnson
#         self.openGnome("Cave Johnson")
#
#         userString = "User-" + command
#         AIString = "AI assistant-" + genericResponse[1]
#
#         voiceResponse = self.generateResponse(userString + "\n" + AIString)
#
#         print(voiceResponse)
#         self.gnome = tempgnome
#         self.Voice.synthVoice(voiceResponse)
#         self.Voice.playSound()
# =============================================================================

        return genericResponse#, voiceResponse

    def llmOSCommand(self, prompt):
        genericResponse = self.speakCommand(prompt) #,voiceResponse

        inputCommand = "RomControl {}".format(genericResponse[0])
        # only the Rom Control commands are available for now
        self.osDecider(inputCommand)

    def osDecider(self, instruction):
        # decide the class of command
        print(instruction)
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
            self.commandLineMode = 0
            romFile = self.romDictionary[components[2]]
            romFolder = romFile.split("//{}.rom".format(components[2]))
            print(romFolder)
            self.FileManager.addDirectory(romFolder[0])

            self.RomLauncher.startRom(components[2])
            # open the appropriate gnome
            self.openGnome("EndRom")
            self.currentHandler = self.KeyboardPeripheral.KeyboardHandles

        elif "EndRom" == components[1]:
            print("llmos endRom")
            self.commandLineMode = 1
            self.RomLauncher.endRom()

            # open the appropriate gnome
            self.openGnome("StartRom")
            self.currentHandler = self.KeyboardPeripheral.KeyboardHandles

        else:
            print("{} is not a valid instruction".format(components[1]))

    def PeripheralManagement(self, instruction):

        components = instruction.split(" ")

        if "Connect" == components[1]:
            self.PeripheralManager.connectPeripheral(components[2], components[3], components[4:])

            if components[2] == "Display":
                self.MainWindow.renderDisplay(self.PeripheralManager.TactileDisplay)

                self.TactileDisplay = self.HapticsEngine.getPeripheral("Fourplex")
                self.isDisplayConnected = 1
                #displaySize = TactileDisplay.return_displaySize()
# =============================================================================
#                 self.Render = gro.GraphicsRenderOperation("Render", self.TactileDisplay)
#                 self.HapticsEngine.addOperation(self.Render)
# =============================================================================
                # add the commandline output to be set


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

    """ Keyboard related functions """

    def onPress(self, key):

        if key == keyboard.Key.ctrl_l:
            if not self.commandLineMode:
# =============================================================================
#                 print("command line mode off")
#                 self.commandLineMode = 0
#                 self.CommandLine.clear()
#                 self.KeyboardPeripheral.setNewKeyboardHandler(self.currentHandler)
#                 if self.isDisplayConnected:
#                     self.TactileDisplay.clear()
#                     self.TactileDisplay.refresh()
# =============================================================================
                print("command line mode on")
                self.RomLauncher.endRom()

                # open the appropriate gnome
                self.openGnome("StartRom")

                self.commandLineMode = 1
                self.KeyboardPeripheral.setNewKeyboardHandler(self.CommandLineKeyboardHandles)

        if self.commandLineMode:
            self.KeyboardPeripheral.handleKeyPressEvent(key)

            if key == keyboard.Key.tab:

                self.MainWindow.TactileDisplayVisualizerRenderer.changeDisplay()
                print("changing display")

            elif key == keyboard.Key.enter:

                prompt = self.MainWindow.commandBox.toPlainText()
                print(prompt)
                self.llmOSCommand(prompt)
                self.CommandLine.clear()

            elif key == keyboard.Key.f2:

                prompt = self.MainWindow.commandBox.toPlainText()
                print(prompt)
                self.osDecider(prompt)
                self.CommandLine.clear()

            outputText = self.CommandLine.editorMatrixOutput()
            print(outputText)
            self.HapticsEngine.commandText = outputText
            if self.isDisplayConnected:
                self.TactileDisplay.clear()
                self.TactileDisplay.braille((0,0), outputText)
                self.TactileDisplay.refresh()

        else:
            self.KeyboardPeripheral.handleKeyPressEvent(key)

        #self.MainWindow.commandBox.setText(outputText)
        #print(f"Key {key} pressed on device")

    def onRelease(self, key):

        self.KeyboardPeripheral.handleKeyReleaseEvent(key)
        #print(f"Key {key} released on device")

# =============================================================================
#     def keyPressEvent(self, key):
#         key.ignore()
#
#         if key() == qc.Qt.Key_F1:
#             prompt = self.commandBox.toPlainText()
#             print(prompt)
#             self.llmOSCommand(prompt)
#             self.commandBox.clear()
#
#         if event.key() == qc.Qt.Key_F2:
#             prompt = self.commandBox.toPlainText()
#             print(prompt)
#             self.HapticOS.osDecider(prompt)
#             self.commandBox.clear()
#
#         # Connect to KeyboardPeripheral class key press event
#         self.KeyboardPeripheral.handleKeyPressEvent(event)
# =============================================================================

    def keyReleaseEvent(self, event):
        event.ignore()

        # Connect to KeyboardPeripheral class key release event
        self.KeyboardPeripheral.handleKeyReleaseEvent(event)


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
