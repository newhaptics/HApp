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
            msbString = ''.join(map(str, byte))
            lsbString = '0b' + ''.join(reversed(msbString))
            
            output.append(int(lsbString, base=2))
        
# =============================================================================
#         print("row index to edit {}".format(rowIndex))
#         print("row data to set {}".format(rowData))
#         print("encoded row data {}".format(output))
# =============================================================================
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

# =============================================================================
#     # Function 4: Returns 1 if matrix is in the process of refreshing, 0 if done refreshing.        
#     def is_idle(self):
#         #create list to be the output
#         output = []
#         
#         #select the fourth function
#         output.append(4)
#         
#         #send the byte
#         self.port.write(bytearray(output))
#         
#         #read whether the device is idle
#         # self.__recieveBuffer = self.port.read_until(b'\x0b')
#         self.__recieveBuffer_value = self.port.read(1)
# 
#         #read the output on the serial port
#         self.__readSerialResponse()
# 
#         return self.__recieveBuffer_value
#         
#     # Function 5: Turns all electronic valves OFF    
#     def turn_off(self):
#         #create the list for output
#         output = []
#         
#         #select the fifth function
#         output.append(5)
#         
#         #send the byte
#         self.port.write(bytearray(output))
#         
#         #read the output on the serial port
#         self.__readSerialResponse()
#         
#     # Function 6: Turns source pressure ON
#     def turn_on(self):
#         #create a list for the output
#         output = []
#         
#         #select the sixth function
#         output.append(6)
#         
#         #send the command
#         self.port.write(bytearray(output))
#         
#         
#         
#         #read the output on the serial port
#         self.__readSerialResponse()
#         
#         
#         
#     # Function 7: Sets value of matrix to desired state. Input is m x n array, where m = numRows and n=numCols of matrix.
#     def set_matrix(self, mat):
#         
#         #create a list for the output
#         output = []
#         
#         #flush the port
#         self.port.flushInput()
#         
#         #select the first function as set matrix is implementing set row
#         #output.append(1)
#         
#         #response = self.port.write(bytearray(output))
#          
#         #take list of rows and create byte arrays out of each row
#         rowIndex = 1
#         for rowData in mat:    
#             self.set_row(rowIndex,rowData)
#             rowIndex += 1            
#             
#             
#         test = 1
#     
#     # Function 7: Sets value of matrix to desired state. Input is m x n array, where m = numRows and n=numCols of matrix.
#     def setMatrix(self, mat):
#         #create a list for the output
#         output = []
#         
#         #select the seventh function
#         output.append(7)
#         
#         #flush the port
#         self.port.flushInput()
#         
#         #take list of rows and create byte arrays out of each row
#         fill = 0
#         N = 8
#         for rowData in mat:
#             row = list(map(int, rowData))[::-1]
#             tempList = row + [fill] * N
#             subList = [tempList[n:n+N] for n in range(0, len(row), N)]
#             for lst in subList:
#                 s = '0b' + ''.join(map(str, lst))
#                 output.append(int(s, base=2))
#     
#         #send the command
#         #n = len(output)
#         test = self.port.write(bytearray(output))
#         #self.port.write(bytearray(output[0:n/2]))
#         
#         #self.port.write(bytearray(output[n/2:n-1]))
#         
#         #read the output on the serial port
#         self.__readSerialResponse()
#         
#     # Function 8: Sets state of single dot. Inputs: (row_index=1:num_rows, col_index=1:num_cols, state=0,1)  
#     def set_dot(self, rowIndex, colIndex, data):
#         #create output list
#         output = []
#         
#         #select the eighth function
#         output.append(8)
#         
#         #add the row index column index and state
#         output.append(rowIndex-1) # accomodate 0 index shift
#         output.append(colIndex-1) # accomodate 0 index shift
#         output.append(data)
#         
#         #send the command
#         self.port.write(bytearray(output))
#         
#         #read the output on the serial port
#         self.__readSerialResponse()
#         
#     # Function 9: Sets state of all dots ON or OFF. Input: (state=0,1)    
#     def set_all(self, data):
#         #create output list
#         output = []
#         
#         #select function
#         output.append(9)
#         
#         #add the desired data for the state to be set to
#         output.append(data)
#         
#         #send the command
#         self.port.write(bytearray(output))
#         
#         #read the output on the serial port
#         self.__readSerialResponse()
# =============================================================================
    
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