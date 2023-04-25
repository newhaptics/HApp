# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:39:32 2020

@author: Derek Joslin
"""

import serial

class DisplaySerial(serial.Serial):

     #the Board Com object contains a serial port connection object and commands to communicate with hardware

    def __init__(self, *args):
        # if there is more than a single arguement intialize with baudrate
        if len(args) > 1:
            super().__init__(args[0], args[1], timeout=args[2])
        else:
            super().__init__(args[0])

        self.read(1)
        # create command history
        self.commandHistory = []

    def getSize(self):
        self.nRows = self.getNRows()
        self.nColumns = self.getNColumns()
        self.nBytesPerRow = self.getNBytesPerRow()
        self.nBytesPerColumn = self.getNBytesPerColumn()

# =============================================================================
#     #sets the echo of the com port onOff (0=Off, 1=On)
#     def echo(self, onOff):
#         if onOff:
#             self.__echo = 1
#         else:
#             self.__echo = 0
#     
# =============================================================================
    #opens the serial port
# =============================================================================
#     def open(self):
#         self.port.open()
#         self.__readSerialResponse()
# =============================================================================

# =============================================================================
#     #closes the serial port
#     def close(self):
#         self.port.close()
# 
#     #if echo is on prints the recieve data
#     def __print_rx(self):
#         read = self.__read_rx()
#         if self.__echo:
#             print(read)
#         else:
#             pass
#         
#     #reads in data on the serial line
#     def __read_rx(self):
#         # self.port.flushInput()
#         self.__recieveBuffer = self.port.read(1)
#         return self.__recieveBuffer #.decode('utf-8')
#     
#     #reads one byte and prints based on echo state
#     def __readSerialResponse(self):
#         read = self.port.read(1)
#         if self.__echo:
#             print(read)
#         else:
#             pass
#         
# =============================================================================
    # Function 1: Sets state of a row on the chip
    def setRow(self, rowIndex, rowData):
        #select the set Row Function (1)
        self.write(bytearray([1]))
        
        output = []
        
        #add the row index to the list
        output.append(rowIndex) 

        rowData = list(map(int, rowData))

        fill = 0
        N = 8
        # pad the data so that all of the row data can fit into a mulitple of 8 bits
        padList = rowData + [fill] * N
        
        # create a list with each element as a byte representing 8 bits of data in the rowData
        byteList = [padList[n:n+N] for n in range(0, len(rowData), N)]
        
        for byte in byteList: 
            msbString = '0b' +''.join(map(str, byte))
            
            #lsbString = '0b' + ''.join(reversed(msbString))
            output.append(int(msbString, base=2))
        
        #send as bytearray with each parameter as a byte
        self.write(bytearray(output))
        
        responseList = self.genericSerialCommand(0)# + (self.nBytesPerRow/8)*2)
        

    # Function 2: Sets display matrix to all 0s and turns all electronic valves OFF    
    def forceClearAll(self):
        #create list of bytes to send
        self.write(bytearray([2]))
        
        responseList = self.genericSerialCommand(1)
        
        #print the recieved bit
        return responseList[0]

    # Function 3: Returns the current state of the matrix
    def getMatrix(self):
        self.write(bytearray([3]))
        nMatrixBytes = self.nBytesPerRow * self.nRows
        
        return self.genericSerialCommand(nMatrixBytes)
    
    # Function 10: Returns number of rows of dot matrix
    def getNRows(self):
        #send the function 10 command
        self.write(bytearray([10]))

        responseList = self.genericSerialCommand(1)
        
        return responseList[0]

    # Function 11: Returns number of columns of dot matrix
    def getNColumns(self):
        #send the function 11 command
        self.write(bytearray([11]))

        responseList = self.genericSerialCommand(1)

        return responseList[0]

    # Function 12: Returns number of bytes to expect per row of the matrix. 
    def getNBytesPerRow(self):
        #send the function 12 command
        self.write(bytearray([12]))

        responseList = self.genericSerialCommand(1)

        return responseList[0]
    
    # Function 15: Gets the RowValveArray
    def getRowValveArray(self):
        self.write(bytearray([15]))
        
        responseList = self.genericSerialCommand(self.nRows)

        return responseList

    # Function 16: Sets the state of elements in rowValveArray
    def setRowValveArrayAssignment(self, rowValveArray):
        self.write(bytearray([16]))

        self.write(bytearray(rowValveArray))

        self.genericSerialCommand(0)

    # Function 17: Gets the Column valve array assignments
    def getColumnValveArray(self):
        # send the function 17 command
        self.write(bytearray([17]))
        
        responseList = self.genericSerialCommand(self.nColumns)
        
        return responseList

    # Function 18: Sets the start of elements in columnValveArray
    def setColumnValveArrayAssignment(self, columnValveArray):
        self.write(bytearray([18]))

        self.write(bytearray(columnValveArray))

        self.genericSerialCommand(0)

    # Function 19: Sets the state of all valves in a row
    def setRowValveStateArray(self, valveStateArray):
        # send the function 19 command
        self.write(bytearray([19]))

        self.write(bytearray(valveStateArray))

        self.genericSerialCommand(0)

    # Function 20: Sets the state of all valves in a column
    def setColumnValveStateArray(self, valveStateArray):
        self.write(bytearray([20]))

        self.write(bytearray(valveStateArray))

        self.genericSerialCommand(0)
        
    # Function 21: turns off the refresh matrix
    def setRefreshMatrix(self, onOff):
        self.write(bytearray([21]))
        
        self.write(bytearray([onOff]))
        
        self.genericSerialCommand(0)

    # Function 23: Gets the number of bytes in a column
    def getNBytesPerColumn(self):
        #send the function 23 command
        self.write(bytearray([23]))

        responseList = self.genericSerialCommand(1)

        return responseList[0]

    # Function 32: Sets the state of all valves in a column
    def setValveStateArray(self, valveStateArray):
        self.write(bytearray([32]))

        self.write(bytearray(valveStateArray))

        self.genericSerialCommand(0)
        
    # Function 35: sets the parameters relating to driving the solenoids
    def setSolenoidDriver(self, settingArray):
        self.write(bytearray([35]))

        self.write(bytearray(settingArray))
        
        self.genericSerialCommand(0)
        
    # Function 36: retieves the current value of parameters related to driving solenoids
    def getSolenoidDriver(self):
        self.write(bytearray([36]))

        responseList = self.genericSerialCommand(8)
        
        return responseList

    def genericSerialCommand(self, responseBytes):
        
        if responseBytes > 0:
            responseList = []
            
            response = self.read(responseBytes)
                    
            for byte in response:
                responseList.append(byte)
            
        else:
            responseList = None
            
        confirmBit = int.from_bytes(self.read(1), byteorder='big', signed=False)
        
        self.commandHistory.append((confirmBit,responseList))
        
        return responseList