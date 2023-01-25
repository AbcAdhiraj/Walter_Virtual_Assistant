import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import sys
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
import requests
import pywikihow
import random
import cv2
import numpy as np
import pyautogui
import operator
import psutil
import datetime
from psutil._common import BatteryTime
        

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    speak("I am Alex Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Just a minute...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Please Repeat...")
        return "None"
    return query


    


       
        
        
if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif " temperature" in query:
            search = "What's the weather"
            speak("checking the weather")
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search}is {temp}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
           
            webbrowser.open(f"{cm}")
            speak("searching"f"{cm}")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'play music' in query:
            speak("playing music")
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
       

        elif " internet speed" in query:
            import speedtest
            # st = speedtest.Speedtest()
            # dl = st.download()
            # up = st.upload()
            # speak(f"sir , the downloading speed is {dl} per seconds and the uploading speed is {up}per seconds") 
            
            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")
                
                  
        elif "sleep" in query or "stop" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()
        
        

        elif "nice" in query:
            speak("Thank You Sir")

        elif "pause" in query:
            pyautogui.press("k")
            speak('video paused')

        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning Volume Up")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning Volume down")
            volumedown()
        elif "poem" in query:
            speak("Twinkle Twinkle Little star,How I Wonder What You Are, Up Above The World So High , like A Diamond In The Sky")

        elif "play" in query:
            pyautogui.press("k")
            speak("video played")

        elif "mute" in query:
            pyautogui.press("m")
            speak("video mute")

        elif " teach me mode" in query:
            from pywikihow import search_wikihow
            speak("activating teach me mode, please tell me what you want to learn")
            how = takeCommand()
            try:
                if "exit" in how or "close" in how:
                    speak("okay sir, teach me mode is closed")
                    break
                else:
                    max_results = 1
                    how_to = search_wikihow(how, max_results)
                    assert len(how_to) == 1
                    how_to[0].print()
                    speak(how_to[0].summary)
            except Exception as e:
                speak("sorry , i don't know that one")

            # def alarm(query):
            #     timehere = open("alarm.txt", "a")
            #     timehere.write(query)
            #     timehere.close()
            #     os.startfile("alarm.py")

        elif " location" in query or "where am i" in query:
            speak("wait sir, let me check")
            loc = Nominatim(user_agent="GetLoc")
            getLoc = loc.geocode("Mahmoorganj")
            print(getLoc.address)
            print("Latitude = ", getLoc.latitude, "\n")
            print("Longitude = ", getLoc.longitude)
            speak(getLoc.address)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)
        elif "battery" in query or "power left" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system has {percentage} percent battery")
            if percentage>=75:
                speak("Enough power to continue")
            elif percentage>=40 and percentage<=75:
                speak("you can connect power but will work otherwise aswell")
            elif percentage<=15 and percentage<=30:
                speak("you should connect to power")
            elif percentage<=15:
                speak,("the system may shutdown")
       
