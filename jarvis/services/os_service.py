import os
from assistant_logic.assistant import Assistant

class OSService:
    def __init__(self):
        self.assistant = Assistant()

    def rsl_action(self, action, action_name):
        self.assistant.speak(f"Ok, your pc will {action_name} in 10 seconds make sure you exit from all applications")
        os.system(f"shutdown /{action}")