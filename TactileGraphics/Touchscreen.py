# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:33:26 2023

@author: Derek Joslin

"""

from serial import Serial
import threading
    

class Touchscreen():

    def __init__(self, comPortPin_):
        # Initialize the UART communication
        self.comPort = Serial(comPortPin_, 115200, timeout=3)

        self.frameStartByte1 = 173
        self.frameStartByte2 = 10
        self.frameEndByte = 218

        # touch gesture macros
        NO_GESTURE = 0x00

        SINGLE_TAP_GESTURE = 0x91
        DOUBLE_TAP_GESTURE = 0x92
        TRIPLE_TAP_GESTURE = 0x93

        RIGHT_SWIPE_GESTURE = 0x10
        LEFT_SWIPE_GESTURE = 0x20
        UP_SWIPE_GESTURE = 0x30
        DOWN_SWIPE_GESTURE = 0x40

        CW_WHEEL_GESTURE = 0xf0
        CCW_WHEEL_GESTURE = 0xf1

        self.gestureDictionary = {
            SINGLE_TAP_GESTURE: "single tap",
            DOUBLE_TAP_GESTURE: "double tap",
            TRIPLE_TAP_GESTURE: "triple tap",
            RIGHT_SWIPE_GESTURE: "right swipe",
            LEFT_SWIPE_GESTURE: "left swipe",
            UP_SWIPE_GESTURE: "up swipe",
            DOWN_SWIPE_GESTURE: "down swipe",
            CW_WHEEL_GESTURE: "cw wheel",
            CCW_WHEEL_GESTURE: "ccw wheel"
        }
        
    def gestureCallback(self, gesture):
        print(f"Gesture detected: {gesture}")

    def syncTouchscreen(self):
        while True:
            # pass bytes until a 173 is read
            while self.comPort.read(1)[0] != self.frameStartByte1:
                pass
            if self.comPort.read(1)[0] == self.frameStartByte2:
                self.comPort.read(60)
                if self.comPort.read(1)[0] == self.frameEndByte:
                    break
    
    def gestureRecieved(self,debugDataIntegers):
        gestureId = debugDataIntegers[10]
    
        if gestureId in self.gestureDictionary.keys():
            gesture = self.gestureDictionary[gestureId]
            self.syncTouchscreen()
            self.gestureCallback(gesture)
    
    def pollTouchscreenUart(self):
        self.syncTouchscreen()
        print("uart frame synced")
    
        while True:
            try:
                debugData = self.comPort.read(63)
                debugDataIntegers = [b for b in debugData]
                self.gestureRecieved(debugDataIntegers)
            except Exception as e:
                print(f"An error occurred: {e}")
                
    def beginTouchscreen(self):        
        # Start the UART thread
        touchscreenPollingThread = threading.Thread(target=self.pollTouchscreenUart)
        touchscreenPollingThread.start()