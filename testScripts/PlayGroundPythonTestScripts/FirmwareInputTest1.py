# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:00:06 2023

@author: Derek Joslin

"""

from DisplaySerial import *
import time

comPort = DisplaySerial("COM3", 57600, 3)

prev_button_values = [0, 0, 0, 0]
prev_analog_values = [0, 0, 0, 0]

def is_change_greater_than_10_percent(old_value, new_value):
    if old_value == 0:
        return True
    return abs((new_value - old_value) / old_value) > 30

while 1:
    time.sleep(0.001)
    button_changed = False
    analog_changed = False

    button_values = comPort.readButtonMatrix()
    for i, button_value in enumerate(button_values):
        if prev_button_values[i] != button_value:
            button_changed = True
            prev_button_values[i] = button_value
            for j in range(0,4):
                binary_string = bin(button_values[j])[2:].zfill(8)  # convert to binary and pad with leading zeros
                print("Button Value ({}): {}".format(j, binary_string))
            analog_values = comPort.readAnalog()
            print("Joy Stick x: {}".format(analog_values[3]))
            print("Joy Stick y: {}".format(analog_values[2]))
            print("Potentiometer: {}".format(analog_values[1]))
            print("Pressure: {}".format(analog_values[0]))


# =============================================================================
#     analog_values = comPort.readAnalog()
#     for i, analog_value in enumerate(analog_values):
#         if is_change_greater_than_10_percent(prev_analog_values[i], analog_value):
#             analog_changed = True
#             prev_analog_values[i] = analog_value
# 
#     if analog_changed:
#         print("Joy Stick x: {}".format(analog_values[3]))
#         print("Joy Stick y: {}".format(analog_values[2]))
#         print("Potentiometer: {}".format(analog_values[1]))
#         print("Pressure: {}".format(analog_values[0]))
# =============================================================================
