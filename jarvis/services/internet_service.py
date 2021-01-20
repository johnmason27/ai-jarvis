import webbrowser
import time
import wikipedia
from assistant_logic.assistant import Assistant

class InternetService:
    '''
        Houses all the logic responsible for the internet.
    '''
    def __init__(self):
        '''
            Setting up the dependencies.
        '''
        self.assistant = Assistant()

    def open_tab(self, url, website_name):
        '''
            Open a new tab for the user.  
            Args:
                url: string, url search string.
                website_name: string, website name.
        '''
        webbrowser.open_new_tab(url)
        self.assistant.speak(f"{website_name} is open now")
        print(f"{website_name} is open now")
        time.sleep(1)
    
    def search_web(self, statement):
        '''
            Open a new browser based of the statement given by the user.  
            Args:
                statement: string, user command.
        '''
        statement = statement.replace("search", "")
        search_query = ""
        statement = statement.split()

        for item in range(len(statement)):
            if item == 0:
                search_query += statement[item]
            else:
                search_query += "+" + statement[item]

        webbrowser.open_new_tab(f"https://www.bing.com/search?q={search_query}")
        self.assistant.speak("Website is open")
        print("Website is open")
        time.sleep(1)

    def search_wikipedia(self, statement):
        '''
            Search wikipedia based off the user statement.  
            Args:
                statement: string, user command.
        '''
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