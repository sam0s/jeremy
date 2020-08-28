import tts,games
import speech_recognition as sr

wft=0
run=True

def process_text(msg):
    global wft
    global run
    msg=msg.split(" ")
    if wft == 1:
        if "dice" in msg:
            dice(6)
        if msg[0]=="quit":
            run = False
        print(msg)
        wft=0
    if msg[0] == "Jeremy" and wft==0:
        wft = 1
        speak("Yes, what do you need?")



def heard(recognizer, audio):
    print("heard you, light: "+str(wft))
    try:
        text = recognizer.recognize_google(audio)
        process_text(text)
    except sr.UnknownValueError:
        pass
        #no need to tell the user, just means we heard gibberish or noise
    except sr.RequestError as e:
        #
        print("request error; {0}".format(e))

#listener.energy_threshold()
def mainLoop():
    while(run):
        pass
    #close the listener
    listener(False)
    engine.stop()

if __name__ == '__main__':

    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
       r.adjust_for_ambient_noise(source,2)
    print(r.energy_threshold)
    r.energy_threshold=16
    listener = r.listen_in_background(m, heard)
    games.dice(12)
    mainLoop()
