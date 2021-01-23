import requests
import json
import time
from assistant_logic.assistant import Assistant

class MusicService:
    '''
        Houses the music service and it's related methods.
    '''
    def __init__(self, key):
        '''
            Setup the dependencies.  
            Args:
                key: string, music api key.
        '''
        self.api_key = "&apikey=" + key
        self.assistant = Assistant()

    def get_input(self, question):
        '''
            Get the input from the user.  
            Args:
                question: string, quesiton to ask.  
            Returns:
                statement: string, user input.
        '''
        # Ask for input and ask again if nothing is returned.
        while True:
            self.assistant.speak(question)
            print(question)
            statement = self.assistant.take_command()

            if statement != "None":
                break
        
        return statement

    def sing_song_segment(self):
        '''
            Call the api and sing the start of the song to the user via the assistant.
        '''
        self.assistant.speak("Welcome to the Music Service!")
        print("Welcome to the Music Service!")

        artist_name = self.get_input("Whats's the name of the artist?")
        track_name = self.get_input("What's the name of the track?")

        self.assistant.speak("Loading music...")
        print("Loading music...")

        # Create API request.
        api_call = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_artist=" + artist_name + "&q_track=" + track_name + self.api_key
        
        # Perform the API call.
        try:
            request = requests.get(api_call)
            data = request.json()
            # Extract the data from reponse and print/speak.
            data = data['message']['body']
            data['lyrics']['lyrics_body'] = data['lyrics']['lyrics_body'].replace("\n...\n\n******* This Lyrics is NOT for Commercial use *******", "")
            self.assistant.speak(f"Playing {track_name} by {artist_name}")
            print(f"Playing {track_name} by {artist_name}")
            print(data['lyrics']['lyrics_body'])
            self.assistant.speak(data['lyrics']['lyrics_body'])
        except Exception:
            self.assistant.speak(f"Sorry the song, {track_name} by {artist_name} wasn't found.")
            print(f"Sorry the song, {track_name} by {artist_name} wasn't found.")

        time.sleep(1)