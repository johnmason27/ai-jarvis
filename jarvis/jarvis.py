import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import wolframalpha
import json
import requests

from services.internet_service import InternetService

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", "voices[1].id")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
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

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language="en-in")
            print(f"User said: {statement}\n")

        except Exception:
            speak("Excuse me, I didn't catch that, please repeat what you said.")
            return "None"
        return statement

def convert_temperature(current_temperature):
    celsius_temperature = round(current_temperature - 273.15)
    return celsius_temperature

print("Loading your AI personal assistant Jarvis")
speak("Loading your AI personal assistant Jarvis")
wish_me()

internet_service = InternetService()

if __name__ == "__main__":
    while True:
        speak("Tell me how I help you now?")
        statement = take_command().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "shut down" in statement:
            speak("Your personal assistant Jarvis is shutting down, Goodbye")
            print("Your personal assistant Jarvis is shutting down, Goodbye")
            break

        if "wikipedia" in statement:
            internet_service.search_wikipedia(statement)
        elif "open youtube" in statement:
            internet_service.open_tab("https://www.youtube.com", "YouTube")
        elif "open google" in statement:
            internet_service.open_tab("https://www.google.com", "Google")
        elif "open outlook" in statement:
            internet_service.open_tab("https://outlook.office.com/mail/inbox", "Outlook")
        elif "open github" in statement:
            internet_service.open_tab("https://github.com", "Github")
        elif "open stackoverflow" in statement:
            internet_service.open_tab("https://stackoverflow.com", "Stackoverflow")
        elif "time" in statement:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
            print(f"The time is {current_time}")
            time.sleep(1)
        elif "news" in statement:
            internet_service.open_tab("https://www.bbc.co.uk/news", "BBC News")
        elif "search" in statement:
            internet_service.search_web(statement)
        elif "who made you" in statement or "who created you" in statement:
            speak("I was developed by John")
            print("I was developed by John")
        elif "who are you" in statement or "what can you do" in statement:
            speak("I am Jarvis your personal assistant. I am programmed to do many tasks you might find boring or find it easier to use your voice to complete." + 
                "For example: opening web tabs such as google, stackoverflow, youtube and github, I can also open the latest news for you, predict time, search" +
                "wikipedia, forcast weather as well as anwser computational and geographical questions too.")
            print("I am Jarvis your personal assistant. I am programmed to do many tasks you might find boring or find it easier to use your voice to complete." + 
                "For example: opening web tabs such as google, stackoverflow, youtube and github, I can also open the latest news for you, predict time, search" +
                "wikipedia, get weather information, small operating system tasks as well as anwser computational and geographical questions too.")
        elif "weather" in statement:
            api_key = "b6c7f08a0ddef75b7265b8f0014af134"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the city name")
            city_name = take_command()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            response_dic = response.json()
            if response_dic["cod"] != "404":
                data = response_dic["main"]
                current_temperature = data["temp"]
                current_temperature = convert_temperature(current_temperature)
                current_humidity = data["humidity"]
                weather_data = response_dic["weather"]
                weather_description = weather_data[0]["description"]
                speak(f"Tempurature is {current_temperature} degrees celsius.\nHumidity is {current_humidity} percent.\nDescription {weather_description}.")
                print(f"Tempurature is {current_temperature} degrees celsius.\nHumidity is {current_humidity} percent.\nDescription {weather_description}.")
            else:
                speak("Failed to fetch weather data.")
                print("Failed to fetch weather data.")
            time.sleep(1)
        elif "log off" in statement or "sign out" in statement:
            speak("Ok, your pc will log off in 10 seconds make sure you exit from all applications")
            os.system("shutdown /l")
        elif "shut down" in statement or "turn off" in statement:
            speak("Ok, your pc will shut down in 10 seconds make sure you exit from all applications")
            os.system("shutdown /s")
        elif "restart" in statement:
            speak("Ok, your pc will restart in 10 seconds make sure you exit from all applications")
            os.system("shutdown /r")
        elif "ask" in statement:
            speak("I can answer to computational and geographical questions and what question do you want to ask now?")
            print("I can answer to computational and geographical questions and what question do you want to ask now?")
            question = take_command()
            try:
                app_id = "X2XKTJ-4PL8L5E4RE"
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)
            except Exception:
                speak("Failed to fetch response.")
                print("Failed to fetch response.")
            time.sleep(1)
