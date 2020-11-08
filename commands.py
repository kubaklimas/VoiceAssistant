import speech_recognition as sr
import reply_voice as reply
import datetime




def whatday():
    x = datetime.datetime.now()
    dayname = x.strftime("%A")
    wholereply = "Today is"+dayname
    reply.speak(wholereply)


def whatdate():
    today = datetime.date.today()
    d = today.strftime("%d %B %Y")
    wholereply = "Today is"+d
    reply.speak(wholereply)


