import speech_recognition as sr
import reply_voice as reply
import time

'''
while True:   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="en-EN")
            print("You said : {}".format(text))
            reply.speak(text)
            time.sleep(5)
        except:
            reply.speak("I do not understand")
'''
def rec_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="en-EN")
            print("You said : {}".format(text))
            return text
            
        except:
            print('I did not recognize')
            #reply.speak("I do not understand")
