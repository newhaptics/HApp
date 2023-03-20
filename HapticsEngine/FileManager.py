# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:35:39 2020

@author: Derek Joslin

"""

import csv
import sys
import os

class FileManager():

    def __init__(self):
        # Root path
        self.rootSoftwarePath = os.getcwd()
        self.rootSoftwarePath = self.rootSoftwarePath.split("HApp\\", 1)
        self.rootSoftwarePath = self.rootSoftwarePath[0] + "HApp//"

        # Path to software folder of the current version
        self.pathToSoftwareFolder = self.rootSoftwarePath #+ self.softwareReleaseFolder + self.softwareFolder

        # Add the software folder to the python path
        try:
            print("Adding Directories to the Path...")
            sys.path.append(self.pathToSoftwareFolder)
            self.addSubdirectories()
        except Exception as e:
            print("Error Adding Directories to the Path")
            print(e)

    def addSubdirectories(self):
        # List all the subdirectories in the software folder
        subdirectories = [d for d in os.listdir(self.pathToSoftwareFolder) if os.path.isdir(os.path.join(self.pathToSoftwareFolder, d))]

        # Add each subdirectory to the python path
        for subdirectory in subdirectories:
            if subdirectory != "Legacy":
                sys.path.append(os.path.join(self.pathToSoftwareFolder, subdirectory))

    def addDirectory(self, directoryPath):
        sys.path.append(directoryPath)

    def makeCWD(self, directoryString):
        subDirectoryList = os.listdir(self.pathToSoftwareFolder)
        for subdirectory in subDirectoryList:
            if subdirectory == directoryString:
                directioryPath = os.path.join(self.pathToSoftwareFolder, subdirectory)
                os.chdir(directioryPath)

    # find the Roms and create a rom dictionary
    def createRomDirectory(self):
        # search the subdirectories and extract the Rom directories
        romDirectory = self.pathToSoftwareFolder + "ROMS//"
        romList = os.listdir(romDirectory)
        
        romDictionary = {}
        for rom in romList:
            romDictionary[rom] = romDirectory + rom + "//" + rom + ".rom"
            
        return romDictionary
        

    def saveFile(self, filePath, fileData):
        # Decide which state to save
        self.saveCsv(filePath, fileData)

# =============================================================================
#         options = qw.QFileDialog.Options()
#         options |= qw.QFileDialog.DontUseNativeDialog
#         source = qw.QFileDialog.getSaveFileName(self.MainWindow,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)[0]
# =============================================================================

    def loadFile(self, filePath):
        # Navigate to the Roms folder

# =============================================================================
#         options = qw.QFileDialog.Options()
#         options |= qw.QFileDialog.DontUseNativeDialog
#         source = qw.QFileDialog.getOpenFileName(self.MainWindow,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)[0]
# =============================================================================

        if filePath[-4:-1] == ".cs":
            matData = self.openCsv(filePath)
            #format the matData properly from strings into ints
            return [[int(i) for i in row] for row in matData]
        elif filePath[-4:-1] == ".pn":
            matData = self.openPng(filePath)
            #format the matData properly from strings into ints
            #return [[int(i) for i in row] for row in matData]
        elif filePath[-4:-1] == ".tx":
            print("{} is a text file".format(filePath))
        elif filePath[-4:-1] == ".ro":
            self.openRom(filePath)
            return
        else:
            return

    def openTxt(self, filePath):
    # =============================================================================
    #     print(repr(open(filename, 'rb').read(200))) # dump 1st 200 bytes of file
    #     data = open(filename, 'rb').read()
    #     print(data.find('\x00'))
    #     print(data.count('\x00'))
    # =============================================================================
        d = {}
        with open(filePath, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='\t')
            for row in csv_reader:
                d[row[0]] = row[1:]
        return d

    def openCsv(self, filePath):
        
    # =============================================================================
    #     print(repr(open(filename, 'rb').read(200))) # dump 1st 200 bytes of file
    #     data = open(filename, 'rb').read()
    #     print(data.find('\x00'))
    #     print(data.count('\x00'))
    # =============================================================================
        
        d = []
        with open(filePath, 'rt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                d.append(row)
        return d

    def openPng(self, filePath):
        print("opening {0}".format(filePath))
# =============================================================================
#         with Image.open(filename) as p:
#             print(p.format)
#             print(p.mode)
#             print(p.size)
#             p = p.resize(size,Image.ANTIALIAS)
#             pix = (numpy.array(p)).tolist()
#             #go through image and convert all lists in list to black and white
#             for (i,row) in enumerate(pix):
#                 for (j,RGB) in enumerate(row):
#                     if p.mode == "RGBA":
#                         if RGB[3] > 100:
#                             pix[i][j] = 1
#                         else:
#                             pix[i][j] = 0
#                     else:
#                         if (sum(RGB)/3) < 250:
#                             pix[i][j] = 1
#                         else:
#                             pix[i][j] = 0
#             print(pix)
#             return pix
# =============================================================================

    def openRom(self, filePath):
        """ Read in tactile roms """
        print("opening {0}".format(filePath))
        
        #filename = 'C:/Users/derek/OneDrive/NewHaptics Shared/HapticOS/FC_GUI_API/APIv0.7-Coeus/v0.762-Coeus/ROMs/NotePad/NotePadReady.rom'
        
        #.initializeRom(filePath)
        
    def saveCsv(self, filename, mat):
        
        with open(filename, "w") as f:
            for row in mat:
                for (i,elem) in enumerate(row):
                    if elem == True:
                        f.write("{0}".format(1))
                    elif elem == False:
                        f.write("{0}".format(0))
                    if i is not len(row) - 1:
                        f.write(",")
                f.write("\n")
        f.close()