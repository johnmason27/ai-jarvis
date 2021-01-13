import webbrowser
import time
import wikipedia
from assistant_logic.assistant import Assistant

class InternetService:
    def __init__(self):
        self.assistant = Assistant()

    def open_tab(self, url, website_name):
        webbrowser.open_new_tab(url)
        self.assistant.speak(f"{website_name} is open now")
        print(f"{website_name} is open now")
        time.sleep(1)
    
    def search_web(self, statement):
        statement = statement.replace("search", "")
        search_query = ""
        statement = statement.split()
        for x in range(len(statement)):
            if x == 0:
                search_query += statement[x]
            else:
                search_query += "+" + statement[x]
        webbrowser.open_new_tab(f"https://www.bing.com/search?q={search_query}")
        self.assistant.speak("Website is open")
        print("Website is open")
        time.sleep(1)

    def search_wikipedia(self, statement):
        self.assistant.speak("Searching Wikipedia...")
        print("Searching Wikipedia...")
        try:
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            self.assistant.speak("According to Wikipedia")
            print(results)
            self.assistant.speak(results)
        except Exception:
            self.assistant.speak("That Wikipedia page couldn't be found")
            print("That Wikipedia page couldn't be found")
        time.sleep(1)