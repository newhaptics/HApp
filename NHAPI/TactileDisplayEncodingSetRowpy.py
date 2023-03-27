# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:32:00 2023

@author: Derek Joslin

"""


import TactileDisplay as td

Display = td.TactileDisplay("testDisplay")
Display.comLink_on("COM14")

# get the intial matrix
testMatrix = Display.return_desiredState()

print("test Matrix")
Display.display_matrix(testMatrix)

# edit the matrix
testMatrix[0][0] = 1
testMatrix[1][1] = 1
testMatrix[2][2] = 1
testMatrix[3][3] = 1
testMatrix[4][4] = 1
testMatrix[5][5] = 1
testMatrix[6][6] = 1
testMatrix[7][7] = 1
testMatrix[8][8] = 1
testMatrix[9][9] = 1
testMatrix[10][10] = 1
testMatrix[11][11] = 1
testMatrix[12][12] = 1
testMatrix[13][13] = 1
testMatrix[14][14] = 1
testMatrix[15][15] = 1
testMatrix[16][16] = 1
testMatrix[17][17] = 1
testMatrix[18][18] = 1

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

