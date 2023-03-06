# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:45:40 2023

@author: Derek Joslin

"""

from PyQt5.QtWidgets import QApplication

import integratedTouchscreenPeripheral as itp
import time
#import serial.tools.list_portsq
import integratedTouchscreenVisualizer as itv
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

if __name__ == "__main__":
    Touchscreen = generateTouchScreensList()
    app = QApplication(sys.argv)

    Visualizer = itv.IntegratedTouchscreenVisualizer("wow vis", Touchscreen)
    Visualizer.show()
    
    sys.exit(app.exec())