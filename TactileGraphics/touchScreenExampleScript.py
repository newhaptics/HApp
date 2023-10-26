# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:42:45 2023

@author: Derek Joslin

"""

from Touchscreen import Touchscreen


class myTouchscreen(Touchscreen):
    
    def gestureCallback(self, gesture):
        if gesture == "cw wheel":
            print("this is a clockwise wheel")
        print("wow this is a touch")

gestureScreen = myTouchscreen("COM50")

gestureScreen.beginTouchscreen()