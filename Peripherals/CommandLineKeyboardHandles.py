# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:45:42 2023

@author: Derek Joslin

"""

import DefaultKeyboardHandles as dk

class CommandLineKeyboardHandles(dk.DefaultKeyboardHandles):
    
    def __init__(self, CommandLine):
        self.editor = CommandLine
        
    def KeyLeftHandler(self):
        #perform cursor movement left
        self.editor.moveCursorBackward()
        #self.updateDisplay()
        
    def KeyUpHandler(self):
        #perform cursor movement up
        self.editor.moveCursorUpward()
        #self.updateDisplay()
        
    def KeyRightHandler(self):
        #perform cursor movement right
        self.editor.moveCursorForward()
        #self.updateDisplay()
        
    def KeyDownHandler(self):
        #perform cursor movement down
        self.editor.moveCursorDownward()
        #self.updateDisplay()
        
    def KeySpaceHandler(self):
        self.editor.insertCharacter(" ")
        #self.updateDisplay()
        
    def KeyAHandler(self):
        self.editor.insertCharacter("a")
        #self.updateDisplay()
        #print("Editor A key pressed")
        
    def KeyBHandler(self):
        self.editor.insertCharacter("b")
        #self.updateDisplay()
       #print("Editor B key pressed")
        
    def KeyCHandler(self):
        self.editor.insertCharacter("c")
        #self.updateDisplay()

       #print("Editor C key pressed")
        
    def KeyDHandler(self):
        self.editor.insertCharacter("d")
        #self.updateDisplay()
       #print("Editor D key pressed")
        
    def KeyEHandler(self):
        self.editor.insertCharacter("e")
        #self.updateDisplay()
       #print("Editor E key pressed")

    def KeyFHandler(self):
        self.editor.insertCharacter("f")
        #self.updateDisplay()
       #print("Editor F key pressed")
        
    def KeyGHandler(self):
        self.editor.insertCharacter("g")
        #self.updateDisplay()
       #print("Editor G key pressed")
        
    def KeyHHandler(self):
        self.editor.insertCharacter("h")
        #self.updateDisplay()
       #print("Editor H key pressed")
        
    def KeyIHandler(self):
        self.editor.insertCharacter("i")
        #self.updateDisplay()
       #print("Editor I key pressed")
        
    def KeyJHandler(self):
        self.editor.insertCharacter("j")
        #self.updateDisplay()
       #print("Editor J key pressed")
        
    def KeyKHandler(self):
        self.editor.insertCharacter("k")
        #self.updateDisplay()
       #print("Editor K key pressed")
        
    def KeyLHandler(self):
        self.editor.insertCharacter("l")
        #self.updateDisplay()
       #print("Editor L key pressed")
        
    def KeyMHandler(self):
        self.editor.insertCharacter("m")
        #self.updateDisplay()
       #print("Editor M key pressed")
        
    def KeyNHandler(self):
        self.editor.insertCharacter("n")
        #self.updateDisplay()
       #print("Editor n key pressed")
        
    def KeyOHandler(self):
        self.editor.insertCharacter("o")
        #self.updateDisplay()
       #print("Editor O key pressed")

    def KeyPHandler(self):
        self.editor.insertCharacter("p")
        #self.updateDisplay()
       #print("Editor P key pressed")
        
    def KeyQHandler(self):
        self.editor.insertCharacter("q")
        #self.updateDisplay()
       #print("Editor Q key pressed")
        
    def KeyRHandler(self):
        self.editor.insertCharacter("r")
        #self.updateDisplay()
       #print("Editor R key pressed")
        
    def KeySHandler(self):
        self.editor.insertCharacter("s")
        #self.updateDisplay()
       #print("Editor S key pressed")
        
    def KeyTHandler(self):
        self.editor.insertCharacter("t")
        #self.updateDisplay()
       #print("Editor T key pressed")
        
    def KeyUHandler(self):
        self.editor.insertCharacter("u")
        #self.updateDisplay()
       #print("Editor u key pressed")
        
    def KeyVHandler(self):
        self.editor.insertCharacter("v")
        #self.updateDisplay()
       #print("Editor V key pressed")
        
    def KeyWHandler(self):
        self.editor.insertCharacter("w")
        #self.updateDisplay()
       #print("Editor W key pressed")
        
    def KeyXHandler(self):
        self.editor.insertCharacter("x")
        #self.updateDisplay()
       #print("Editor X key pressed")
        
    def KeyYHandler(self):
        self.editor.insertCharacter("y")
        #self.updateDisplay()
        #print("Editor Y key pressed")
      
    def KeyZHandler(self):
        self.editor.insertCharacter("z")
        #self.updateDisplay()
       #print("Editor z key pressed")

    def KeyBackSpaceHandler(self):
        self.editor.deleteCharacter()
        #self.updateDisplay()

# =============================================================================
#     def KeyEnterHandler(self):
#         print("executing {}".format(self.editor.contents))
#         self.editor.clear()
# 
#     def KeyReturnHandler(self):
#         print("executing {}".format(self.editor.contents))
#         self.editor.clear()
# 
# =============================================================================
    def Key0Handler(self):
        self.editor.insertCharacter("0")
        #self.updateDisplay()

    def Key1Handler(self):
        self.editor.insertCharacter("1")
        #self.updateDisplay()
        
    def Key2Handler(self):
        self.editor.insertCharacter("2")
        #self.updateDisplay()
        
    def Key3Handler(self):
        self.editor.insertCharacter("3")
        #self.updateDisplay()

    def Key4Handler(self):
        self.editor.insertCharacter("4")
        #self.updateDisplay()
        
    def Key5Handler(self):
        self.editor.insertCharacter("5")
        #self.updateDisplay()

    def Key6Handler(self):
        self.editor.insertCharacter("6")
        #self.updateDisplay()
        
    def Key7Handler(self):
        self.editor.insertCharacter("7")
        #self.updateDisplay()
        
    def Key8Handler(self):
        self.editor.insertCharacter("8")
        #self.updateDisplay()

    def Key9Handler(self):
        self.editor.insertCharacter("9")
        #self.updateDisplay()

    def KeyParenLeftHandler(self):
        self.editor.insertCharacter("(")
        #self.updateDisplay()

    def KeyParenRightHandler(self):
        self.editor.insertCharacter(")")
        #self.updateDisplay()

    def KeyCommaHandler(self):
        self.editor.insertCharacter(",")
        #self.updateDisplay()
        
    def KeyPlusHandler(self):
        self.editor.insertCharacter("+")
        #self.updateDisplay()
        
    def KeyMinusHandler(self):
        self.editor.insertCharacter("-")
        #self.updateDisplay()
        
    def KeyAsteriskHandler(self):
        self.editor.insertCharacter("*")
        #self.updateDisplay()
        
    def KeyPeriodHandler(self):
        self.editor.insertCharacter(".")
        #self.updateDisplay()
        
    def KeySlashHandler(self):
        self.editor.insertCharacter("\\")
        #self.updateDisplay()
        
    def KeyColonHandler(self):
        self.editor.insertCharacter(":")
        #self.updateDisplay()
        
    def KeySemicolonHandler(self):
        self.editor.insertCharacter(";")
        #self.updateDisplay()
        
    def BracketLeftHandler(self):
        self.editor.insertCharacter("[")     
        #self.updateDisplay()
        
    def BracketRightHandler(self):
        self.editor.insertCharacter("]")
        #self.updateDisplay()

        
    def EqualHandler(self):
        self.editor.insertCharacter("=")
        #self.updateDisplay()

        
    def GreaterHandler(self):
        self.editor.insertCharacter(">")
        #self.updateDisplay()

        
    def LessHandler(self):
        self.editor.insertCharacter("<")
        #self.updateDisplay()

        
    def QuoteDblHandler(self):
        self.editor.insertCharacter('"')
        #self.updateDisplay()

        
    def QuoteLeftHandler(self):
        self.editor.insertCharacter("'")
        #self.updateDisplay()