# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:26:44 2023

@author: Derek Joslin

"""

import requests
import pyaudio
from io import BytesIO
from pydub import AudioSegment

class VoiceSynthesizer():
    
    def __init__(self, apiKey):
        # initialize the api key
        self.headers = {
            "accept": "audio/mpeg",
            "xi-api-key": apiKey,
            "Content-Type": "application/json",
        }

        self.url = 'https://api.elevenlabs.io/v1/text-to-speech/C0XKHcz5YQ00cz0PkFtl'
        
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
        audio_content = BytesIO(self.audioBytes)
        audio = AudioSegment.from_file(audio_content, format="mp3")
            
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(audio.sample_width),
                        channels=audio.channels,
                        rate=audio.frame_rate,
                        output=True)
        stream.write(audio.raw_data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        
    def saveMp3(self):
        with open('output.mp3', 'wb') as f:
            f.write(self.audioBytes)
