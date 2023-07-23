from turtle import Turtle, Screen
import random

my_turtle = Turtle()
colors = ['lawn green', 'yellow', 'blue', 'dark goldenrod', 'teal', 'navy', 'medium violet red']
direction = [0, 90, 180, 270]

gameplay = True
while gameplay:
    rand_num = random.choice(direction)
    color_choice = random.choice(colors)
    my_turtle.color(color_choice)
    my_turtle.setheading(rand_num)
    my_turtle.forward(15)

my_screen = Screen()
my_screen.exitonclick()
