# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:29:04 2023

@author: derek
"""

import integratedTouchscreenPeripheral as itp
import TouchscreenPeripheral as tp
import time

Touchscreen1 = tp.TouchScreenPeripheral("test touch")
Touchscreen2 = tp.TouchScreenPeripheral("test touch")

Touchscreen1.connect("COM50")
Touchscreen2.connect("COM53")
#Touchscreen.serialPort.write(bytearray([1, 2, 3, 0, 2, 2, 1, 0, 3, 2, 1]))


while 1:
    Touchscreen1.writeDeltaCommand()
    Touchscreen2.getDeltaValues()
    time.sleep(0.01)
    Touchscreen2.writeDeltaCommand()
    Touchscreen1.getDeltaValues()
    
    Touchscreen1.printDeltaValues()
    Touchscreen2.printDeltaValues()

# =============================================================================
# Touchscreen = itp.IntegratedTouchscreenPeripheral("touch")
# 
# Touchscreen.connectNewTouchscreen("COM7")
# Touchscreen.connectNewTouchscreen("COM42")
# Touchscreen.connectNewTouchscreen("COM34")
# Touchscreen.connectNewTouchscreen("COM33")
# 
# Touchscreen.writeDeltaCommand()
# 
# Touchscreen.getDeltaValues()
# 
# Touchscreen.printTheDataMatrix()
# =============================================================================
