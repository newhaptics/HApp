# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:23:43 2022

@author: Derek Joslin

"""

import cairo
import serial
import LLMOS as llm
import sys

elevenLabsKey = "188c0f632906bc15892cf9955e3c1253"
openAIKey = "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"
HapticOS = llm.LLMOS(openAIKey, elevenLabsKey)

# import the remaining HapticOS Libraries
import HAppMainWindow as hm
from PyQt5 import QtWidgets as qw
import sys

if __name__ == '__main__':

    app = qw.QApplication([])

    MainWindow = hm.HAppMainWindow(HapticOS)
    
    sys.exit(app.exec_())