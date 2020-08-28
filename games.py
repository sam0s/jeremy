import random
import tts

def dice(num):
    x=random.randint(1,num)
    tts.speak("You rolled, "+str(x))
