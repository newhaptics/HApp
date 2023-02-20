# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 16:15:59 2023

@author: Derek Joslin

"""

class TouchTunesModel:
    def __init__(self, nColumns, nRows):
        self.nColumns = nColumns
        self.nRows = nRows
        self.barIndex = 0
        self.bars = [self.nColumns for i in range(self.nRows)]

    def setBarLength(self, newLength):
        if self.barIndex >= 0 and self.barIndex < self.nColumns:
            self.bars[barIndex] = newLength
            
    def selectBar(self, newBarIndex):
        if newBarIndex >= 0 and self.newBarIndex < self.nRows:
            self.barIndex = newBarIndex
            
    def getBarLength(self, barIndex):
        return self.bars[barIndex]
