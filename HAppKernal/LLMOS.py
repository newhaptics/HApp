# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:21:03 2023

@author: Derek Joslin

"""

import Imprint as im
import VoiceSynthesizer as vs

class LLMOS(im.Imprint):
    
    def __init__(self, openAIKey, elevenLabsKey):
        # create the imprint of llmOS
        super().__init__(openAIKey, "C://Users//derek//Documents//HApp//HAppKernal//gnomes//LLMOS.gnome")
        
        # create the cave johnson voice
        self.Voice = vs.VoiceSynthesizer(elevenLabsKey)
        
    def speakCommand(self, command):
        self.openGnome("Start Rom")
        genericResponse = self.generateResponse(command)
        genericResponse = self.decodeResponse()
        
        # turn the response into Cave Johnson
        self.openGnome("Cave Johnson")
        
        userString = "User-" + command
        AIString = "AI assistant-" + genericResponse[1]
        
        voiceResponse = self.generateResponse(userString + "\n" + AIString)
                
        self.Voice.synthVoice(voiceResponse)
        self.Voice.playSound()
        
        return genericResponse, voiceResponse