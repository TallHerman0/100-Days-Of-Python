from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def create_paddle(self):
        pass

    def go_up(self):
        new_position = (self.xcor(), self.ycor()+20)
        self.goto(new_position)

    def go_down(self):
        new_position = (self.xcor(), self.ycor()-20)
        self.goto(new_position)