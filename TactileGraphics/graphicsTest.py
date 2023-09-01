from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td

Display = td.TactileDisplay("testDisplay")
Display.connect("COM6")
Engine = GraphicsEngine((83, 19))

def refreshDisplay():
    Engine.drawFeatures()

    mat = Engine.retrieveList()
    # set the desired to the edited
    Display.set_desiredState(mat)
    # push the desired into current
    Display.push_desiredState()
   
def clearDisplay():
    Engine.clearFeatures()
    mat = Engine.retrieveList()
    # set the desired to the edited
    Display.set_desiredState(mat)
    # push the desired into current
    Display.push_desiredState()


if __name__ == "__main__":
    clearDisplay()
    Engine.addLine((0,0), (18,18), 3)
    refreshDisplay()

    ## above is the intializing code for the various objects necessary ##
    ## below is the scene scripting paradigm ##

    input("Scene 1 Intro to the Graphics Engine")
    clearDisplay()

    # Scene 1
    Engine.addBraille((0,0), "This is an intro to adding features using the graphics engine")

    refreshDisplay()

    input("Scene 2 Adding a Point to the display")
    clearDisplay()

    # Scene 2
    Engine.addPoint((0,0))

    refreshDisplay()

    input("Scene 3 Adding a Line to the display")
    clearDisplay()

    # Scene 3
    Engine.addLine((0,0), (82,18), 3)

    refreshDisplay()

    input("Scene 4 Adding a Triangle to the display")
    clearDisplay()

    # create the triangle vertices list
    triangleVertices = [(0,0), (50,18), (82,0)]

    # Scene 3
    Engine.addTriangle(triangleVertices, 4)

    refreshDisplay()

    input("Scene 5 Adding a Circle to the display")
    clearDisplay()

    # create the center point
    centerPoint = (30,10)

    # create the radius
    radius = 5

    # Scene 5
    Engine.addCircle(centerPoint, radius, 2)

    refreshDisplay()

    input("Scene 6 Adding a Rectangle to the display")
    clearDisplay()

    # Scene 3
    Engine.addRectangle((30,10), (70,18), 3)

    refreshDisplay()