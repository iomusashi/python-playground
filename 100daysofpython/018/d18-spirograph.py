from random import choice
from random import randrange
from turtle import Screen
from turtle import Turtle
from turtle import screensize

turtle = Turtle()
screen = Screen()
screensize(520, 520, "black")
GREYSCALE_COLOR_RANGE = 256


def draw_spirograph(radius: int):
    global turtle
    global GREYSCALE_COLOR_RANGE

    turtle.speed("fastest")

    for i in range(0, 361, 2):
        red = randrange(GREYSCALE_COLOR_RANGE)
        green = randrange(GREYSCALE_COLOR_RANGE)
        blue = randrange(GREYSCALE_COLOR_RANGE)
        turtle.pencolor(red/GREYSCALE_COLOR_RANGE,
                        green/GREYSCALE_COLOR_RANGE,
                        blue/GREYSCALE_COLOR_RANGE)
        turtle.circle(100)
        turtle.setheading(i)


draw_spirograph(100)
screen.exitonclick()
