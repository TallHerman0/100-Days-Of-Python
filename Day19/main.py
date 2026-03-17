from turtle import Turtle, Screen
import random

start = -100

is_game_on = False
screen = Screen()
screen.setup(500,400)
colors = ["red", "orange", "blue", "yellow", "purple", "green"]

turtles = []

for num in range(len(colors)):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[num])
    tim.penup()
    tim.goto(-230,start)
    start += 40
    turtles.append(tim)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ").lower()

if user_bet in colors:
    is_game_on = True

while is_game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!!")
                is_game_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!!")
                is_game_on = False
        
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
