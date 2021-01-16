import os
from assistant_logic.assistant import Assistant

class OSService:
    '''
        Houses all logic for handling operating system requests.
    '''
    def __init__(self):
        '''
            Setting up the dependencies.
        '''
        self.assistant = Assistant()

    def rsl_action(self, action, action_name):
        '''
            Perform an action such as shutdown, log off or restart depending on the
            given in arguements.

            Args:
                action: string, l/r/s action for the system to do.
                action_name: string, action name.
        '''
        self.assistant.speak(f"Ok, your pc will {action_name} in 10 seconds make sure you exit from all applications")
        os.system(f"shutdown /{action}")