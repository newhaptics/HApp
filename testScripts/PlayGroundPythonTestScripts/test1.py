# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:18:40 2023

@author: derek
"""

from DisplaySerial import DisplaySerial

testSerial = DisplaySerial("COM3", 57600, 3)
response = testSerial.getRefreshStateParameters()
response[0] = 30

testSerial.setRefreshStateParameters(response)

response = testSerial.getRefreshStateParameters()

# =============================================================================
# response = testSerial.getSolenoidDriver()
# 
# response[0] = 10
# response[-2] = 1
# response[2] = 5
# 
# 
# testSerial.setSolenoidDriver(response)
# 
# response = testSerial.getSolenoidDriver()
# =============================================================================
