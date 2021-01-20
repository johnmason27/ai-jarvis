import time
import random
from assistant_logic.assistant import Assistant

class QuizService:
    '''
        Houses the quiz service logic.
    '''
    def __init__(self):
        '''
            Setup the quiz service dependencies.
        '''
        self.assistant = Assistant()
        self.questions = [("What is the biggest animal in the world?", "blue whale"), ("Which country did brie cheese originate from?", "france"),
            ("What year was Heniz established?", "1869"), ("What is a baby rabbit called?", "kit"), 
            ("As of 2020 who is manager of the england football team?", "gareth southgate"), ("What does He stand for on the periodic table?", "helium"),
            ("What is the capital of Australia?", "canberra"), ("Which bird can fly backwards?", "hummingbird"),
            ("When did the Vietnam War end?", "1975"), ("Which hit video game series has released games called World At War and Black Ops?", "call of duty"),
            ("What building did I'm a Celebrity 2020 taking place in?", "castle"), ("What type of nut is in the middle of a Ferrero Rocher?", "hazelnut"),
            ("What is a baby kangaroo called?", "joey"), ("What's the national flower of Japan?", "cherry blossom"),
            ("Which football team is known as The Red Devils?", "manchester united"), ("Which football team is known as The Baggies?", "west bromwich albion"),
            ("How many ghosts visit Scrooge in A Christmas Carol?", "4"), ("Which TV series has an alternate universe called The Upside Down?", "stranger things"),
            ("In Texas, it’s illegal to swear in front of what?", "corpse"), ("What was Marilyn Monroe’s natural hair color?", "red"),
            ("What do you call a group of unicorns?", "blessing"), ("What is banned in public places in Florida after 6 pm on a Thursday?", "farting"),
            ("What animal cannot stick out its tongue?", "crocodile"), ("With how many bricks is the Empire State Building made of?", "10 million"),
            ("According to Russian law, a homeless person must be where after 10 pm?", "at home"), ("How many years old the oldest piece of chewing gum?", "9000 years"),
            ("On Sunday, what is illegal to sell in Columbus, Ohio?", "cornflake"), ("What is illegal to eat with a cherry pie in Kansas?", "ice cream"),
            ("On average, what is the thing that Americans do 22 times in a day?", "open the fridge"), ("A crossbreed between a donkey and the zebra is known as?", "zonkey"),
            ("What was the first fruit that was eaten on the moon?", "peach"), ("How do you tell the age of a horse?", "it's teeth"),
            ("What sport has been played on the moon?", "golf"), ("How many noses does a slug have?", "four"), 
            ("What were clocks missing before 1577?", "minute hands")]
    
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
        self.assistant.speak("Welcome to the Quiz! Here's how this is going to work. Your going to be asked 5 questions total and then given a score out of 5 at the end. " + 
            "Each round you get asked a question and then given 10 seconds to think of an answer. After the 10 seconds are up you will be asked by Jarvis for your answer. Until you " + 
            "have answered 5 questions. Once you have completed the quiz you'll get your score.")

        previous_questions = []
        score = 0

        for round in range(5):
            self.assistant.speak("Round", round + 1)
            print("Round", round + 1)
            running = True
            exists = True

            while running:
                random_question = random.choices(self.questions)

                if random_question in previous_questions:
                    random_question = random.choices(self.questions)
                else:
                    running = False

            previous_questions.append(random_question)

            self.assistant.speak(random_question[0][0])
            print(random_question[0][0])
            time.sleep(10)

            while True:
                self.assistant.speak("What is your answer?")
                print("What is your answer?")
                statement = self.assistant.take_command()

                if statement != "None":
                    break

            if statement.lower() in random_question[0][1]:
                print("Correct")
                self.assistant.speak("Correct")
                score += 1
            else:
                print("Incorrect")
                self.assistant.speak("Incorrect")

            time.sleep(1)
        
        self.assistant.speak("Quiz Complete!")
        self.assistant.speak("Drum role please...")
        self.assistant.speak(f"Your final score is, {score} points!")
        self.assistant.speak("Welldone thanks for playing!")

        print("Quiz Complete!")
        print("Drum role please...")
        print(f"Your final score is, {score} points!")
        print("Welldone and thanks for playing!")
        time.sleep(1)