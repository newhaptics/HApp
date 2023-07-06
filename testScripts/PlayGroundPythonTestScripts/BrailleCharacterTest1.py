# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:31:22 2023

@author: derek
"""

import serial

def genericSerialCommand(serial, responseBytes):

        if responseBytes > 0:
            responseList = []

            response = serial.read(responseBytes)

            for byte in response:
                responseList.append(byte)

        else:
            responseList = None

        confirmBit = int.from_bytes(serial.read(1), byteorder='big', signed=False)

        #serial.commandHistory.append((confirmBit,responseList))

        return responseList

def print_bits(responseList):
    
    rowString = ""
    nBytes = 0
    
    for element in responseList:
        nBytes += 1
        for i in range(8):
            bit = (element >> i) & 1
            rowString += "{}".format(bit)
        
        # if N_BYTES_PER_ROW exceeded print the rowString
        if nBytes > 5:
            print(rowString)
            rowString = ""
            nBytes = 0


# Initialize serial port
ser = serial.Serial('COM7', baudrate=57600, timeout=0.1)

while True:
    if ser.in_waiting > 0:
        responseList = genericSerialCommand(ser, 210)
        print(" " * 40)
        print_bits(responseList)
        print(" " * 40)
        
    # Clear serial port
    ser.reset_input_buffer()