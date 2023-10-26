# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:25:03 2020

@author: Derek Joslin

"""

import copy
import DisplaySerial as ds
import PeripheralDevice as pd


# touch gesture macros
# =============================================================================
# NO_GESTURE = 0x00
# 
# TAP_GESTURE = 0x01
# 
# RIGHT_SWIPE_GESTURE = 0x02
# LEFT_SWIPE_GESTURE = 0x03
# UP_SWIPE_GESTURE = 0x04
# DOWN_SWIPE_GESTURE = 0x05
# 
# CW_WHEEL_GESTURE = 0x06
# CCW_WHEEL_GESTURE = 0x07
# =============================================================================

class TactileDisplay(pd.PeripheralDevice):

    # Tactile Display creates a COM port connection to the embedded processor.
    # HE maintains two primary arrays, currentState and desiredState.
    #   - currentState is populated with the current emebedded state of dot matrix by using pull_currentState.
    #   - desiredState is sent to the embedded processor using push_desiredState
    #   - return_currentState and return_desiredState prints the respective arrays for viewing

    #Tactile Display can also contain a cursor
    def __init__(self, name, port = ''):

        super().__init__(name)

        self.testData = []

        #initialize a cursor position
        self.__pinCursorPosition = [0,0]
        self.__inputCursorPosition = [0,0]
        self.isLinkingCursor = 0
        self.TouchScreenList = []
        self.TouchPosition = []

        #create default desired and current state
        self.__numRows = 19
        self.__numColumns = 41
        self.__currentState = [[0 for i in range(0,self.__numColumns)] for j in range(0,self.__numRows)]
        self.__desiredState = [[0 for i in range(0,self.__numColumns)] for j in range(0,self.__numRows)]

        self.debugString = "size: rows:{} columns:{}".format(self.__numRows, self.__numColumns)

        if port == '':
            self.__comLink = 0
            self.__touchLink = 0
        else:
            self.comLink_on(port,0)
            self.__touchLink = 0
            self.pull_displaySize()


# =============================================================================
#         self.gestureDictionary = {
#             NO_GESTURE: "none",
#             TAP_GESTURE: "tap",
#             RIGHT_SWIPE_GESTURE: "right swipe",
#             LEFT_SWIPE_GESTURE: "left swipe",
#             UP_SWIPE_GESTURE: "up swipe",
#             DOWN_SWIPE_GESTURE: "down swipe",
#             CW_WHEEL_GESTURE: "cw wheel",
#             CCW_WHEEL_GESTURE: "ccw wheel"
#         }
# =============================================================================

    def listResizer(self, listToResize, nColumns, nRows):
        #cutoff the columns
        for index,row in enumerate(listToResize):
            listToResize[index] = [0 for i in range(0,nColumns)]

        #cutoff the rows
        if len(listToResize) > nRows:
            listToResize[nRows:] = []
        elif len(listToResize) < nRows:
            while len(listToResize) < nRows:
                listToResize.append([0 for i in range(0,nColumns)])
        else:
            pass

        return listToResize


    def pull_displaySize(self):
        """ grabs the number of rows and columns from the embedded processor and sets up currentState and desiredState arrays"""


# =============================================================================
#         print("nRows {}".format(self.com.nRows))
#         print("nColumns {}".format(self.com.nColumns))
# =============================================================================
        self.__numRows = self.com.nRows
        self.__numColumns = self.com.nColumns
        self.debugString = "size: rows:{} columns:{}\n".format(self.__numRows, self.__numColumns)
        self.__currentState = self.listResizer(self.__currentState, self.__numColumns, self.__numRows)
        self.__desiredState = self.listResizer(self.__desiredState, self.__numColumns, self.__numRows)

    def display_matrix(self, matrix):
        """ displays the matrix in table view"""
        # print("num: {}".format(num))
        print('---------------------------\n')
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in matrix]))
        print('---------------------------\n')

    def size(self):
        """ returns the current number of rows and columns """
        return (self.__numRows, self.__numColumns)

    def return_currentState(self):
        """ returns the current state of the chip """
        return self.__currentState

    def pull_currentState(self):
        """  grabs the current state from the emebdded side and stores it in currentState """

        matrix_state = self.com.getMatrix()
        state = []
        for byte in matrix_state:

            binary = list(bin(byte))
            del binary[0:2]
            binary = [int(i) for i in binary]

            while len(binary) != 8:
                binary.insert(0,0)

            binary = binary[::-1]

            state.append(binary)

        # del state[-1]

        matrix_state = []
        matrix_state.append([])

        columnIndex = 0
        rowIndex = 0

        for byte in state:

            if columnIndex > (self.__numColumns - 8):
                extensionNum = self.__numColumns - columnIndex
                matrix_state[rowIndex].extend(byte[0:extensionNum])
                #matrix_state[rowIndex].reverse()
                matrix_state.append([])
                columnIndex = 0
                rowIndex = rowIndex + 1
            else:
                matrix_state[rowIndex].extend(byte)
                columnIndex = columnIndex + 8

        matrix_state = [[bool(i) for i in row] for row in matrix_state]

        #reverese items inside list
        #matrix_state.reverse()

        #reverse each item inside the list using map function(Better than doing loops...)
        #matrix_state = list(map(lambda x: x[::-1], matrix_state))

        for rowIndex,row in enumerate(matrix_state):
            for elemIndex,elem in enumerate(row):
                self.__currentState[rowIndex][elemIndex] = copy.deepcopy(elem)

    def return_desiredState(self):
        """ returns the desired state of the dot matrix """
        return self.__desiredState

    def set_desiredState(self, newState):
        """ sets a desired state of the dot matrix """
        for rowIndex,row in enumerate(newState):
            for elemIndex,elem in enumerate(row):
                self.__desiredState[rowIndex][elemIndex] = copy.deepcopy(int(elem))

    def push_desiredState(self):
        """ sends the desired state of the dot matrix to the embedded side resulting in a refresh"""
        #sendMatrix = np.array(self.__desiredState)
        #flipMatrix = np.fliplr(sendMatrix)

        #only refresh rows which need refresh
        rowIndex = 0
        for (desiredRowData,currentRowData) in zip(self.__desiredState,self.__currentState):
            #currentRowData.reverse()
            if desiredRowData != currentRowData:
                self.testData = desiredRowData
                #programmatically flip data in currentRowData to desired
                currentRowData.clear()
                currentRowData.extend(desiredRowData)
                self.com.setRow(rowIndex,desiredRowData)
            rowIndex += 1

    def connect(self, COM, *args):
        """ creates connection to embedded side and initializes dot matrix size"""
        if len(args) > 0:
            if args[0] == 1:
                onOff = 1
            else:
                onOff = 0
        else:
            onOff = 0

        self.com = ds.DisplaySerial(COM, 115200, 3)
        self.com.getSize()
        self.pull_displaySize()
        self.__comLink = 1

    def comLink_off(self):
        """ removes connection to embedded side """
        self.__comLink = 0
        self.com.close()
        del self.com

    def comLink_check(self):
        """ checks connection to embedded side """
        return self.__comLink

    def clear(self):
        for sublist in self.__desiredState:
            for i in range(len(self.__desiredState)):
                self.__desiredState[i] = 0
        self.push_desiredState()

    # function that returns the gesture which has occurred
    def detectTouchGesture(self):
        gestureId = self.com.getTouchGesture()[0]
        return self.gestureDictionary[gestureId]