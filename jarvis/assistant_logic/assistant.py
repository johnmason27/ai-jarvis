import speech_recognition as sr
import pyttsx3
import datetime

class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", "voices[1].id")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def wish_me(self):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            self.speak("Hello, Good Morning")
            print("Hello, Good Morning")
        elif hour >= 12 and hour < 18:
            self.speak("Hello, Good Afternoon")
            print("Hello, Good Afternoon")
        else:
            self.speak("Hello, Good Evening")
            print("Hello, Good Evening")

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                statement = r.recognize_google(audio, language="en-in")
                print(f"User said: {statement}\n")

            except Exception:
                self.speak("Excuse me, I didn't catch that, please repeat what you said.")
                return "None"
            return statement