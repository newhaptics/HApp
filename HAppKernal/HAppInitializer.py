# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:23:43 2022

@author: Derek Joslin

"""

import cairo
import serial
import LLMOS as llm
import sys

HapticOS = llm.LLMOS(openAIKey, elevenLabsKey)

# import the remaining HapticOS Libraries
import HAppMainWindow as hm
from PyQt5 import QtWidgets as qw
import sys

if __name__ == '__main__':

    app = qw.QApplication([])

    MainWindow = hm.HAppMainWindow(HapticOS)
    MainWindow.show()

    sys.exit(app.exec_())