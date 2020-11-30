import pyttsx3
from multiprocessing import Process
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def aspeak(text):
    p = Process(target=ttsSay,args=(text,))
    p.start()
    p.join()
