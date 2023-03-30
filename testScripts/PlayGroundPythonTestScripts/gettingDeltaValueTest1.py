# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:29:04 2023

@author: derek
"""

import integratedTouchscreenPeripheral as itp
import TouchscreenPeripheral as tp

Touchscreen = tp.TouchScreenPeripheral("test touch")

Touchscreen.connect("COM7")

while 1:
    Touchscreen.writeDeltaCommand()
    
    Touchscreen.getDeltaValues()
    
    Touchscreen.printDeltaValues()


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
