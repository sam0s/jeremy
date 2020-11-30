import tts,utils
import speech_recognition as sr
from gpiozero import LED
from re import sub
greetings = ["how are you", "what's up", "are you doing","it going","you been"]
l1 = LED(17)
l2 = LED(18)
l2.on()
def process_text(msg):
    global wft
    global run
    omsg=msg
    msg=msg.split(" ")
    if wft == 1:
        if "news" in omsg:
            utils.news()
        elif "repeat me" in omsg:
            s=omsg.replace("repeat me","",1)
            tts.speak(s)
        elif "weather" in msg:
            utils.weather()
        elif "dice" in msg:
            utils.dice(6)
        elif "time is it" in omsg or "the time" in omsg:
            utils.time()
        elif any(greeting in omsg for greeting in greetings):
            utils.greeting()
        elif "shut down" in omsg:
            run = False
        print(msg)
        wft=0
        l1.off()
        l2.on()
    if "jeremy" in msg[0] or "tyranny" in msg[0] and wft==0:
        wft = 1
        l1.on()
        l2.off()
        tts.speak("Yes, what do you need?")


#listener.energy_threshold()
def mainLoop():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,6)
    print(r.energy_threshold)
    #r.energy_threshold=40
    nn=sr.Microphone.list_microphone_names()
    print("j-init",nn)
    while(run):
        try:
            with sr.Microphone() as source2:
                audio2 = r.listen(source2,timeout=1)
                print("heard you, light: "+str(wft))
                if wft==1:
                    text = r.recognize_wit(audio2,key="JE7HXDQLPQ3JIO7CX6KU7QOFIPRAAEVA")
                else:
#                    text = r.recognize_wit(audio2,key="JE7HXDQLPQ3JIO7CX6KU7QOFIPRAAEVA")
                    text = r.recognize_sphinx(audio2)
                text = text.lower()
                print("I heard: "+text)
                if(len(text)>1):
                    process_text(text)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("no words detected")
        except:
            print("oops")

if __name__ == '__main__':
    wft=0
    run=True
    mainLoop()
