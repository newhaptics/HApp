# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:20:14 2023

@author: Derek Joslin

"""

from GraphicsEngine import *
import Features as f
import numpy as np

Engine = GraphicsEngine((41, 19))
#for i in range(0,5):
Engine.addBraille((0,3), "abcdefghijklmnopqrstuvwxyz")


Engine.drawFeatures()   
mat = Engine.retrieveList()
print("num: {}".format(0))
print('---------------------------\n')
print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
             for row in mat]))
print('---------------------------\n')


Engine.clearFeatures()

Engine.addBraille((0,0), "hello world")


Engine.drawFeatures()
mat = Engine.retrieveList()
print("num: {}".format(0))
print('---------------------------\n')
print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
             for row in mat]))
print('---------------------------\n')