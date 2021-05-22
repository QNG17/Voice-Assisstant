import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import cv
from gtts import gTTS
import playsound
import bs4
import smtplib


#print('Loading your AI personal assistant - Eve')

#engine = pyttsx3.init('sapi5')

#rate=engine.getProperty('rate')
#engine.setProperty('rate', 170)

#voices = engine.getProperty('voices')
#engine.setProperty('voice','voices[0].id')
#engine.setProperty('voice', voices[1].id)

def speak(String):
    #engine.say(text)
    #engine.runAndWait()
    tts = gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning Tyler")
        #print("Hello, Good Morning Tyler")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon Tyler")
        #print("Hello, Good Afternoon Tyler")
    else:
        speak("Hello, Good Evening Tyler")
        #print("Hello, Good Evening Tyler")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source, phrase_time_limit = 20)

        try:
            statement=r.recognize_google(audio,language='en-US')
            print(f"user said:{statement}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your personal assistant Eve")
wishMe()


if __name__=='__main__':


    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "goodbye" in statement or "goodbye Eve" in statement or "bye" in statement:
            speak('Shutting down. Have a nice day')
            print('Shutting down. Have a nice day')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            speak("According to Wikipedia") 
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stackoverflow. Have fun coding")
            time.sleep(5)

        elif 'look for computer parts' in statement:
            webbrowser.open_new_tab("https://www.newegg.com/")
            speak('Looks like there are deals')
            time.sleep(5)

        elif 'amazon' in statement or 'open amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com/ref=nav_logo")
            speak('Opening amazon.com now')
            time.sleep(5)

        elif 'ebay' in statement or 'open ebay' in statement:
            webbrowser.open_new_tab("https://www.ebay.com/")
            speak('Opening ebay.com now')
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url) 
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature is " +
                      str(current_temperature) +
                      "\n humidity is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                #print(" Temperature = " +
                      #str(current_temperature) +
                      #"\n humidity (in percentage) = " +
                      #str(current_humidiy) +
                      #"\n description = " +
                      #str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement or 'what is the current time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M %p")
            speak(f"the time is {strTime}")
        
        elif "what is your name" in statement or "who are you" in statement:
            speak('My name is Eve.')

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am programmed to do minor tasks like:'
                  'opening youtube, google chrome, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather' 
                  'in different cities, and you can ask me computational or geographical questions too!')
            time.sleep(5)

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Tyler")
            print("I was built by Tyler")


        #elif "camera" in statement or "take a photo" in statement:
            #ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)

        elif 'calculate' in statement or 'look this up' in statement:
            app_id = "3KQ33Q-GAWEHVL7TA"
            client = wolframalpha.Client('3KQ33Q-GAWEHVL7TA')
            question = takeCommand()
            speak("Please give me a moment")
            res = client.query(question)
            if res['@success']=='true':
                pod0=res['pod'][0]['subpod']['plaintext']
                print(pod0)
                pod1=res['pod'][1]
                if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                    result = pod1['subpod']['plaintext']
                speak("The answer is " + result)
                print(result)
            else:
                print("No answer returned")
            time.sleep(5)

        elif 'find location' in statement:
            location = statement
            speak("What is the location?")
            location = takeCommand()
            webbrowser.open_new_tab("https://www.google.com/maps/place/" + location + " ")
            speak("Here is the location of " + location)
            time.sleep(5)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your pc will log off in 10 second. Make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
