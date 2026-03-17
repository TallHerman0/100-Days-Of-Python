from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        with open("C:/Users/HopeK/Desktop/highscore.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,270)
    
    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", move=False, align="center", font=('Arial', 16, 'normal'))
    
    def score_increase(self):
        self.score += 1
        self.score_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_update()
        scoree = str(self.high_score)
        with open("highscore.txt", mode="w") as f:
            f.write(scoree)
