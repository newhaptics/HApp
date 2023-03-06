# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:22:03 2023

@author: Derek Joslin

"""


import integratedTouchscreenPeripheral as itp
import time
#import serial.tools.list_portsq
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from findpeaks import findpeaks

import sys

def generateTouchScreensList():
    # Get a list of available COM ports
    comports = "waw"#list(serial.tools.list_ports.comports())

    # Check if any COM ports are available
    if not comports:
        print('No COM ports available')
        exit()

    Touchscreen = itp.IntegratedTouchscreenPeripheral("touch")

    print(comports)
    
    Touchscreen.connectNewTouchscreen("COM38")
    #Touchscreen.connectNewTouchscreen("COM7")
    #Touchscreen.connectNewTouchscreen("COM35")
    #Touchscreen.connectNewTouchscreen("COM36")
# =============================================================================
#     for connection in comports:
# 
#         # Connect to the first available COM port
#         port = connection.device
#         
#         Touchscreen.connectNewTouchscreen(port)
# =============================================================================

    return Touchscreen

def getDeltaValues(Touchscreen):
    Touchscreen.writeDeltaCommand()
    Touchscreen.getDeltaValues()
    
    
    
HistoricalData = np.array([])

fp = findpeaks(method='mask')

Touchscreen = generateTouchScreensList()
getDeltaValues(Touchscreen)
# create figure with subplots
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

interpolationResolution = (100, 100)

x = np.arange(interpolationResolution[0])#integratedTouchscreen.nSensorColumns)
y = np.arange(interpolationResolution[1])#integratedTouchscreen.nSensorRows)

Y, X = np.meshgrid(x,y)

Touchscreen.getInterpolation(interpolationResolution)

surf = ax.plot_surface(X,Y, Touchscreen.interpolatedDataMatrix, vmin=0, vmax=20, cmap=cm.tab10)

#plot = ax.plot_surface(X,Y, Touchscreen.interpolatedDataMatrix, vmin=0, vmax=20, cmap=cm.tab10)

# Add a color bar
fig.colorbar(surf, aspect=5)

ax.set_zlim(0, 20)

ax.view_init(azim=-20, elev=45)

def updateSurf(i):

    getDeltaValues(Touchscreen)
    #print(Touchscreen.integratedDataMatrix)
    
    Touchscreen.getInterpolation(interpolationResolution)
    
    #surf.set_array(data.ravel())
    
    ax.clear()
    surf = ax.plot_surface(X,Y, Touchscreen.interpolatedDataMatrix, vmin=0, vmax=20, cmap=cm.tab10)
    ax.set_box_aspect((1, 1, 0.5))
    ax.set_zlim(0, 20)

    
    #peakData = fp.fit(Touchscreen.interpolatedDataMatrix)
    
    #print(peakData["Xranked"])
    #peakPos = np.argwhere(peakData["Xranked"] == 1)#np.max(peakData["Xranked"])*0.99)

    
    #print(peakData["Xranked"])
    #print(peakPos)
    
    #plot = ax.scatter(peakPos[:,0],peakPos[:,1], 20, c="red")
    
    #self.ax.view_init(azim=-20, elev=45)
    
    #plt.draw()
# =============================================================================
#     fig.canvas.draw()
#     ax.figure.canvas.draw_idle()
# =============================================================================

    #return surf
    
if __name__ == "__main__":
    
    getDeltaValues(Touchscreen)
    
    ani = animation.FuncAnimation(fig, updateSurf, frames=200, interval=1)
    
    plt.show()
