# Final Project
# Name: John Mason
# Student No: 2034708
# Personal virtual assistant for automating tasks and speeding up daily processes.
# -----------------------------------
from services.internet_service import InternetService
from services.api_call_service import ApiCallService
from services.general_service import GeneralService
from services.file_service import FileService
from services.os_service import OSService
from services.music_service import MusicService
from assistant_logic.assistant import Assistant

# Program dependencies
assistant = Assistant()
os_service = OSService()
internet_service = InternetService()
general_service = GeneralService()
file_service = FileService("./appsettings.json")
appsettings = file_service.read_appsettings()
api_call_service = ApiCallService(appsettings["WeatherApiKey"], appsettings["WolframalphaApiKey"])
music_service = MusicService(appsettings["MusixmatchApiKey"])

# Startup
print("Loading your AI personal assistant Jarvis")
assistant.speak("Loading your AI personal assistant Jarvis")
assistant.wish_me()

# Main logic
if __name__ == "__main__":
    while True:
        assistant.speak("How can I help you now?")
        statement = assistant.take_command().lower()
        
        if statement == 0:
            continue

        if "goodbye" in statement or "ok bye" in statement or "stop" in statement or "shut down" in statement:
            assistant.speak("Your personal assistant Jarvis is shutting down, Goodbye")
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
            general_service.display_time()
        elif "news" in statement:
            internet_service.open_tab("https://www.bbc.co.uk/news", "BBC News")
        elif "search" in statement:
            internet_service.search_web(statement)
        elif "who made you" in statement or "who created you" in statement:
            assistant.speak("I was developed by John")
            print("I was developed by John")
        elif "who are you" in statement or "what can you do" in statement:
            assistant.speak("I am Jarvis your personal assistant. I am programmed to do many tasks you might find boring or find it easier to use your voice to complete." + 
                "For example: opening web tabs such as google, stackoverflow, youtube and github, I can also open the latest news for you, predict time, search" +
                "wikipedia, forcast weather as well as anwser computational and geographical questions too.")
            print("I am Jarvis your personal assistant. I am programmed to do many tasks you might find boring or find it easier to use your voice to complete." + 
                "For example: opening web tabs such as google, stackoverflow, youtube and github, I can also open the latest news for you, predict time, search" +
                "wikipedia, get weather information, small operating system tasks as well as anwser computational and geographical questions too.")
        elif "weather" in statement:
            api_call_service.forecast_weather()
        elif "log off" in statement or "sign out" in statement:
            os_service.rsl_action("l", "log off")
        elif "shut down" in statement or "turn off" in statement:
            os_service.rsl_action("s", "shut down")
        elif "restart" in statement:
            os_service.rsl_action("r", "restart")
        elif "ask" in statement:
            api_call_service.call_wolframalpha()
        elif "joke" in statement:
            general_service.tell_joke()
        elif "music" in statement:
            music_service.sing_song_segment()