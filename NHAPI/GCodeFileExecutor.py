# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:47:37 2023

@author: Derek Joslin

"""

import DisplaySerial as ds
import TactileDisplayGcode as gc

class GCodeFileExecutor:
    def __init__(self, gcode_controller):
        self.gcode_controller = gcode_controller

    def read_gcode_file(self, file_path):
        with open(file_path, 'r') as file:
            gcode_lines = file.readlines()
        
        return gcode_lines

    def execute_gcode_file(self, file_path):
        gcode_lines = self.read_gcode_file(file_path)
        print(gcode_lines)
        for line in gcode_lines:
            self.gcode_controller.process_gcode(line.strip())

# Usage example:
serial_port = ds.DisplaySerial("COM4", 57600, 3)
gcode_controller = gc.GCodeController(serial_port)
gcode_executor = GCodeFileExecutor(gcode_controller)
gcode_executor.execute_gcode_file("sample.gcode")