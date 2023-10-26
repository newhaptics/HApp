# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:19:51 2023

@author: derek
"""

from serial import Serial

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


def syncTouch():
    while True:
        # pass bytes until a 173 is read
        while comPort.read(1)[0] != frameStartByte1:
            pass
        if comPort.read(1)[0] == frameStartByte2:
            comPort.read(60)
            if comPort.read(1)[0] == frameEndByte:
                break
            
            
def gestureRecieved():
    if gestureId in gestureDictionary.keys():
        gesture = gestureDictionary[gestureId]
        syncTouch()
        print(gesture)
        

syncTouch()
print("uart frame synced")


# implement as an interrupted based system
while True:
    try:
        # Once the trigger value is found, read the next 63 values
        debugData = comPort.read(63)

        debugDataIntegers = [b for b in debugData]
        
        gestureId = debugDataIntegers[10]

        if gestureId in gestureDictionary.keys():
            gesture = gestureDictionary[gestureId]
            syncTouch()
            print(gesture)
            
        
        
    except Exception as e:
        print(f"An error occurred: {e}")