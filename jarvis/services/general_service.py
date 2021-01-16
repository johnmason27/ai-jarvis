import time
import datetime
from assistant_logic.assistant import Assistant

class GeneralService:
    '''
        Contains general services that are used by the assistant and program.
    '''
    def __init__(self):
        '''
            Setting up the dependencies.
        '''
        self.assistant = Assistant()

    def convert_temperature(self, current_temperature):
        '''
            Converts temperature from kelvin units to celsius units.

            Args:
                current_temperature: integer, temperature in kelvin.

            Returns:
                current_temperature: integer, temperature in celsius.
        '''
        celsius_temperature = round(current_temperature - 273.15)
        return celsius_temperature

    def display_time(self):
        '''
            Display the current time in the format HH:MM:SS.
        '''
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.assistant.speak(f"The time is {current_time}")
        print(f"The time is {current_time}")
        time.sleep(1)