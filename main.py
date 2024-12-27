import json
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr 
from datetime import datetime
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random  
import numpy as np
import psutil
import subprocess

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer=pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder=pickle.load(encoder_file)

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...", end="", flush=True)
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        audio = r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("Recognizing.......", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print("\r", end="", flush=True)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def cal_day():
    day = datetime.now().weekday() + 1
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def wishMe():
    hour = int(datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()
    if (hour>=0) and (hour<=12) and ('AM' in t):
        speak(f"Good Morning Manish! It's {t} on {day}")
    elif (hour>=12) and (hour<=17) and ('PM' in t):
        speak(f"Good Afternoon Manish! It's {t} on {day}")
    else:
        speak(f"Good Evening Manish! It's {t} on {day}")

def open_social_media():
    if 'open facebook' in command:
        speak("Opening your Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif 'open instagram' in command:
        speak("Opening your instagram")
        webbrowser.open("https://www.instagram.com/")
    elif 'open linkedin' in command:
        speak("Opening your linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif 'open twitter' in command:
        speak("Opening your twitter")
        webbrowser.open("https://www.twitter.com/")
    elif 'open whatsapp' in command:
        speak("opening your whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'open github' in command:
        speak("opening your github")
        webbrowser.open("https://github.com")
    else:
        speak("Sorry, I can't open the platform")

def close_social_media():
    platforms = ["facebook", "instagram", "linkedin", "twitter", "whatsapp", "github"]
    closed_any = False
    for platform in platforms:
        if platform in command:
            closed_any = True
            speak(f"Closing {platform}")
            os.system(f"taskkill /f /im chrome.exe")  # Replace 'chrome.exe' with the browser process if you're not using Chrome
            break
    if not closed_any:
        speak("Sorry, I can't find any social media platform to close.")

def schedule():
    day = cal_day().lower()
    speak("Boss today's schedule is ")
    week={
    "monday": "Boss, from 9:00 to 9:50 you have Algorithms class, from 10:00 to 11:50 you have System Design class, from 12:00 to 2:00 you have a break, and today you have Programming Lab from 2:00 onwards.",
    "tuesday": "Boss, from 9:00 to 9:50 you have Web Development class, from 10:00 to 10:50 you have a break, from 11:00 to 12:50 you have Database Systems class, from 1:00 to 2:00 you have a break, and today you have Open Source Projects lab from 2:00 onwards.",
    "wednesday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Machine Learning class, from 11:00 to 11:50 you have Operating Systems class, from 12:00 to 12:50 you have Ethics in Technology class, from 1:00 to 2:00 you have a break, and today you have Software Engineering workshop from 2:00 onwards.",
    "thursday": "Boss, today you have a full day of classes. From 9:00 to 10:50 you have Computer Networks class, from 11:00 to 12:50 you have Cloud Computing class, from 1:00 to 2:00 you have a break, and today you have Cybersecurity lab from 2:00 onwards.",
    "friday": "Boss, today you have a full day of classes. From 9:00 to 9:50 you have Artificial Intelligence class, from 10:00 to 10:50 you have Advanced Programming class, from 11:00 to 12:50 you have UI/UX Design class, from 1:00 to 2:00 you have a break, and today you have Capstone Project work from 2:00 onwards.",
    "saturday": "Boss, today you have a more relaxed day. From 9:00 to 11:50 you have team meetings for your Capstone Project, from 12:00 to 12:50 you have Innovation and Entrepreneurship class, from 1:00 to 2:00 you have a break, and today you have extra time to work on personal development and coding practice from 2:00 onwards.",
    "sunday": "Boss, today is a holiday, but keep an eye on upcoming deadlines and use this time to catch up on any reading or project work."
    }
    if day in week.keys():
        speak(week[day])

def openApp(command):
    if "open calculator" in command:
        speak("Opening calculator")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    elif "open notepad" in command:
        speak("Opening notepad")
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    elif "open paint" in command:
        speak("Opening paint")
        subprocess.Popen('C:\\Users\\user\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe')
    else:
        speak("Sorry, I can't open this app..")

def closeApp(command):
    if "close calculator" in command:
        speak("Closing calculator")
        os.system("taskkill /f /im calc.exe")
    elif "close notepad" in command:
        speak("Closing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif "close paint" in command:
        speak("Closing paint")
        os.system("taskkill /f /im mspaint.exe")

def open_browsing(query):
    if 'open google' in query:
        speak("Boss, what should i search on google..")
        s = command().lower()
        webbrowser.open(f"{s}")
    elif 'open youtube' in query:
        speak("Boss, what should i search on youtube..")
        s = command().lower()
        webbrowser.open(f"https://www.youtube.com/results?search_query={s}")
    elif 'open edge' in query:
        speak("Boss, what should i search on edge..")
        s = command().lower()
        webbrowser.open(f"https://www.bing.com/search?q={s}")
    elif 'open website' in query or 'visit site' in query or 'go to' in query:
        speak("Which website should I open, boss?")
        site = command().lower()   
        # Remove common phrases that users might say
        site = site.replace('open', '').replace('website', '').replace('go to', '').strip()   
        try:
            # Add 'https://' if not present
            if not site.startswith(('http://', 'https://')):
                # Add 'www.' if not present
                if not site.startswith('www.'):
                    site = 'www.' + site
                site = 'https://' + site           
            # Add '.com' if no domain extension present
            if not any(site.endswith(domain) for domain in ['.com', '.org', '.edu', '.gov', '.net']):
                site = site + '.com'           
            speak(f"Opening {site}, boss")
            webbrowser.open(site)
        except Exception as e:
            speak("Sorry boss, I couldn't open that website")
            print(f"Error: {e}")
    else:
        speak("Sorry, I can't browse this website..")

import os

def close_browsing(query):
    if 'close google' in query:
        speak("Closing Google, boss")
        os.system("taskkill /f /im chrome.exe")  # Replace with your browser's process name if needed
    elif 'close youtube' in query:
        speak("Closing YouTube, boss")
        os.system("taskkill /f /im chrome.exe")  # Same as above
    elif 'close edge' in query:
        speak("Closing Microsoft Edge, boss")
        os.system("taskkill /f /im msedge.exe")  # For Microsoft Edge
    elif 'close browser' in query or 'close website' in query:
        speak("Closing all browsers, boss")
        os.system("taskkill /f /im chrome.exe")  # Modify or add processes as needed
        os.system("taskkill /f /im msedge.exe")
        os.system("taskkill /f /im firefox.exe")  # For Firefox
    else:
        speak("Sorry, I couldn't determine which browser or site to close, boss")

def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percantage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Boss our system have {percentage} percentage battery")

    if percentage>=80:
        speak("Boss we could have enough charging to continue our recording")
    elif percentage>=40 and percentage<=75:
        speak("Boss we should connect our system to charging point to charge our battery")
    else:
        speak("Boss we have very low power, please connect to charging otherwise recording should be off...")



if __name__ == "__main__":
    wishMe()
    # engine_talk("Allow me to introduce myself I am Jarvis, the virtual artificial intelligence and I'm here to assist you with a variety of tasks as best I can, 24 hours a day seven days a week.")
    while True:
        query = command().lower()
        # query  = input("Enter your command-> ")
        if ('open facebook' in query) or ('open instagram' in query) or ('open whatsapp' in query) or ('open linkedin' in query) or ('open twitter' in query) or ('open github' in query):
            open_social_media(query)
        elif ('close facebook' in query) or ('close instagram' in query) or ('close whatsapp' in query) or ('close linkedin' in query) or ('close twitter' in query) or ('close github' in query):
            close_social_media(query)
        elif ("university time table" in query) or ("schedule" in query):
            schedule()
        elif ("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")
        elif ("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decrease")
        elif ("volume mute" in query) or ("mute the sound" in query):
            pyautogui.press("volumemute")
            speak("Volume muted")
        elif ("open calculator" in query) or ("open notepad" in query) or ("open paint" in query):
            openApp(query)
        elif ("close calculator" in query) or ("close notepad" in query) or ("close paint" in query):
            closeApp(query)
        elif ("what" in query) or ("who" in query) or ("how" in query) or ("hi" in query) or ("thanks" in query) or ("hello" in query):
                padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
                result = model.predict(padded_sequences)
                tag = label_encoder.inverse_transform([np.argmax(result)])

                for i in data['intents']:
                    if i['tag'] == tag:
                        speak(np.random.choice(i['responses']))
        elif ("open google" in query) or ("open edge" in query) or ("open youtube" in query) or ("open website" in query) or ("visit site" in query) or ("go to" in query):
            open_browsing(query)
        elif ("close google" in query) or ("close edge" in query) or ("close youtube" in query) or ("close website" in query):
            close_browsing(query)
        elif ("system condition" in query) or ("condition of the system" in query):
            speak("checking the system condition")
            condition()
        elif "exit" in query:
            sys.exit()