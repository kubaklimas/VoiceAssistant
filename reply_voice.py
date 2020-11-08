#import speech_recognition as sr
from gtts import gTTS
import os
#import time
import playsound

def speak(text):
    if os.path.exists("voice.mp3"):
      os.remove('voice.mp3')
    else:
      #print("Plik dźwiekowy nie istnieje")
      tts = gTTS(text=text, lang='en')
      filename = 'voice.mp3'
      tts.save(filename)
      playsound.playsound(filename)
      
