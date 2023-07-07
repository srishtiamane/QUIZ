import random

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display_question(self):
        print(self.question)
        random.shuffle(self.options)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
    
    def check_answer(self, user_answer):
        return user_answer == self.answer


class Quizgame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run_game(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display_question()
            user_answer = input("Enter your answer (1, 2, 3, etc.): ")
            if question.check_answer(int(user_answer)):
                print("Correct answer!\n")
                self.score += 1
            else:
                print("Incorrect answer!\n")
        self.display_final_score()

    def display_final_score(self):
        print("Quiz finished!")
        print(f"Your score: {self.score}/{len(self.questions)}")


# Create some questions
que1 = Question("What is the capital of France?", ["Paris", "London", "Berlin"], 1)
que2 = Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], 1)
que3 = Question("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune"], 1)

# Create the Quiz Game
quiz = Quizgame()
quiz.add_question(que1)
quiz.add_question(que2)
quiz.add_question(que3)

# Run the Quiz Game
quiz.run_game()
