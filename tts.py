import pyttsx3
from multiprocessing import Process
engine = pyttsx3.init()

def ttsSay(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def speak(text):
    p = Process(target=ttsSay,args=(text,))
    p.start()
    p.join()
