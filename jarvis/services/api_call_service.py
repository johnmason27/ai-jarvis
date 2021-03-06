import requests
import time
import wolframalpha
from assistant_logic.assistant import Assistant
from services.general_service import GeneralService

class ApiCallService:
    '''
        Houses all logic for calling the third party API's.
    '''
    def __init__(self, weather_api_key, wolframalpha_api_key):
        '''
            Setup for API keys from appsettings and other dependencies.
        '''
        self.weather_api_key = weather_api_key
        self.wolframalpha_api_key = wolframalpha_api_key
        self.assistant = Assistant()
        self.general_service = GeneralService()

    def forecast_weather(self):
        '''
            Forecast weather using the openweathermap api.
        '''
        self.assistant.speak("What is the city name")
        city_name = self.assistant.take_command()
        # Create the API request.
        complete_url = "https://api.openweathermap.org/data/2.5/weather?" + "appid=" + self.weather_api_key + "&q=" + city_name
        response = requests.get(complete_url)
        response_dic = response.json()

        # Check if the response is bad.
        if response_dic["cod"] != "404":
            # Extract response and print out.
            data = response_dic["main"]
            current_temperature = data["temp"]
            current_temperature = self.general_service.convert_temperature(current_temperature)
            current_humidity = data["humidity"]
            weather_data = response_dic["weather"]
            weather_description = weather_data[0]["description"]
            self.assistant.speak(f"Tempurature is {current_temperature} degrees celsius.\nHumidity is {current_humidity} percent.\nDescription {weather_description}.")
            print(f"Tempurature is {current_temperature} degrees celsius.\nHumidity is {current_humidity} percent.\nDescription {weather_description}.")
        else:
            self.assistant.speak("Failed to fetch weather data.")
            print("Failed to fetch weather data.")

        time.sleep(1)

    def call_wolframalpha(self):
        '''
            Respond to questions about computational and geographical questions using
            the wolframalpha api.
        '''
        self.assistant.speak("I can answer to computational and geographical questions and what question do you want to ask now?")
        print("I can answer to computational and geographical questions and what question do you want to ask now?")
        question = self.assistant.take_command()

        # Call and fetch data.
        try:
            client = wolframalpha.Client(self.wolframalpha_api_key)
            res = client.query(question)
            answer = next(res.results).text
            self.assistant.speak(answer)
            print(answer)
        except Exception:
            self.assistant.speak("Failed to fetch response.")
            print("Failed to fetch response.")
            
        time.sleep(1)