# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:43:56 2022

@author: derek
"""


filename = "C:/Users/derek/OneDrive/NewHaptics Shared/HapticOS/FC_GUI_API/APIv0.7-Coeus/v0.766-Coeus/ROMs/FileNavigatorTouch/FileNavigatorTouchReady.rom"

fileFolderList = filename.split("/")

folderDirectory = ""

for folder in fileFolderList[:-1]:
    folderDirectory = folderDirectory + folder + "//"
    
print(folderDirectory)
    
    