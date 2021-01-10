import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", "voices[1].id")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language="en-in")
            print(f"User said: {statement}\n")

        except Exception:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Jarvis")
speak("Loading your AI personal assistant Jarvis")
wishMe()

if __name__ == "__main__":
    while True:
        speak("Tell me how I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "shut down" in statement:
            speak("Your personal assistant Jarvis is shutting down, Goodbye")
            print("Your personal assistant Jarvis is shutting down, Goodbye")
            break

        if "wikipedia" in statement:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            try:
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("That Wikipedia page couldn't be found")
                print("That Wikipedia page couldn't be found")
            time.sleep(1)
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open now")
            print("YouTube is open now")
            time.sleep(1)
        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            print("Google is open now")
            time.sleep(1)
        elif "open outlook" in statement:
            webbrowser.open_new_tab("https://outlook.office.com/mail/inbox")
            speak("Outlook is open now")
            print("Outlook is open now")
            time.sleep(1)
        elif "open github" in statement:
            webbrowser.open_new_tab("https://github.com")
            speak("Github is open now")
            print("Github is open now")
            time.sleep(1)
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Stackoverflow is now open")
            print("Stackoverflow is now open")
            time.sleep(1)
        elif "time" in statement:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
            print(f"The time is {current_time}")
            time.sleep(1)
        elif "news" in statement:
            webbrowser.open_new_tab("https://www.bbc.co.uk/news")
            speak("BBC News is now open")
            print("BBC News is now open")
            time.sleep(1)
        elif "search" in statement:
            statement = statement.replace("search", "")
            search_query = ""
            statement = statement.split()
            for x in range(len(statement)):
                if x == 0:
                    search_query += statement[x]
                else:
                    nsearch_query += "+" + statement[x]
            webbrowser.open_new_tab(f"https://www.bing.com/search?q={search_query}")
            time.sleep(1)