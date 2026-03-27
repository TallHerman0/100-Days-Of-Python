from tkinter import *
from quiz_brain import QuizBrain
import data
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.dataa = data
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("340x500")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        #Score Text
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(row=0, column=1, pady=20)

        #Canvas
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)

        #Canvas Text
        self.question = self.canvas.create_text(150, 125, width=250, 
                                                text="This will be the question at hand becuase I know it", 
                                                font=("Arial", 16, "italic"), 
                                                fill=THEME_COLOR)

        #Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0, pady=20)
        
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = self.q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You have reached the end of the quiz!. You score is {self.quiz.score}/{self.dataa.my_parameters["amount"]}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)