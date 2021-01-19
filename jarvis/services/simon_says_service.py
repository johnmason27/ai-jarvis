import time
import random
from assistant_logic.assistant import Assistant

class SimonSaysService:
    def __init__(self):
        self.assistant = Assistant()
        self.game_commands = ["Touch your head", "Touch your toes", "Spin around", "Touch your ears", "Touch your ears", "Touch your eyes", "Jump!", "Touch your hair",
            "Do 5 jumping jacks", "Do 5 press ups", "Do 5 situps", "Do 5 Burpees", "Wink with your left eye", "Wink with your right eye", "Walk like a penguin", 
            "Act like a monkey", "Sit down", "Stand on one foot", "Touch your nose", "Pretend to ride a horse", "Pretend to swim", "Turn around",
            "Walk on the spot", "Pretend to sit on a chair", "Don't move", "Pretend to lift a very heavy box", "Pretend to drink water", "Walk in a straight line",
            "Pretend to be cold", "Moo like a cow", "Whispher your name", "Do a silly dance", "Move in slow motion"]
        self.simon_commands = ["Simon says", ""]

    def mirror_me(self):
        self.assistant.speak("What does Simon say?")
        print("What does Simon say?")

        command = self.assistant.take_command()

        self.assistant.speak("Simon says, " + command)
        print("Simon says, " + command)

        time.sleep(1)

    def simon_says_game(self):
        for round in range(10):
            simon_command = random.choices(self.simon_commands)
            command = random.choices(self.game_commands)

            if simon_command[0] != "":
                self.assistant.speak(simon_command[0] + " " + command[0])
                print(simon_command[0] + " " + command[0])
            else:
                self.assistant.speak(command[0])
                print(command[0])
        
            time.sleep(5)

        self.assistant.speak("Game over! Thanks for playing!\n")
        print("Game over! Thanks for playing!")
        time.sleep(1)

    # Add quiz too
