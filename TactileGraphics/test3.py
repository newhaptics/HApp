# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:52:23 2023

@author: derek
"""

from serial import Serial

import time

comPort = Serial("COM21", 115200, timeout=3)

trigger_value = 218
specified_value = 0x91  # 100 in hexadecimal

currentTime = time.perf_counter_ns()
elapsedTime = time.perf_counter_ns()


while True:
        # Poll the serial port for the trigger value
        if comPort.read(1)[0] == trigger_value:
            
            # Once the trigger value is found, read the next 63 values
            debugData = comPort.read(62)
            
            debugDataIntegers = [b for b in debugData]
            debugDataHex = [hex(b) for b in debugData]
            
            print(debugDataIntegers[23])
            elapsedTime = time.perf_counter() - currentTime
            print(elapsedTime)
            currentTime = time.perf_counter()
            if specified_value in debugDataIntegers:
                index_of_value = debugDataIntegers.index(specified_value)
                print(f"Found at index {index_of_value}")
                break
            # print(comPort.in_waiting)

            # print(debugDataHex)
            # print("\n"*40)
