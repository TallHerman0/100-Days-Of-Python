from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.up()
        self.down()
        self.left()
        self.right()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def create_snake(self):
        for num in STARTING_POSITIONS:
            self.add_turtle(num)
    
    def add_turtle(self, position):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.turtles.append(tim)
        self.head = self.turtles[0]

    def move(self):
        for tur_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[tur_num-1].xcor()
            new_y = self.turtles[tur_num-1].ycor()
            self.turtles[tur_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def grow(self):
        self.add_turtle(self.turtles[-1].position())
    
    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]