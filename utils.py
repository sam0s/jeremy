#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import tts
from datetime import datetime
import requests
import json

#weather api key :)
from credentz import *
base_url = 'http://api.openweathermap.org/data/2.5/weather?'


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
