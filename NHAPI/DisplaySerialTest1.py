# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:55:05 2023

@author: Derek Joslin

"""

import DisplaySerial as ds
import time

serialPort = ds.DisplaySerial("COM4", 57600, 3)
serialPort.getSize()
rowArray = serialPort.getRowValveArray()
columnArray = serialPort.getColumnValveArray()

serialPort.setColumnValveArrayAssignment(columnArray)
serialPort.setRowValveArrayAssignment(rowArray)
print(serialPort.getColumnValveArray())
print(serialPort.getRowValveArray())

def stateArrayToBytearray(state_array):
    bit_string = ''.join(map(str, state_array))
    num_full_bytes = len(bit_string) // 8
    num_remaining_bits = len(bit_string) % 8
    
    bytearray_result = bytearray(int(bit_string[i:i+8], 2) for i in range(0, num_full_bytes * 8, 8))
    
    if num_remaining_bits > 0:
        last_byte = int(bit_string[-num_remaining_bits:] + '0' * (8 - num_remaining_bits), 2)
        bytearray_result.append(last_byte)
    
    return bytearray_result

rowValveStateArray = [1] * 19
columnValveStateArray = [1] * 41

row_bytearray = stateArrayToBytearray(rowValveStateArray)
column_bytearray = stateArrayToBytearray(columnValveStateArray)

serialPort.setRowValveStateArray(list(row_bytearray))
serialPort.setColumnValveStateArray(list(column_bytearray))

# =============================================================================
# 
# time.sleep(1)
# 
# for i in range(0,len(columnValveStateArray)):
#     columnValveStateArray[i] = 1
#     column_bytearray = stateArrayToBytearray(columnValveStateArray)
#     serialPort.setColumnValveStateArray(list(column_bytearray))
#     time.sleep(0.2)
#     
# rowValveStateArray = [1] * 19
# columnValveStateArray = [0] * 41
# 
# row_bytearray = stateArrayToBytearray(rowValveStateArray)
# column_bytearray = stateArrayToBytearray(columnValveStateArray)
# 
# serialPort.setRowValveStateArray(list(row_bytearray))
# time.sleep(1)
# serialPort.setColumnValveStateArray(list(column_bytearray))
# 
# 
# for i in range(0,len(rowValveStateArray)):
#     rowValveStateArray[i] = 0
#     row_bytearray = stateArrayToBytearray(rowValveStateArray)
#     serialPort.setRowValveStateArray(list(row_bytearray))
#     time.sleep(0.2)
# =============================================================================
