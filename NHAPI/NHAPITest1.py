# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:58:44 2023

@author: Derek Joslin

"""


import NHAPI as nh


Display = nh.NHAPI("testDisplay")

Display.connect("COM14")


# draw line
Display.line((0,0),(19,82))

Display.stroke(4)
# draw triangle
Display.circle((10,60),6)

# set the desired to the edited
desiredState = Display.return_desiredState()

print("desired State")
Display.displayMatrix(desiredState)

Display.refresh()

# retrieve the current
Display.pull_currentState()
newMatrix = Display.return_currentState()

print("changed State")
Display.displayMatrix(newMatrix)