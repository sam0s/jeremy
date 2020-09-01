import tts,games
import speech_recognition as sr
from re import sub

wft=0
run=True

def process_text(msg):
    global wft
    global run
    omsg=msg
    msg=msg.split(" ")
    if wft == 1:
        if "dice" in msg:
            games.dice(6)
        if "how are you" in omsg:
            tts.speak("I'm ok bro. What about yourself big fella.")
        if "repeat me" in omsg:
            s=omsg.replace("repeat me","",1)
            tts.speak(s)
        if "shut down" in omsg:
            run = False
        print(msg)
        wft=0
    if msg[0] == "jeremy" and wft==0:
        wft = 1
        tts.speak("Yes, what do you need?")


#listener.energy_threshold()
def mainLoop():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,3)
    print(r.energy_threshold)
    #r.energy_threshold=40
    print("j-init")
    while(run):
        try:
            with sr.Microphone() as source2:
                audio2 = r.listen(source2)
                print("heard you, light: "+str(wft))
                if wft==1:
                    text = r.recognize_wit(audio2,key="JE7HXDQLPQ3JIO7CX6KU7QOFIPRAAEVA")
                else:
                    text = r.recognize_sphinx(audio2)
                text = text.lower()
                print("I heard: "+text)
                if(len(text)>1):
                    process_text(text)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("no words detected")

    listener(False)

if __name__ == '__main__':
    mainLoop()
