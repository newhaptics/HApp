# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:12:00 2023

@author: Derek Joslin

"""

from PyQt5 import QtWidgets as qw
import sys
import TactileDisplayVisualizer as tdv



if __name__ == '__main__':

    app = qw.QApplication([])
    MainWindow = qw.QMainWindow()
    
    TactileDisplayVisualizer = tdv.TactileDisplayVisualizer("testVisu", (19,40))
    MainWindow.setCentralWidget(TactileDisplayVisualizer)
    
    
    print(TactileDisplayVisualizer.getCoordinateSystem())

    MainWindow.show()
    sys.exit(app.exec_())