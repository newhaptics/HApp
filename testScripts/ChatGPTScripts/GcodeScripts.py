# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:12:24 2023

@author: Derek Joslin

"""


import DisplaySerial as ds
import time
from TactileDisplayGcode import GCodeController

serial_port = ds.DisplaySerial("COM4", 57600, 3)
serial_port.getSize()
row_array = serial_port.getRowValveArray()
column_array = serial_port.getColumnValveArray()

# =============================================================================
# serial_port.setColumnValveArrayAssignment(column_array)
# serial_port.setRowValveArrayAssignment(row_array)
# =============================================================================

gcode_controller = GCodeController(serial_port)

# Set all column valves high sequentially
gcode_controller.process_gcode("c")
gcode_controller.process_gcode("r")
time.sleep(3)
gcode_controller.process_gcode("C")
time.sleep(3)
gcode_controller.process_gcode("R")
time.sleep(3)
gcode_controller.process_gcode("c")
time.sleep(3)
gcode_controller.process_gcode("r")

#print(gcode_controller.row_valve_state_array)
#print(gcode_controller.column_valve_state_array)

# make shift functionality test

# =============================================================================
# for i in range(len(column_array)):
#     gcode_controller.process_gcode(f"C[{i}:{i}]")
#     time.sleep(0.1)
# 
# # Set all row valves high
# gcode_controller.process_gcode("R")
# time.sleep(1)
# 
# # Set all column valves low
# gcode_controller.process_gcode("c")
# 
# # Set all row valves low sequentially
# for i in range(len(row_array)):
#     gcode_controller.process_gcode(f"r[{i}:{i}]")
#     time.sleep(0.1)
# 
# =============================================================================

