# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:53:58 2023

@author: Derek Joslin

"""

import openai
import GnomeInterpreter

class Imprint():

    def __init__(self, key, gnomePath):
        # create the operating system for the HApp
        
        # store the api key
        self.apiKey = key
        openai.api_key = self.apiKey
        
        # Create the Gnome intrepreter
        self.Gnomes = GnomeInterpreter.GnomeInterpreter(gnomePath)
        
        self.gnomeList = self.Gnomes.getGnomeKeys()
        
        # current gnome
        self.gnome = []
        
        # save the encoded response from llmOS
        self.encodedResponse = ""
        
    def openGnome(self, gnomeKey):
        self.gnome = self.Gnomes[gnomeKey]
        
    def generateResponse(self, prompt):
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages = [
                {"role": "system", "content": self.gnome[0]},
                {"role": "user", "content": self.gnome[1]},
                {"role": "assistant", "content": self.gnome[2]},
                {"role": "user", "content": prompt}
            ]
        )
    
        self.encodedResponse = response.choices[0].message.content
        return self.encodedResponse

    def decodeResponse(self):
        # decode the response to find the application to start
        
        if "$" in self.encodedResponse:
            applicationString = self.encodedResponse.split("$")[1]
            commentString = self.encodedResponse.split("@")[1]
        else:
            applicationString = ""
            commentString = self.encodedResponse
            
        return applicationString, commentString
    
# =============================================================================
# systemPrompt = """You are an operating system named llmOS. Your sole job is to determine based on user questions which of the installed applications to start. These are the rules you follow:
# -Refer to the list of installed applications (commonly referred to as roms) to help you remember which applications to start. 
# -When starting an application use the start application template to create the start prompt and provide a comment. 
# -If the user asks a question that is not starting an application provide a helpful response asking the user to start an installed application and list them.
# -If you would suggest starting a specific application just start the application.
# installed applications START
# 1. Slides
# 2. Notepad
# 3. Avalanche
# 4. Pong
# 5. TouchTunes
# installed applications END
# start application template START
# $<application>$ started
# @<llmOS comment>@
# start application template END
# Be as helpful as possible."""
# 
# intialQuery = """I'd like to start notepad rom"""
# 
# intialResponse = """$Notepad$ started
# @Alright I'm starting Notepad.@"""
# 
# 
# UserQuery = "Let me play pong."
# 
# Cave = LLMOS(key, systemPrompt, intialQuery, intialResponse)
# 
# Cave.generateResponse(UserQuery)
# 
# print(Cave.decodeResponse())
# =============================================================================
