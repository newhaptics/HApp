# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:19:51 2023

@author: derek
"""

from TactileDisplay import TactileDisplay
from serial import Serial

Display = TactileDisplay("touchScreen")
Display.connect("COM50")

# =============================================================================
# comPort = Serial("COM50", 115200, timeout=3)
# =============================================================================

while 1:
    try:
        gesture = Display.detectTouchGesture()
        print(gesture)
# =============================================================================
#         gesture = int.from_bytes(gesture, byteorder='big', signed=False)
#         print(gesture)
#         if gesture == 0x01:
#             print("tap") 
# =============================================================================
    except:
        pass

