#!/usr/bin/env python
import pyttsx3
from multiprocessing import Process
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
