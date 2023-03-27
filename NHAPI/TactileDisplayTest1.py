# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:43:52 2023

@author: Derek Joslin

"""


import TactileDisplay as td

Display = td.TactileDisplay("testDisplay")
Display.comLink_on("COM3")

# get the intial matrix
testMatrix = Display.return_desiredState()

print("test Matrix")
Display.display_matrix(testMatrix)

# edit the matrix
testMatrix[0][0] = 1
testMatrix[1][1] = 1
testMatrix[2][2] = 1
testMatrix[3][3] = 1

# set the desired to the edited
Display.set_desiredState(testMatrix)
desiredState = Display.return_desiredState()

print("desired State")
Display.display_matrix(desiredState)

# push the desired into current
Display.push_desiredState()
currentState = Display.return_currentState()

print("current State")
Display.display_matrix(currentState)

# retrieve the current
Display.pull_currentState()
newMatrix = Display.return_currentState()

print("changed State")
Display.display_matrix(newMatrix)
