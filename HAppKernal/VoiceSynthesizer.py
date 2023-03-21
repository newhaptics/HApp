# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:26:44 2023

@author: Derek Joslin

"""

import requests
import pygame
import io

class VoiceSynthesizer():

    def __init__(self, apiKey):
        # initialize the api key
        self.headers = {
            "accept": "audio/mpeg",
            "xi-api-key": apiKey,
            "Content-Type": "application/json",
        }

        self.url = 'https://api.elevenlabs.io/v1/text-to-speech/C0XKHcz5YQ00cz0PkFtl'

        pygame.mixer.init()

    def synthVoice(self, voiceString):
        data = {
          "text": voiceString,
          "voice_id": "C0XKHcz5YQ00cz0PkFtl",
          "voice_settings": {
            "stability": 0.25,
            "similarity_boost": 0.9
          }
        }

        response = requests.post(self.url, headers=self.headers, json=data)

        self.audioBytes = response.content

    def playSound(self):
        audioBuffer = io.BytesIO(self.audioBytes)
        pygame.mixer.music.load(audioBuffer)
        pygame.mixer.music.play()
        
    def saveMp3(self):
        with open('output.mp3', 'wb') as f:
            f.write(self.audioBytes)
