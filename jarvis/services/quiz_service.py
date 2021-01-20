import time
import random
# from assistant_logic.assistant import Assistant

class QuizService:
    '''
        Houses the quiz service logic.
    '''
    def __init__(self):
        '''
            Setup the quiz service dependencies.
        '''
        # self.assistant = Assistant()
        self.questions = [("What is the biggest animal in the world", "Blue whale"), ("Which country did brie cheese originate from", "France"),
            ("What year was Heniz established", "1869"), ("What is a baby rabbit called", "Kit"), 
            ("As of 2020 who is manager of the england football team", "Gareth Southgate"), ("What does He stand for on the periodic table", "Helium"),
            ("What is the capital of Australia", "Canberra"), ("Which bird can fly backwards", "Hummingbird"),
            ("When did the Vietnam War end", "1975"), ("Which hit video game series has released games called World At War and Black Ops", "Call of Duty"),
            ("What building did I'm a Celebrity 2020 taking place in", "Castle"), ("What type of nut is in the middle of a Ferrero Rocher", "Hazelnut"),
            ("What is a baby kangaroo called", "Joey"), ("What's the national flower of Japan", "Cherry blossom"),
            ("Which football team is known as The Red Devils", "Manchester United"), ("Which football team is known as The Baggies", "West Bromwich Albion"),
            ("How many ghosts visit Scrooge in A Christmas Carol", "4"), ("Which TV series has an alternate universe called The Upside Down", "Stranger Things"),
            ("In Texas, it’s illegal to swear in front of what", "A Corpse"), ("What was Marilyn Monroe’s natural hair color", "Red"),
            ("What do you call a group of unicorns", "A blessing"), ("What is banned in public places in Florida after 6 pm on a Thursday", "Farting"),
            ("What animal cannot stick out its tongue", "Crocodiles"), ("With how many bricks is the Empire State Building made of", "10 million"),
            ("According to Russian law, a homeless person must be where after 10 pm", "At home"), ("How many years old the oldest piece of chewing gum", "9000 years"),
            ("On Sunday, what is illegal to sell in Columbus, Ohio", "Cornflakes"), ("What is illegal to eat with a cherry pie in Kansas", "Ice cream"),
            ("On average, what is the thing that Americans do 22 times in a day", "Open the fridge"), ("A crossbreed between a donkey and the zebra is known as", "Zonkey"),
            ("What was the first fruit that was eaten on the moon", "Peach"), ("How do you tell the age of a horse", "It's teeth"),
            ("What sport has been played on the moon", "Golf"), ("How many noses does a slug have", "Four"), 
            ("What were clocks missing before 1577", "Minute Hands")]
    
    def play_quiz(self):
        '''
            Play the quiz game.  
            Asked 5 questions and given 10 seconds to think of an anwser.  
            Then the assistant will ask for your asnwer and store whether you
            got it right or wrong.  
            At the end you will get given a score out of 5.
        '''
        print("Welcome to the Quiz! Here's how this is going to work. Your going to be asked 5 questions total and then given a score out of 5 at the end. " + 
            "Each round you get asked a question and then given 10 seconds to think of an answer. After the 10 seconds are up you will asked by Jarvis for your answer. Until you " + 
            "have answered 5 questions. Once you have completed the quiz you'll get your score.")
        # self.assistant.speak('''Welcome to the Quiz! Here's how this is going to work. Your going to be asked 5 questions total and then given a score out of 5 at the end.
        #     Each round you get asked a question and then given 10 seconds to think of an answer. After the 10 seconds are up you will asked by Jarvis for your answer. Until you
        #     have answered 5 questions. Once you have completed the quiz you'll get your score.''')
        
        previous_questions = []

        for round in range(5):
            running = True
            exists = True

            while running:
                print(1)
                random_question = random.choices(self.questions)

                for question in previous_questions:
                    if question != random_question:
                        # exists = False
                        running = False

            previous_questions.append(random_question)

            print("Round", round)
            # time.sleep(10)

QuizService().play_quiz()