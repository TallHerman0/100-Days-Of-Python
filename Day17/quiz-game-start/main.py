from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for number in range(0,len(question_data)):
    text = question_data[number]["text"]
    answer = question_data[number]["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz!!!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
