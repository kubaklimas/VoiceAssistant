from gtts import gTTS
import os
import datetime
import playsound

def speak(text):
    x = datetime.datetime.now()
    a = x.strftime("%d-%b-%Y-%H-%M-%S")
    
    tts = gTTS(text=text, lang='en')
    #filename = a+'.mp3'
    filename = "bye.mp3"
    tts.save(filename)
    playsound.playsound(filename)
      
speak('see ya')