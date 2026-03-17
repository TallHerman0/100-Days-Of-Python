class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
    
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text}. (True/False)?: ")
        self.question_number += 1
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!!")
            self.score += 1
        else:
            print("You are wrong!!")
        
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
