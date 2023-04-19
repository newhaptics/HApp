# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:30:35 2023

@author: Derek Joslin

"""
import pygame
from GraphicsEngine import *
import Features as f
import numpy as np
import TactileDisplay as td

Display = td.TactileDisplay("testDisplay")
Display.connect("COM4")
Engine = GraphicsEngine((41, 19))

def refreshDisplay():
    Engine.drawFeatures()

    mat = Engine.retrieveList()
    # set the desired to the edited
    Display.set_desiredState(mat)
    print("num: {}".format(0))
    print('---------------------------\n')
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                 for row in mat]))
    print('---------------------------\n')
    # push the desired into current
    Display.push_desiredState()
    Engine.clearFeatures()
    
    
def drawHAppManager():
    # Scene 3
    Engine.addBraille((0,0), "Y")
    Engine.addBraille((1,0), "Avalanche")
    Engine.addBraille((1,1), "Slides")
    Engine.addBraille((1,2), "Notepad")
    
    # Notepad entry
    # context dialog
    Engine.addBraille((0,4), "HApps")

    # modal inteface
    Engine.addBraille((12,4), "H")
    refreshDisplay()

def drawNotePad():
    # Scene 3
    Engine.addBraille((0,0), "Y")
    
    # Notepad entry
    # context dialog
    Engine.addBraille((0,4), "Notepad")

    # modal inteface
    Engine.addBraille((12,4), "H")
    refreshDisplay()
    
def drawSlides():
    # Scene 5
    Engine.addBraille((0,0), "Y")
    
    # context dialog
    Engine.addBraille((0,4), "Slides")

    # modal inteface
    Engine.addBraille((12,4), "H")

    refreshDisplay()
    
def drawAvalanche():
    Engine.addLine((0, 17), (5, 17), 3)
    Engine.addLine((0, 0), (1, 2), 3)
    
    # context dialog
    #Engine.addBraille((0,4), "Avalanche")
    
    # modal inteface
    Engine.addBraille((12,4), "H")
    
    refreshDisplay()

class TreeNode:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def addChild(self, child):
        self.children.append(child)
        
    def __str__(self):
        return self.name
    
HappManager = TreeNode("HApp Manager")
Notepad = TreeNode("Notepad")
Slides = TreeNode("Slides")
Avalanche = TreeNode("Avalanche")

HappManager.addChild(Notepad)
HappManager.addChild(Slides)
HappManager.addChild(Avalanche)

def navigateTree(node, path=""):
    if not node.children:
        print(path + node.name)
    else:
        path += node.name + " > "
        for child in node.children:
            navigateTree(child, path)

def command_line_interface(tree_root):
    current_node = tree_root
    while True:
        print(f"\nCurrent node: {current_node}")
        print("Options:")
        print("  - 'tree' to display the whole tree structure")
        print("  - 'up' to go up one level")
        print("  - 'exit' to quit")

        for i, child in enumerate(current_node.children):
            print(f"  - {i} to select '{child}'")

        user_input = input("Enter your command: ")

        if user_input == "tree":
            print("\nAccessibility Tree:")
            navigateTree(tree_root)
        elif user_input == "up":
            if current_node is not tree_root:
                current_node = tree_root
            else:
                print("Already at the root node.")
        elif user_input == "exit":
            print("Exiting.")
            break
        elif user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(current_node.children):
                current_node = current_node.children[index]
            else:
                print("Invalid index.")
        else:
            print("Invalid command.")

        # draw current node
        if current_node.name == "HApp Manager":
            drawHAppManager()
        elif current_node.name == "Notepad":
            #drawNotePad()
            print("running notepad")
        elif current_node.name == "Slides":
            #drawSlides()
            print("running slides")
        elif current_node.name == "Avalanche":
            #drawAvalanche()
            print("running avalanche")
            
if __name__ == "__main__":
    command_line_interface(HappManager)
