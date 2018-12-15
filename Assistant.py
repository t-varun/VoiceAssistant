from colorama import init
from termcolor import colored
import speech_recognition as sr
import os
import ctypes
from googlesearch import search
import webbrowser
import pyttsx3
import win32api
import cv2
import sys

r = sr.Recognizer()
m = sr.Microphone()
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
engine = pyttsx3.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
print("Hi, I am your Assistant. How can I help you?")
engine.say('Hi, I am your Assistant. How can I help you?')
engine.runAndWait()
while(True):
    with m as source:
        r.adjust_for_ambient_noise(source)
        format(r.energy_threshold)
        with sr.Microphone() as source:
            print("Speak now:")
            audio = r.listen(source)
    try:
        init()
        Aud = r.recognize_google(audio)
        print("TEXT :"+Aud)
        X = Aud
        X = X.split(" ")
        if(Aud == "open jupyter notebook"):
            print("Opening Jupyter Notebook")
            engine.say("Opening Jupyter Notebook")
            engine.runAndWait()
            os.system("E:/Work/JupyterNotebook.bat")
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif(Aud == "open camera"):
            print("Opening Camera...")
            engine.say("Opening Camera...")
            engine.runAndWait()
            while(True):
                ret, frame = video_capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            video_capture.release()
            cv2.destroyAllWindows()
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif((Aud == "open Chrome")|(Aud == "open Google Chrome")|(Aud == "open browser")|(Aud == "please open Chrome")|(Aud == "please open Google Chrome")):
            print("Opening Google Chrome")
            engine.say("Opening Google Chrome")
            engine.runAndWait()
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.co.in/")
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif((Aud == "what is your age")|(Aud == "how old are you")):
            print("I am old enough to assist you..!")
            engine.say("I am old enough to assist you..!")
            engine.runAndWait()
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif((Aud == "how are you")|(Aud == "how do you do")):
            print("I am doing great, Thanks.\nWhat about you..?")
            engine.say("I am doing great, Thanks. What about you..?")
            engine.runAndWait()
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif((Aud == "what is your name")|(Aud == "who are you")):
            print("I am your Assistant, I can run many applications in your pc and I can search anything in Google.")
            engine.say("I am your Assistant, I can run many applications in your pc and I can search anything in Google.")
            engine.runAndWait()
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif((Aud == "what can you do")|(Aud == "how can you help me")|(Aud == "what can you do for me")):
            print("I can run many applications in your pc and I can search anything in Google.")
            engine.say("I can run many applications in your pc and I can search anything in Google.")
            engine.runAndWait()
            print("How can I help you?")
        elif((Aud == "quit")|(Aud == "close")|(Aud == "exit")):
            print("I am sleeping now...bye.")
            engine.say("I am sleeping now...bye.")
            engine.runAndWait()
            exit()
        elif((X[0] == "play")|(Aud == "open YouTube")):
            if (Aud == "open YouTube"):
                print("Opening YouTube...")
                engine.say("Opening YouTube...")
                engine.runAndWait()
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/")
            else:
                print("Playing "+X[1]+"...")
                engine.say("Playing "+X[1]+"...")
                engine.runAndWait()
                webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.youtube.com/results?search_query="+X[1])
        elif(Aud == "open text files"):
            print("Searching in PC...")
            engine.say("Searching in PC...")
            engine.runAndWait()
            for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
                dir_path = drive
            for root, dirs, files in os.walk(dir_path):
                for file in files: 
                    if file.endswith('.txt'):
                        print(root+'/'+str(file))
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif(X[0] == "open"):
            print("Opening "+X[1]+"...")
            engine.say("Opening "+X[1]+"...")
            engine.runAndWait()
            X[1] = X[1].lower()
            Y = (X[1]+".exe")
            os.system(Y)
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        elif(X[0] == "please"):
            print("Opening "+X[2]+"...")
            engine.say("Opening "+X[2]+"...")
            engine.runAndWait()
            X[2] = X[2].lower()
            Y = (X[2]+".exe")
            os.system(Y)
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()
        else:
            #ctypes.windll.user32.MessageBoxW(0, "Command Not found..! Searching through google", "Alert", 1)
            print("Searching through google...")
            engine.say("Searching through google...")
            engine.runAndWait()
            f = open('E:/VaruN/Automation/Data.txt','a')
            f.write(Aud + '\n')
            f.close()
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.co.in/search?q="+Aud)
            #for i in search(Aud, tld="com", num=2, stop=1, pause=2):
            #    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(i)
            print("How can I help you?")
            engine.say("How can I help you?")
            engine.runAndWait()

    except:
        pass
engine.stop()
