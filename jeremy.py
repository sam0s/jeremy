from multiprocessing import Process

import speech_recognition as sr

wft=0
run=True

def momkey():
    print("momkey"*10)

def process_text(msg):
    global wft
    global run
    msg=msg.split(" ")
    if wft == 1:
        if msg[0]=="quit":
            run = False
        if msg[0]=="monkey":
            p = Process(target=momkey,args=())
            p.start()
            p.join()
        print(msg)
        wft=0
    if msg[0] == "Jeremy" and wft==0:
        wft = 1
        print("Jeremy: Yeah, what you need?")
        
            

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


r = sr.Recognizer()
m = sr.Microphone()

with m as source:
   r.adjust_for_ambient_noise(source)  
listener = r.listen_in_background(m, heard)

def mainLoop():
    while(run):
        pass
    #close the listener
    listener(False)

if __name__ == '__main__':
    mainLoop()

    
