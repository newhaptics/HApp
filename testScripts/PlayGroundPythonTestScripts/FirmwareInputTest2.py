# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 09:59:10 2023

@author: Derek Joslin

"""

import serial

com = serial.Serial("COM23", timeout=0.3)


while 1:
    try:
        while 1:
            print(com.read(15))
    except:
        pass
