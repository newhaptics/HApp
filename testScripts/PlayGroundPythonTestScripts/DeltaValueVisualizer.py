# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:20:45 2023

@author: Derek Joslin

"""


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
import PyQt5.QtCore as qc
import serial.tools.list_ports
import serial


class SensorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sensor Heatmap")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)


        self.sensorList = []
        # Create labels for each sensor
        for i in range(35):
            sensor = QLabel()
            self.sensorList.append(sensor)
            sensor.setAlignment(qc.Qt.AlignCenter)
            self.grid_layout.addWidget(sensor, i // 5, i % 5)
            
            
        print(self.sensorList)
        
        # Get a list of available COM ports
        comports = list(serial.tools.list_ports.comports())
        
        # Check if any COM ports are available
        if not comports:
            print('No COM ports available')
            exit()
            
        # Connect to the first available COM port
        port = comports[0].device
        baudrate = 115200  # Set the baud rate to use for the serial connection
        timeout = 1  # Set the timeout for reading from the serial connection
        
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        
        # Print information about the connected port
        print(f'Connected to {self.ser.name} ({self.ser.baudrate} baud)')

        # Send byte array
        self.byte_array = bytearray([1, 2, 3, 0, 2, 4, 35, 0, 3, 2, 1])
        self.ser.write(self.byte_array)

        self.comportBytes = []  # Create empty list to store received bytes
        
        # Create a QTimer that calls collect_sensor_data() every 1000 ms
        self.timer = qc.QTimer(self)
        self.timer.timeout.connect(self.collect_sensor_data)
        self.timer.start(10)
    
    def collect_sensor_data(self):
        # Read data from the COM port and parse the information
        # Update the sensor values using setSensorValues() function
        sensor_values = []
        #print("collecting sensor data")
        if self.ser.in_waiting > 0:  # Check if there are bytes in the input buffer
            byte = self.ser.read()  # Read a single byte from the serial port
            self.comportBytes.append(byte)  # Add the byte to the list
            
        i = 0
        if len(self.comportBytes) == 45:
            self.comportBytes[0:7] = []
            self.comportBytes[-3:-1] = []
            byteString = ""
            for byte in self.comportBytes:
                smolString = ' {} '.format(int.from_bytes(byte, byteorder='big', signed=False))
                byteString += smolString
                sensor_values.append(smolString)
                i += 1
                if i > 5:
                    byteString += "\n"
                    i = 0
            print(byteString)
            print("\n" * 35)
            self.comportBytes.clear()
            self.ser.write(self.byte_array)
            self.setSensorValues(sensor_values)
            
            
    def setSensorValues(self, sensor_values):
        # Set the value of each sensor label based on input values
        for i,sensor in enumerate(self.sensorList):
            try:
                sensor.setText(sensor_values[i])
            except:
                print("no value")
            
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SensorWindow()
    window.show()
    sys.exit(app.exec_())







