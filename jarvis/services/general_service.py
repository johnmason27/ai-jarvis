import time
import datetime
import random
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
        self.joke_list = [("Why did the chicken cross the road?", "To get to the otherside."), ("Why do geese why south in the winter?", "Walking takes too long!"),
            ("Why do flamingos always lift one leg while standing?", "Because if they lifted both legs they'd fall over."), ("Why do ants never get sick?", "Because they have little antibodies."),
            ("Why did the old man fall into a well?", "He couldn’t see that well."), ("Why does Snoop Dog carry an umbrella?", "Fo’ drizzle."),
            ("Why shouldn’t you invite a nosy pepper to your house?", "He’ll get jalapeño business."), ("Why can't you trust a burrito?", "They tend to spill the beans!"),
            ("Why couldn't the lifeguard save the hippie?", "He was too far out."), ("Why was the tomato red?", "It saw the salad dressing."),
            ("Why do mermaids wear seashells?", "Because they grew out of their B shells."), ("Why did the mushroom go to the party?", "Because he's a fungi."),
            ("Why did the banana lose his driver's license?", "He peeled out."), ("Why do scuba divers fall backwards out of the boat?", "Because if they fell forwards they'd still be in the boat.")]

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

    def tell_joke(self):
        '''
            Tell a joke to the user via speech and text.
        '''
        # Get a random joke.
        joke = random.choices(self.joke_list)
        self.assistant.speak(joke[0][0])
        print(joke[0][0])

        time.sleep(1.5)

        self.assistant.speak(joke[0][1])
        print(joke[0][1])
        time.sleep(1)