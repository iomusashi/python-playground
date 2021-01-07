from random import choice
from random import randrange
from turtle import Screen
from turtle import Turtle

turtle = Turtle()
DIRECTIONS = [0, 90, 180, 270]
GREYSCALE_COLOR_RANGE = 256


def draw_random_walk(length: int, step_count: int):
    global turtle
    global DIRECTIONS
    global GREYSCALE_COLOR_RANGE

    turtle.pensize(10)
    turtle.speed("fast")

    for i in range(step_count):
        red = randrange(GREYSCALE_COLOR_RANGE)
        green = randrange(GREYSCALE_COLOR_RANGE)
        blue = randrange(GREYSCALE_COLOR_RANGE)
        turtle.pencolor(red/GREYSCALE_COLOR_RANGE,
                        green/GREYSCALE_COLOR_RANGE,
                        blue/GREYSCALE_COLOR_RANGE)
        angle = choice(DIRECTIONS)
        turtle.setheading(choice(DIRECTIONS))
        turtle.forward(length)


draw_random_walk(100, 50)
screen = Screen()
screen.exitonclick()
