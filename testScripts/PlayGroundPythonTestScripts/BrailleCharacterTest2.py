# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:49:04 2023

@author: Derek Joslin

"""


import serial

# Initialize serial port
ser = serial.Serial('COM7', baudrate=57600, timeout=0.1)


while True:
    try:
        print(ser.read(1))
    except:
        pass
# =============================================================================
#     if doWrite:
#         doWrite = 0    
#         ser.write(bytearray([1,2,3]))
#     if ser.in_waiting > 0:
#         print(ser.read(3))
#         doWrite = 1
# =============================================================================
