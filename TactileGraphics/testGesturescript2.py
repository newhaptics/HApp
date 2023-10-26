# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:29:12 2023

@author: derek
"""

from serial import Serial
import threading


# Initialize the UART communication
comPort = Serial("COM21", 115200, timeout=3)

frameStartByte1 = 173
frameStartByte2 = 10
frameEndByte = 218

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

gestureDictionary = {
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

def syncTouchscreen():
    while True:
        # pass bytes until a 173 is read
        while comPort.read(1)[0] != frameStartByte1:
            pass
        if comPort.read(1)[0] == frameStartByte2:
            comPort.read(60)
            if comPort.read(1)[0] == frameEndByte:
                break

def gestureCallback(gesture):
    print(f"Gesture detected: {gesture}")

def gestureRecieved(debugDataIntegers):
    gestureId = debugDataIntegers[10]

    if gestureId in gestureDictionary.keys():
        gesture = gestureDictionary[gestureId]
        syncTouchscreen()
        gestureCallback(gesture)

def pollTouchscreenUart():
    syncTouchscreen()
    print("uart frame synced")

    while True:
        try:
            debugData = comPort.read(63)
            debugDataIntegers = [b for b in debugData]
            gestureRecieved(debugDataIntegers)
        except Exception as e:
            print(f"An error occurred: {e}")


# Start the UART thread
touchscreenPollingThread = threading.Thread(target=pollTouchscreenUart)
touchscreenPollingThread.start()
