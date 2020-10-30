#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import tts
import feedparser
from datetime import datetime
import requests
import json
import speech_recognition as sr

#weather api key :)
from credentz import *
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def greeting():
    now = datetime.now()
    a,b=now.strftime("%H"),now.strftime("%p")
    if b=="AM" and int(a)<12:
        tts.speak("Good moring friend")
        return
    if b=="PM" and int(a)>6:
        tts.speak("Good evening friend")
        return
    tts.speak("Good afternoon friend")
    return


def dice(num):
    x = random.randint(1, num)
    tts.speak('You rolled, ' + str(x))


def time():
    now = datetime.now()
    current_time = now.strftime('It is currently %H:%M %p')
    tts.speak(current_time)


def weather():
    city_name = 'Boiling Springs'

    complete_url = base_url + 'appid=' + wapi_key + '&q=' + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x['cod'] != '404':
        current_temperature = int((float(x['main']['temp'])*9/5)-459.67)
        z = x['weather']
        wd = z[0]['description']
        desc="Currently it is "+wd+", and the temperature is "+str(current_temperature)+" degrees Fahrenheit"
        tts.speak(desc)
    else:
        print (' City Not Found ')

def ask(q):
    if q=="continue":
        tts.speak("Keep going?")
        ans = ""
        while ans=="":
            a=getYesNoOk()
            if a=="yes":
                return True
            if a=="no":
                return False
    return False

def news():
    a = feedparser.parse("http://rss.cnn.com/rss/cnn_latest.rss")
    d = a.entries
    headlines = [i['title'] for i in d]
    print(headlines)
    for i in headlines:
        tts.speak(i)
        if ask("continue")==False:
            break


def getYesNoOk():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,3)
        nn=sr.Microphone.list_microphone_names()
        while(True):
            try:
                with sr.Microphone() as source2:
                    audio2 = r.listen(source2)
                    text = r.recognize_sphinx(audio2)
                    text = text.lower()
                    print("I heard: "+text)
                    if(len(text)>1):
                        if "yes" in text:
                            return "yes"
                        if "no" in text:
                            return "no"
                        if "ok" in text:
                            return "ok"
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
            except sr.UnknownValueError:
                print("no words detected")
