# import turtle

# Katli = turtle.Turtle()
# Katli.shape('turtle')
# Katli.color("cyan2")
# Katli.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

Table = prettytable.PrettyTable()

Table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
Table.add_column("Type", ["Electric", "Water", "Fire"])
Table.align = "r"

print(Table)