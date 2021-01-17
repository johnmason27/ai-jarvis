import speech_recognition as sr
import pyttsx3
import datetime

class Assistant:
    '''
        Houses all logic for configuring the AI voice and
        speech recognition.
    '''
    def __init__(self):
        '''
            Configuring the AI voice.
        '''
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", "voices[1].id")

    def speak(self, text):
        '''
            AI will speak to the user what ever text is passed in.

            Args:
                text: string, text to speak.
        '''
        self.engine.say(text)
        self.engine.runAndWait()
    
    def wish_me(self):
        '''
            Produces a welcome message depending on the time of day.
        '''
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
        '''
            Listens to the user when called and using the google voice API
            it will produce a string containing the command.
            
            Returns:
                statement: string, user's command.
        '''
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                statement = r.recognize_google(audio, language="en-in")
                print(f"User said: {statement}\n")
            except Exception:
                self.speak("Excuse me, I didn't catch that.")
                return "None"
                
            return statement