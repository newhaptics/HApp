# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:32:03 2022

@author: Derek Joslin
"""

from pynput import keyboard

import PeripheralDevice as pd

class KeyboardPeripheral(pd.PeripheralDevice):
    
    def __init__(self, name, KeyBoardHandles):
        super().__init__(name)
            
        # stores all the keys pressed and their order
        self.keyHistory = []
        
        # defines if the control key is on
        self.controlOn = 0
        
        self.DefaultKeyboardHandles = KeyBoardHandles
        self.KeyboardHandles = KeyBoardHandles

    def setNewKeyboardHandler(self, newKeyboardHandles):

        self.KeyboardHandles = newKeyboardHandles

    def revertToDefaultHandler(self):
        
        self.KeyboardHandles = self.DefaultKeyboardHandles

    def setDefaultHandler(self, DefaultKeyboardHandles):
        
        self.DefaultKeyboardHandles = DefaultKeyboardHandles
        self.KeyboardHandles = DefaultKeyboardHandles

    def handleKeyPressEvent(self, key):

        #key = keyPressEvent.key()
        try:
            if key.char:
                
                key = key.char
        except:
            pass
        
        try:

            self.debugString = "Key Pressed: {}".format(chr(key))

        except:

            self.debugString = "Key Pressed: {}".format(key)

        # add the key to the key history list
        self.keyHistory.append(key)

        # if more than 100 keys pressed pop
        if len(self.keyHistory) > 100:
            self.keyHistory.pop(0)
            
        if self.controlOn:
            #self.controlPressedHandlers(key)
            pass
        else:
            try:
                self.normalHandlers(key)
            except Exception as e:
                print("key error: {}".format(e))

    def normalHandlers(self, key):

        if key == keyboard.Key.space:
            
            self.KeyboardHandles.KeySpaceHandler()

        elif key == keyboard.Key.left:

            self.KeyboardHandles.KeyLeftHandler()
            
        elif key == keyboard.Key.up:

            self.KeyboardHandles.KeyUpHandler()

        elif key == keyboard.Key.right:

            self.KeyboardHandles.KeyRightHandler()

        elif key == keyboard.Key.down:

            self.KeyboardHandles.KeyDownHandler()

        elif key == 'a' or key == 'A':
            #print("test")

            self.KeyboardHandles.KeyAHandler()
            
        elif key == 'b' or key == 'B':
        
            self.KeyboardHandles.KeyBHandler()
            
        elif key == 'c' or key == 'C':
        
            self.KeyboardHandles.KeyCHandler()
            
        elif key == 'd' or key == 'D':
        
            self.KeyboardHandles.KeyDHandler()
            
        elif key == 'e' or key == 'E':
        
            self.KeyboardHandles.KeyEHandler()
            
        elif key == 'f' or key == 'F':
        
            self.KeyboardHandles.KeyFHandler()
            
        elif key == 'g' or key == 'G':
        
            self.KeyboardHandles.KeyGHandler()
            
        elif key == 'h' or key == 'H':
        
            self.KeyboardHandles.KeyHHandler()
            
        elif key == 'i' or key == 'I':
        
            self.KeyboardHandles.KeyIHandler()
            
        elif key == 'j' or key == 'J':
        
            self.KeyboardHandles.KeyJHandler()
            
        elif key == 'k' or key == 'K':
        
            self.KeyboardHandles.KeyKHandler()
            
        elif key == 'l' or key == 'L':
        
            self.KeyboardHandles.KeyLHandler()
            
        elif key == 'm' or key == 'M':
        
            self.KeyboardHandles.KeyMHandler()
            
        elif key == 'n' or key == 'N':
        
            self.KeyboardHandles.KeyNHandler()
            
        elif key == 'o' or key == 'O':
        
            self.KeyboardHandles.KeyOHandler()
            
        elif key == 'p' or key == 'P':
        
            self.KeyboardHandles.KeyPHandler()
            
        elif key == 'q' or key == 'Q':
        
            self.KeyboardHandles.KeyQHandler()
            
        elif key == 'r' or key == 'R':
        
            self.KeyboardHandles.KeyRHandler()
            
        elif key == 's' or key == 'S':
        
            self.KeyboardHandles.KeySHandler()
            
        elif key == 't' or key == 'T':
        
            self.KeyboardHandles.KeyTHandler()
            
        elif key == 'u' or key == 'U':
        
            self.KeyboardHandles.KeyUHandler()
            
        elif key == 'v' or key == 'V':
        
            self.KeyboardHandles.KeyVHandler()
            
        elif key == 'w' or key == 'W':
        
            self.KeyboardHandles.KeyWHandler()
            
        elif key == 'x' or key == 'X':
        
            self.KeyboardHandles.KeyXHandler()
            
        elif key == 'y' or key == 'Y':
        
            self.KeyboardHandles.KeyYHandler()
            
        elif key == 'z' or key == 'Z':
        
            self.KeyboardHandles.KeyZHandler()
            
        elif key == keyboard.Key.backspace:
    
            self.KeyboardHandles.KeyBackSpaceHandler()
            
        elif key == keyboard.Key.enter:
        
            self.KeyboardHandles.KeyEnterHandler()
            
        elif key == '0':
            
            self.KeyboardHandles.Key0Handler()
        
        elif key == '1':
            
            self.KeyboardHandles.Key1Handler()
            
        elif key == '2':
            
            self.KeyboardHandles.Key2Handler()
            
        elif key == '3':
            
            self.KeyboardHandles.Key3Handler()
            
        elif key == '4':
            
            self.KeyboardHandles.Key4Handler()
            
        elif key == '5':
            
            self.KeyboardHandles.Key5Handler()
            
        elif key == '6':
            
            self.KeyboardHandles.Key6Handler()
            
        elif key == '7':
            
            self.KeyboardHandles.Key7Handler()
            
        elif key == '8':
            
            self.KeyboardHandles.Key8Handler()
            
        elif key == '9':
            
            self.KeyboardHandles.Key9Handler()
            
        elif key == '(':
            
            self.KeyboardHandles.KeyParenLeftHandler()
            
        elif key == ')':
            
            self.KeyboardHandles.KeyParenRightHandler()
            
        elif key == ',':
            
            self.KeyboardHandles.KeyCommaHandler()
        
        elif key == '+':
            
            self.KeyboardHandles.KeyPlusHandler()
            
        elif key == '-':
            
            self.KeyboardHandles.KeyMinusHandler()
            
        elif key == '*':
            
            self.KeyboardHandles.KeyAsteriskHandler()
            
        elif key == '.':
            
            self.KeyboardHandles.KeyPeriodHandler()
            
# =============================================================================
#         elif key == '/':
#             
#             self.KeyboardHandles.Key key Handler()
# =============================================================================
            
        elif key == ':':
            
            self.KeyboardHandles.KeyColonHandler()
            
        elif key == ';':
            
            self.KeyboardHandles.KeySemicolonHandler()
            
        elif key == '[':
            
            self.KeyboardHandles.BracketLeftHandler()
            
        elif key == ']':
            
            self.KeyboardHandles.BracketRightHandler()
            
        elif key == '=':
            
            self.KeyboardHandles.EqualHandler()
            
        elif key == '>':
            
            self.KeyboardHandles.GreaterHandler()
            
        elif key == '<':
            
            self.KeyboardHandles.LessHandler()
            
# =============================================================================
#         elif key == keyboard.Key.QuoteLeft:
#             
#             self.KeyboardHandles.QuoteLeftHandler()
#             
#         elif key == keyboard.Key.QuoteDbl:
#             
#             self.KeyboardHandles.QuoteDblHandler()
# =============================================================================
            
        elif key == keyboard.Key.page_up:
            
            self.KeyboardHandles.KeyPageUpHandler()
            
        elif key == keyboard.Key.page_down:
            
            self.KeyboardHandles.KeyPageDownHandler()
            
        elif key == keyboard.Key.f1:
            
            self.KeyboardHandles.KeyF1Handler()
            
        elif key == keyboard.Key.f2:
            
            self.KeyboardHandles.KeyF2Handler()
            
        elif key == keyboard.Key.f3:
        
            self.KeyboardHandles.KeyF3Handler()
            
        elif key == keyboard.Key.f4:
        
            self.KeyboardHandles.KeyF4Handler()
            
        elif key == keyboard.Key.f5:
            
            self.KeyboardHandles.KeyF5Handler()
            
        elif key == keyboard.Key.f6:
        
            self.KeyboardHandles.KeyF6Handler()
            
        elif key == keyboard.Key.f7:
            
            self.KeyboardHandles.KeyF7Handler()
            
        elif key == keyboard.Key.f8:
            
            self.KeyboardHandles.KeyF8Handler()
            
        elif key == keyboard.Key.f9:
        
            self.KeyboardHandles.KeyF9Handler()
            
        elif key == keyboard.Key.f10:
            
            self.KeyboardHandles.KeyF10Handler()
            
        elif key == keyboard.Key.f11:
            
            self.KeyboardHandles.KeyF11Handler()
            
        elif key == keyboard.Key.f12:
        
            self.KeyboardHandles.KeyF12Handler()
            
        elif key == keyboard.Key.end:
            
            self.KeyboardHandles.KeyEndHandler()
            
        elif key == keyboard.Key.delete:
        
            self.KeyboardHandles.KeyDeleteHandler()
            
        elif key == keyboard.Key.tab:
            
            self.KeyboardHandles.KeyTabHandler()
            
        elif key == keyboard.Key.shift:
            
            self.KeyboardHandles.KeyShiftHandler()
            
        elif key == keyboard.Key.caps_lock:
            
            self.KeyboardHandles.KeyCapsLockHandler()
            
        #ai generated
# =============================================================================
#         elif key == keyboard.Key.slash:
#             
#             self.KeyboardHandles.KeypadSlashHandler()
#             
#         elif key == keyboard.Key.asterisk:
#             
#             self.KeyboardHandles.KeypadAsteriskHandler()
# =============================================================================
            
        elif key == '-':
            
            self.KeyboardHandles.KeypadMinusHandler()
            
        elif key == '+':

            self.KeyboardHandles.KeypadPlusHandler()
            
        elif key == keyboard.Key.enter:
            
            self.KeyboardHandles.KeypadEnterHandler()

        elif key == '.':
            
            self.KeyboardHandles.KeypadPeriodHandler()
            
# =============================================================================
#         elif key == qc.Qt.Keypad_0:
#             
#             self.KeyboardHandles.Keypad0Handler()
#             
#         elif key == qc.Qt.Keypad_1:
#             
#             self.KeyboardHandles.Keypad1Handler()
#             
#         elif key == qc.Qt.Keypad_2:
#             
#             self.KeyboardHandles.Keypad2Handler()
#             
#         elif key == qc.Qt.Keypad_3:
#             
#             self.KeyboardHandles.Keypad3Handler()
#             
#         elif key == qc.Qt.Keypad_4:
#             
#             self.KeyboardHandles.Keypad4Handler()
#             
#         elif key == qc.Qt.Keypad_5:
#             
#             self.KeyboardHandles.Keypad5Handler()
#             
#         elif key == qc.Qt.Keypad_6:
#         
#             self.KeyboardHandles.Keypad6Handler()
#             
#         elif key == qc.Qt.Keypad_7:
#             
#             self.KeyboardHandles.Keypad7Handler()
#             
#         elif key == qc.Qt.Keypad_8:
#         
#             self.KeyboardHandles.Keypad8Handler()
#             
#         elif key == qc.Qt.Keypad_9:
#             
#             self.KeyboardHandles.Keypad9Handler()
#             
# =============================================================================
# =============================================================================
#             
#         elif key == keyboard.Key.ParenLeft:
#             
#             self.KeyboardHandles.KeypadParenLeftHandler()
#             
#         elif key == keyboard.Key.ParenRight:
#         
#             self.KeyboardHandles.KeypadParenRightHandler()
#             
#         elif key == keyboard.Key.BracketLeft:
#             
#             self.KeyboardHandles.KeypadBracketLeftHandler()
#             
#         elif key == keyboard.Key.BracketRight:
#         
#             self.KeyboardHandles.KeypadBracketRightHandler()
#             
#         elif key == keyboard.Key.BraceLeft:
#             
#             self.KeyboardHandles.KeypadBraceLeftHandler()
#             
#         elif key == keyboard.Key.BraceRight:
#         
#             self.KeyboardHandles.KeypadBraceRightHandler()
#             
#         elif key == keyboard.Key.Bar:
#             
#             self.KeyboardHandles.KeypadBarHandler()
#             
#         elif key == keyboard.Key.Backslash:
#         
#             self.KeyboardHandles.KeypadBackslashHandler()
#             
#         elif key == keyboard.Key.Colon:
#             
#             self.KeyboardHandles.KeypadColonHandler()
#             
#         elif key == keyboard.Key.QuoteDbl:
#         
#             self.KeyboardHandles.KeypadQuoteDblHandler()
#             
#         elif key == keyboard.Key.Apostrophe:
#             
#             self.KeyboardHandles.KeypadApostropheHandler()
#             
#         elif key == keyboard.Key.Less:
#         
#             self.KeyboardHandles.KeypadLessHandler()
#             
#         elif key == keyboard.Key.Greater:
#             
#             self.KeyboardHandles.KeypadGreaterHandler()
#             
#         elif key == keyboard.Key.Question:
#         
#             self.KeyboardHandles.KeypadQuestionHandler()
#             
#         elif key == keyboard.Key.Exclam:
#             
#             self.KeyboardHandles.KeypadExclamHandler()
#             
#         elif key == keyboard.Key.At:
#         
#             self.KeyboardHandles.KeypadAtHandler()
#             
#         elif key == keyboard.Key.NumberSign:
#             
#             self.KeyboardHandles.KeypadNumberSignHandler()
#             
#         elif key == keyboard.Key.Dollar:
#         
#             self.KeyboardHandles.KeypadDollarHandler()
#             
#         elif key == keyboard.Key.Percent:
#             
#             self.KeyboardHandles.KeypadPercentHandler()
#             
#         elif key == keyboard.Key.AsciiCircum:
#         
#             self.KeyboardHandles.KeypadAsciiCircumHandler()
#             
#         elif key == keyboard.Key.Ampersand:
#             
#             self.KeyboardHandles.KeypadAmpersandHandler()
#             
#         elif key == keyboard.Key.Apostrophe:
#         
#             self.KeyboardHandles.KeypadApostropheHandler()
#             
#         elif key == keyboard.Key.AsciiTilde:
#             
#             self.KeyboardHandles.KeypadAsciiTildeHandler()
#             
#         elif key == keyboard.Key.notsign:
#         
#             self.KeyboardHandles.KeypadNotHandler()
#             
#         elif key == keyboard.Key.Bar:
#             
#             self.KeyboardHandles.KeypadBarHandler()
# =============================================================================
            
        elif key == keyboard.Key.ctrl_l:
            pass
# =============================================================================
#             self.controlOn = 1
#             print("control is on")
# =============================================================================
# =============================================================================
#         elif key == keyboard.Key.EuroSign:
#         
#             self.KeyboardHandles.KeypadEuroSignHandler()
#             
#         elif key == keyboard.Key.PoundSign:
#             
#             self.KeyboardHandles.KeypadPoundSignHandler()
#             
#         elif key == keyboard.Key.YenSign:
#         
#             self.KeyboardHandles.KeypadYenSignHandler()
#             
#         elif key == keyboard.Key.Para:
#             
#             self.KeyboardHandles.KeypadParaHandler()
#             
#         elif key == keyboard.Key.SectionSign:
#         
#             self.KeyboardHandles.KeypadSectionSignHandler()
#             
#         elif key == keyboard.Key.CentSign:
#             
#             self.KeyboardHandles.KeypadCentSignHandler()
#             
#         elif key == keyboard.Key.DegreeSign:
#         
#             self.KeyboardHandles.KeypadDegreeSignHandler()
#             
#         elif key == keyboard.Key.PlusMinusSign:
#             
#             self.KeyboardHandles.KeypadPlusMinusSignHandler()
#             
#         elif key == keyboard.Key.MicroSign:
#         
#             self.KeyboardHandles.KeypadMicroSignHandler()
#             
#         elif key == keyboard.Key.RootSign:
#             
#             self.KeyboardHandles.KeypadRootSignHandler()
#             
#         elif key == keyboard.Key.ApproxSign:
#         
#             self.KeyboardHandles.KeypadApproxSignHandler()
#             
#         elif key == keyboard.Key.AcuteAccent:
#             
#             self.KeyboardHandles.KeypadAcuteAccentHandler()
#             
#         elif key == keyboard.Key.AsciiTilde:
#         
#             self.KeyboardHandles.KeypadAsciiTildeHandler()
#             
#         elif key == keyboard.Key.Diaeresis:
#             
#             self.KeyboardHandles.KeypadDiaeresisHandler()
#             
#         elif key == keyboard.Key.CircumflexAccent:
#         
#             self.KeyboardHandles.KeypadCircumflexAccentHandler()
#             
#         elif key == keyboard.Key.GraveAccent:
#             
#             self.KeyboardHandles.KeypadGraveAccentHandler()
#             
#         elif key == keyboard.Key.Apostrophe:
#         
#             self.KeyboardHandles.KeypadApostropheHandler()
#             
#         elif key == keyboard.Key.AsciiCircum:
#             
#             self.KeyboardHandles.KeypadAsciiCircumHandler()
#             
#         elif key == keyboard.Key.Cedilla:
#         
#             self.KeyboardHandles.KeypadCedillaHandler()
#             
#         elif key == keyboard.Key.Hook:
#             
#             self.KeyboardHandles.KeypadHookHandler()
# =============================================================================
            
        else:
            print("no handler for that key")

# =============================================================================
#     def controlPressedHandlers(self, key):
#            if key == keyboard.Key.Space:
#                
#                self.KeyboardHandles.controlKeySpaceHandler()
#                
#            elif key == keyboard.Key.Left:
#                
#                self.KeyboardHandles.controlKeyLeftHandler()
#                
#            elif key == keyboard.Key.Up:
#                
#                self.KeyboardHandles.controlKeyUpHandler()
#            
#            elif key == keyboard.Key.Right:
#            
#                self.KeyboardHandles.controlKeyRightHandler()
#                
#            elif key == keyboard.Key.Down:
#            
#                self.KeyboardHandles.controlKeyDownHandler()
#                
#            elif key == keyboard.Key.A:
#            
#                self.KeyboardHandles.controlKeyAHandler()
#                
#            elif key == keyboard.Key.B:
#            
#                self.KeyboardHandles.controlKeyBHandler()
#                
#            elif key == keyboard.Key.C:
#            
#                self.KeyboardHandles.controlKeyCHandler()
#                
#            elif key == keyboard.Key.D:
#            
#                self.KeyboardHandles.controlKeyDHandler()
#                
#            elif key == keyboard.Key.E:
#            
#                self.KeyboardHandles.controlKeyEHandler()
#                
#            elif key == keyboard.Key.F:
#            
#                self.KeyboardHandles.controlKeyFHandler()
#                
#            elif key == keyboard.Key.G:
#            
#                self.KeyboardHandles.controlKeyGHandler()
#                
#            elif key == keyboard.Key.H:
#            
#                self.KeyboardHandles.controlKeyHHandler()
#                
#            elif key == keyboard.Key.I:
#            
#                self.KeyboardHandles.controlKeyIHandler()
#                
#            elif key == keyboard.Key.J:
#            
#                self.KeyboardHandles.controlKeyJHandler()
#                
#            elif key == keyboard.Key.K:
#            
#                self.KeyboardHandles.controlKeyKHandler()
#                
#            elif key == keyboard.Key.L:
#            
#                self.KeyboardHandles.controlKeyLHandler()
#                
#            elif key == keyboard.Key.M:
#            
#                self.KeyboardHandles.controlKeyMHandler()
#                
#            elif key == keyboard.Key.N:
#            
#                self.KeyboardHandles.controlKeyNHandler()
#                
#            elif key == keyboard.Key.O:
#            
#                self.KeyboardHandles.controlKeyOHandler()
#                
#            elif key == keyboard.Key.P:
#            
#                self.KeyboardHandles.controlKeyPHandler()
#                
#            elif key == keyboard.Key.Q:
#            
#                self.KeyboardHandles.controlKeyQHandler()
#                
#            elif key == keyboard.Key.R:
#            
#                self.KeyboardHandles.controlKeyRHandler()
#                
#            elif key == keyboard.Key.S:
#            
#                self.KeyboardHandles.controlKeySHandler()
#                
#            elif key == keyboard.Key.T:
#            
#                self.KeyboardHandles.controlKeyTHandler()
#                
#            elif key == keyboard.Key.U:
#            
#                self.KeyboardHandles.controlKeyUHandler()
#                
#            elif key == keyboard.Key.V:
#            
#                self.KeyboardHandles.controlKeyVHandler()
#                
#            elif key == keyboard.Key.W:
#            
#                self.KeyboardHandles.controlKeyWHandler()
#                
#            elif key == keyboard.Key.X:
#            
#                self.KeyboardHandles.controlKeyXHandler()
#                
#            elif key == keyboard.Key.Y:
#            
#                self.KeyboardHandles.controlKeyYHandler()
#                
#            elif key == keyboard.Key.Z:
#            
#                self.KeyboardHandles.controlKeyZHandler()
#                
#            elif key == keyboard.Key.Backspace:
#            
#                self.KeyboardHandles.controlKeyBackSpaceHandler()
#                
#            elif key == keyboard.Key.Enter:
#            
#                self.KeyboardHandles.controlKeyEnterHandler()
#                
#            elif key == keyboard.Key.Return:
#            
#                self.KeyboardHandles.controlKeyReturnHandler()
#                
#            elif key == keyboard.Key.0:
#                
#                self.KeyboardHandles.controlKey0Handler()
#            
#            elif key == keyboard.Key.1:
#                
#                self.KeyboardHandles.controlKey1Handler()
#                
#            elif key == keyboard.Key.2:
#                
#                self.KeyboardHandles.controlKey2Handler()
#                
#            elif key == keyboard.Key.3:
#                
#                self.KeyboardHandles.controlKey3Handler()
#                
#            elif key == keyboard.Key.4:
#                
#                self.KeyboardHandles.controlKey4Handler()
#                
#            elif key == keyboard.Key.5:
#                
#                self.KeyboardHandles.controlKey5Handler()
#                
#            elif key == keyboard.Key.6:
#                
#                self.KeyboardHandles.controlKey6Handler()
#                
#            elif key == keyboard.Key.7:
#                
#                self.KeyboardHandles.controlKey7Handler()
#                
#            elif key == keyboard.Key.8:
#                
#                self.KeyboardHandles.controlKey8Handler()
#                
#            elif key == keyboard.Key.9:
#                
#                self.KeyboardHandles.controlKey9Handler()
#                
#            elif key == keyboard.Key.ParenLeft:
#                
#                self.KeyboardHandles.controlKeyParenLeftHandler()
#                
#            elif key == keyboard.Key.ParenRight:
#                
#                self.KeyboardHandles.controlKeyParenRightHandler()
#                
#            elif key == keyboard.Key.Comma:
#                
#                self.KeyboardHandles.controlKeyCommaHandler()
#            
#            elif key == keyboard.Key.Plus:
#                
#                self.KeyboardHandles.controlKeyPlusHandler()
#                
#            elif key == keyboard.Key.Minus:
#                
#                self.KeyboardHandles.controlKeyMinusHandler()
#                
#            elif key == keyboard.Key.Asterisk:
#                
#                self.KeyboardHandles.controlKeyAsteriskHandler()
#                
#            elif key == keyboard.Key.Period:
#                
#                self.KeyboardHandles.controlKeyPeriodHandler()
#                
#            elif key == keyboard.Key.Slash:
#                
#                self.KeyboardHandles.controlKeySlashHandler()
#                
#            elif key == keyboard.Key.Colon:
#                
#                self.KeyboardHandles.controlKeyColonHandler()
#                
#            elif key == keyboard.Key.Semicolon:
#                
#                self.KeyboardHandles.controlKeySemicolonHandler()
#                
#            elif key == keyboard.Key.BracketLeft:
#                
#                self.KeyboardHandles.BracketLeftHandler()
#                
#            elif key == keyboard.Key.BracketRight:
#                
#                self.KeyboardHandles.BracketRightHandler()
#                
#            elif key == keyboard.Key.Equal:
#                
#                self.KeyboardHandles.EqualHandler()
#                
#            elif key == keyboard.Key.Greater:
#                
#                self.KeyboardHandles.GreaterHandler()
#                
#            elif key == keyboard.Key.Less:
#                
#                self.KeyboardHandles.LessHandler()
#                
#            elif key == keyboard.Key.QuoteLeft:
#                
#                self.KeyboardHandles.QuoteLeftHandler()
#                
#            elif key == keyboard.Key.QuoteDbl:
#                
#                self.KeyboardHandles.QuoteDblHandler()
#                
#            elif key == keyboard.Key.PageUp:
#                
#                self.KeyboardHandles.controlKeyPageUpHandler()
#                
#            elif key == keyboard.Key.PageDown:
#                
#                self.KeyboardHandles.controlKeyPageDownHandler()
#                
#            elif key == keyboard.Key.F1:
#                
#                self.KeyboardHandles.controlKeyF1Handler()
#                
#            elif key == keyboard.Key.F2:
#                
#                self.KeyboardHandles.controlKeyF2Handler()
#                
#            elif key == keyboard.Key.F3:
#            
#                self.KeyboardHandles.controlKeyF3Handler()
#                
#            elif key == keyboard.Key.F4:
#            
#                self.KeyboardHandles.controlKeyF4Handler()
#                
#            elif key == keyboard.Key.F5:
#                
#                self.KeyboardHandles.controlKeyF5Handler()
#                
#            elif key == keyboard.Key.F6:
#            
#                self.KeyboardHandles.controlKeyF6Handler()
#                
#            elif key == keyboard.Key.F7:
#                
#                self.KeyboardHandles.controlKeyF7Handler()
#                
#            elif key == keyboard.Key.F8:
#                
#                self.KeyboardHandles.controlKeyF8Handler()
#                
#            elif key == keyboard.Key.F9:
#            
#                self.KeyboardHandles.controlKeyF9Handler()
#                
#            elif key == keyboard.Key.F10:
#                
#                self.KeyboardHandles.controlKeyF10Handler()
#                
#            elif key == keyboard.Key.F11:
#                
#                self.KeyboardHandles.controlKeyF11Handler()
#                
#            elif key == keyboard.Key.F12:
#            
#                self.KeyboardHandles.controlKeyF12Handler()
#                
#            elif key == keyboard.Key.End:
#                
#                self.KeyboardHandles.controlKeyEndHandler()
#                
#            elif key == keyboard.Key.Delete:
#            
#                self.KeyboardHandles.controlKeyDeleteHandler()
#                
#            elif key == keyboard.Key.Tab:
#                
#                self.KeyboardHandles.controlKeyTabHandler()
#                
#            elif key == keyboard.Key.Shift:
#                
#                self.KeyboardHandles.controlKeyShiftHandler()
#                
#            elif key == keyboard.Key.CapsLock:
#                
#                self.KeyboardHandles.controlKeyCapsLockHandler()
#                
#            #ai generated
#            elif key == keyboard.Key.Slash:
#                
#                self.KeyboardHandles.controlKeypadSlashHandler()
#                
#            elif key == keyboard.Key.Asterisk:
#                
#                self.KeyboardHandles.controlKeypadAsteriskHandler()
#                
#            elif key == keyboard.Key.Minus:
#                
#                self.KeyboardHandles.controlKeypadMinusHandler()
#                
#            elif key == keyboard.Key.Plus:
#                
#                self.KeyboardHandles.controlKeypadPlusHandler()
#                
#            elif key == keyboard.Key.Enter:
#                
#                self.KeyboardHandles.controlKeypadEnterHandler()
#                
#            elif key == keyboard.Key.Period:
#                
#                self.KeyboardHandles.controlKeypadPeriodHandler()
#                
#    # =============================================================================
#    #         elif key == qc.Qt.Keypad_0:
#    #             
#    #             self.KeyboardHandles.controlKeypad0Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_1:
#    #             
#    #             self.KeyboardHandles.controlKeypad1Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_2:
#    #             
#    #             self.KeyboardHandles.controlKeypad2Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_3:
#    #             
#    #             self.KeyboardHandles.controlKeypad3Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_4:
#    #             
#    #             self.KeyboardHandles.controlKeypad4Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_5:
#    #             
#    #             self.KeyboardHandles.controlKeypad5Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_6:
#    #         
#    #             self.KeyboardHandles.controlKeypad6Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_7:
#    #             
#    #             self.KeyboardHandles.controlKeypad7Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_8:
#    #         
#    #             self.KeyboardHandles.controlKeypad8Handler()
#    #             
#    #         elif key == qc.Qt.Keypad_9:
#    #             
#    #             self.KeyboardHandles.controlKeypad9Handler()
#    #             
#    # =============================================================================
#                
#            elif key == keyboard.Key.ParenLeft:
#                
#                self.KeyboardHandles.controlKeypadParenLeftHandler()
#                
#            elif key == keyboard.Key.ParenRight:
#            
#                self.KeyboardHandles.controlKeypadParenRightHandler()
#                
#            elif key == keyboard.Key.BracketLeft:
#                
#                self.KeyboardHandles.controlKeypadBracketLeftHandler()
#                
#            elif key == keyboard.Key.BracketRight:
#            
#                self.KeyboardHandles.controlKeypadBracketRightHandler()
#                
#            elif key == keyboard.Key.BraceLeft:
#                
#                self.KeyboardHandles.controlKeypadBraceLeftHandler()
#                
#            elif key == keyboard.Key.BraceRight:
#            
#                self.KeyboardHandles.controlKeypadBraceRightHandler()
#                
#            elif key == keyboard.Key.Bar:
#                
#                self.KeyboardHandles.controlKeypadBarHandler()
#                
#            elif key == keyboard.Key.Backslash:
#            
#                self.KeyboardHandles.controlKeypadBackslashHandler()
#                
#            elif key == keyboard.Key.Colon:
#                
#                self.KeyboardHandles.controlKeypadColonHandler()
#                
#            elif key == keyboard.Key.QuoteDbl:
#            
#                self.KeyboardHandles.controlKeypadQuoteDblHandler()
#                
#            elif key == keyboard.Key.Apostrophe:
#                
#                self.KeyboardHandles.controlKeypadApostropheHandler()
#                
#            elif key == keyboard.Key.Less:
#            
#                self.KeyboardHandles.controlKeypadLessHandler()
#                
#            elif key == keyboard.Key.Greater:
#                
#                self.KeyboardHandles.controlKeypadGreaterHandler()
#                
#            elif key == keyboard.Key.Question:
#            
#                self.KeyboardHandles.controlKeypadQuestionHandler()
#                
#            elif key == keyboard.Key.Exclam:
#                
#                self.KeyboardHandles.controlKeypadExclamHandler()
#                
#            elif key == keyboard.Key.At:
#            
#                self.KeyboardHandles.controlKeypadAtHandler()
#                
#            elif key == keyboard.Key.NumberSign:
#                
#                self.KeyboardHandles.controlKeypadNumberSignHandler()
#                
#            elif key == keyboard.Key.Dollar:
#            
#                self.KeyboardHandles.controlKeypadDollarHandler()
#                
#            elif key == keyboard.Key.Percent:
#                
#                self.KeyboardHandles.controlKeypadPercentHandler()
#                
#            elif key == keyboard.Key.AsciiCircum:
#            
#                self.KeyboardHandles.controlKeypadAsciiCircumHandler()
#                
#            elif key == keyboard.Key.Ampersand:
#                
#                self.KeyboardHandles.controlKeypadAmpersandHandler()
#                
#            elif key == keyboard.Key.Apostrophe:
#            
#                self.KeyboardHandles.controlKeypadApostropheHandler()
#                
#            elif key == keyboard.Key.AsciiTilde:
#                
#                self.KeyboardHandles.controlKeypadAsciiTildeHandler()
#                
#            elif key == keyboard.Key.notsign:
#            
#                self.KeyboardHandles.controlKeypadNotHandler()
#                
#            elif key == keyboard.Key.Bar:
#                
#                self.KeyboardHandles.controlKeypadBarHandler()
#                
#            elif key == keyboard.Key.Control:
#                
#                self.controlOn = 1
#                print("control is on")
#    # =============================================================================
#    #         elif key == keyboard.Key.EuroSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadEuroSignHandler()
#    #             
#    #         elif key == keyboard.Key.PoundSign:
#    #             
#    #             self.KeyboardHandles.controlKeypadPoundSignHandler()
#    #             
#    #         elif key == keyboard.Key.YenSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadYenSignHandler()
#    #             
#    #         elif key == keyboard.Key.Para:
#    #             
#    #             self.KeyboardHandles.controlKeypadParaHandler()
#    #             
#    #         elif key == keyboard.Key.SectionSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadSectionSignHandler()
#    #             
#    #         elif key == keyboard.Key.CentSign:
#    #             
#    #             self.KeyboardHandles.controlKeypadCentSignHandler()
#    #             
#    #         elif key == keyboard.Key.DegreeSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadDegreeSignHandler()
#    #             
#    #         elif key == keyboard.Key.PlusMinusSign:
#    #             
#    #             self.KeyboardHandles.controlKeypadPlusMinusSignHandler()
#    #             
#    #         elif key == keyboard.Key.MicroSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadMicroSignHandler()
#    #             
#    #         elif key == keyboard.Key.RootSign:
#    #             
#    #             self.KeyboardHandles.controlKeypadRootSignHandler()
#    #             
#    #         elif key == keyboard.Key.ApproxSign:
#    #         
#    #             self.KeyboardHandles.controlKeypadApproxSignHandler()
#    #             
#    #         elif key == keyboard.Key.AcuteAccent:
#    #             
#    #             self.KeyboardHandles.controlKeypadAcuteAccentHandler()
#    #             
#    #         elif key == keyboard.Key.AsciiTilde:
#    #         
#    #             self.KeyboardHandles.controlKeypadAsciiTildeHandler()
#    #             
#    #         elif key == keyboard.Key.Diaeresis:
#    #             
#    #             self.KeyboardHandles.controlKeypadDiaeresisHandler()
#    #             
#    #         elif key == keyboard.Key.CircumflexAccent:
#    #         
#    #             self.KeyboardHandles.controlKeypadCircumflexAccentHandler()
#    #             
#    #         elif key == keyboard.Key.GraveAccent:
#    #             
#    #             self.KeyboardHandles.controlKeypadGraveAccentHandler()
#    #             
#    #         elif key == keyboard.Key.Apostrophe:
#    #         
#    #             self.KeyboardHandles.controlKeypadApostropheHandler()
#    #             
#    #         elif key == keyboard.Key.AsciiCircum:
#    #             
#    #             self.KeyboardHandles.controlKeypadAsciiCircumHandler()
#    #             
#    #         elif key == keyboard.Key.Cedilla:
#    #         
#    #             self.KeyboardHandles.controlKeypadCedillaHandler()
#    #             
#    #         elif key == keyboard.Key.Hook:
#    #             
#    #             self.KeyboardHandles.controlKeypadHookHandler()
#    # =============================================================================
#                
#            else:
#                print("no handler for that key")
#     
#         
# =============================================================================

    def handleKeyReleaseEvent(self, key):
        pass
# =============================================================================
#         #key = keyReleaseEvent.key()
#         if key == keyboard.Key.ctrl_l:
#             self.controlOn = 0
#             print("control is off")
# 
# =============================================================================
