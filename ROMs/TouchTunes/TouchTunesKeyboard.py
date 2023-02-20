# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:02:58 2023

@author: Derek Joslin

"""


import DefaultKeyboardHandles as dh

class TouchTunesKeyboardHandles(dh.DefaultKeyboardHandles):
    
    
    def __init__(self, TouchTunesModel, TunesFlag):
        # add the model to the keyboards
        self.TouchTunesModel = TouchTunesModel
        
        # flag for Touch Tunes
        self.TunesFlag = TunesFlag
        
        # keep track of selected bar
        self.barSelectedIndex = 0
        
    
    def KeyUpHandler(self):
        if self.barSelectedIndex < self.TouchTunesModel.nRows:
            self.barSelectedIndex += 1
        
        self.TunesFlag.setState(1)
        
    def KeyDownHandler(self):
        if self.barSelectedIndex > 0:
            self.barSelectedIndex -= 1
        
        self.TunesFlag.setState(1)
        
    def KeyRightHandler(self):
        # select the bar get the current length and add one
        self.TouchTunesModel.selectBar(self.barSelectedIndex)
        
        length = self.TouchTunesModel.getBarLength()
        
        length += 1
        
        self.TouchTunesModel.setBarLength(length)
        
        self.TunesFlag.setState(1)
        
    def KeyLeftHandler(self):
        # select the bar get the current length and subtract one
        self.TouchTunesModel.selectBar(self.barSelectedIndex)
        
        length = self.TouchTunesModel.getBarLength()
        
        length -= 1
        
        self.TouchTunesModel.setBarLength(length)
        
        self.TunesFlag.setState(1)
        