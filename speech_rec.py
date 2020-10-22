import speech_recognition as sr
import reply_voice as reply
import time


while True:   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="pl-PL")
            print("You said : {}".format(text))
            reply.speak(text)
            time.sleep(6)
        except:
            reply.speak("Nie rozumiem co powiedziałes")


