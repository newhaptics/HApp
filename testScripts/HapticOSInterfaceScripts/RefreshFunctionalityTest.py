# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:42:53 2023

@author: Derek Joslin

"""


import DisplaySerial as ds
import time
from TactileDisplayGcode import GCodeController

serial_port = ds.DisplaySerial("COM4", 57600, 3)
serial_port.getSize()
row_array = serial_port.getRowValveArray()
column_array = serial_port.getColumnValveArray()

gcode_controller = GCodeController(serial_port)

pw = 0.2

# Set all column valves high sequentially
gcode_controller.process_gcode("c")
time.sleep(0.1)
gcode_controller.process_gcode("R")
time.sleep(0.1)

# =============================================================================
# for i in range(len(row_array)):
#     gcode_controller.process_gcode(f"C[{i}:{i}]")
#     time.sleep(pw)
#     #gcode_controller.process_gcode(f"R[{i}:{i}]")
# =============================================================================

gcode_controller.process_gcode("C")
# Set Clock in all the values sequentially
for i in range(len(row_array)):
    gcode_controller.process_gcode(f"r[{i}:{i}]")
    time.sleep(pw)
    gcode_controller.process_gcode(f"R[{i}:{i}]")
    
gcode_controller.process_gcode("c")

# Set Clock in all the values sequentially
for i in range(len(row_array)):
    gcode_controller.process_gcode(f"r[{i}:{i}]")
    time.sleep(pw)
    gcode_controller.process_gcode(f"R[{i}:{i}]")

# Set all row valves high
time.sleep(0.1)

