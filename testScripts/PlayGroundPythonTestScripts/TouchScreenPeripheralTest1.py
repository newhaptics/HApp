# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:45:40 2023

@author: Derek Joslin

"""

from PyQt5.QtWidgets import QApplication

import integratedTouchscreenPeripheral as itp
import time
# import serial.tools.list_portsq
import integratedTouchscreenVisualizer as itv
import sys

def generateTouchScreensList():
    # Get a list of available COM ports
    comports = "waw"

    # Check if any COM ports are available
    if not comports:
        print('No COM ports available')
        exit()

    Touchscreen = itp.IntegratedTouchscreenPeripheral("touch")

    Touchscreen.connectNewTouchscreen("COM35")
    #Touchscreen.connectNewTouchscreen("COM37")
# =============================================================================
#     Touchscreen.connectNewTouchscreen("COM51")
#     Touchscreen.connectNewTouchscreen("COM52")
# =============================================================================
    
    return Touchscreen

if __name__ == "__main__":
    Touchscreen = generateTouchScreensList()

# =============================================================================
#     while 1:
#         Touchscreen.writeDeltaCommand()
#         
#         Touchscreen.getDeltaValues()
#         
#         Touchscreen.printTheDataMatrix()
#         time.sleep(0.1)
# =============================================================================
    app = QApplication(sys.argv)

    Visualizer = itv.IntegratedTouchscreenVisualizer("wow vis", Touchscreen)
    Visualizer.show()
    
    sys.exit(app.exec())
