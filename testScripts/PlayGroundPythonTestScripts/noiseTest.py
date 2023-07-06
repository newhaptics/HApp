# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:20:45 2023

@author: Derek Joslin

"""


from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td
import time

Display = td.TactileDisplay("testDisplay")
Display.connect("COM6")
Engine = GraphicsEngine((83, 19))

def refreshDisplay():
    Engine.drawFeatures()

    mat = Engine.retrieveList()
    # set the desired to the edited
    Display.set_desiredState(mat)
    print("num: {}".format(0))
    print('---------------------------\n')
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                 for row in mat]))
    print('---------------------------\n')
    # push the desired into current
    Display.push_desiredState()
   
while 1:

        
    Engine.addBraille((0,0), "This is a very long list of words that is very long and it is testing the noise level of the display and it is really really long wow that is a long text.")
    
    refreshDisplay()
    time.sleep(2)
    
    Engine.clearFeatures()
    
    refreshDisplay()
    time.sleep(0.2)
