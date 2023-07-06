# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:06:51 2023

@author: Derek Joslin

"""


from DisplaySerial import *
import time

testDisplay = DisplaySerial("COM7", 57600, 3)
testDisplay.getRefreshMatrixProtocols()

testOne = [1 for i in range(0,41)]
testZero = [0 for i in range(0,41)]

# set all zeros
for i in range(0,19):
    testDisplay.setRow(i,testZero)
time.sleep(11)
print(testDisplay.getRefreshMatrixState())


# set all ones
for i in range(0,19):
    testDisplay.setRow(i,testOne)
    print(testDisplay.getRefreshMatrixState())
    time.sleep(0.01)
    print(testDisplay.getRefreshMatrixState())
    time.sleep(0.01)
    print(testDisplay.getRefreshMatrixState())
    time.sleep(0.01)
    print(testDisplay.getRefreshMatrixState())
    time.sleep(0.01)
    print(testDisplay.getRefreshMatrixState())
    time.sleep(0.01)
    print(testDisplay.getRefreshMatrixState())
# set a single row zero
# =============================================================================
# print("single zero")
# testDisplay.setRow(0,testZero)
# startTime = time.time()
# elapsed = time.time()
# while elapsed < startTime + 1:
#     print(testDisplay.getRefreshMatrixState())
#     elapsed = time.time()
#     print(elapsed - startTime)
#     
# print(testDisplay.getRefreshMatrixState())
# 
# # set a single row zero
# print("single one")
# testDisplay.setRow(0,testOne)
# startTime = time.time()
# elapsed = time.time()
# while elapsed < startTime + 1:
#     print(testDisplay.getRefreshMatrixState())
#     elapsed = time.time()
#     print(elapsed - startTime)
# 
# print(testDisplay.getRefreshMatrixState())
# 
# =============================================================================
