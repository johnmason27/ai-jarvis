import time
import datetime
from assistant_logic.assistant import Assistant

class GeneralService:
    def __init__(self):
        self.assistant = Assistant()

    def convert_temperature(self, current_temperature):
        celsius_temperature = round(current_temperature - 273.15)
        return celsius_temperature

    def display_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.assistant.speak(f"The time is {current_time}")
        print(f"The time is {current_time}")
        time.sleep(1)