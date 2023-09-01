# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:16:59 2023

@author: Derek Joslin

"""

class PeripheralDevice:
    def __init__(self, name):
        self.name = name
        self.debugString = ""
    
    def connect(self):
        pass
    
    def disconnect(self):
        pass
    
    def getStatus(self):
        return self.debugString