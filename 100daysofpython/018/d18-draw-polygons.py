from random import randrange
from turtle import Screen
from turtle import Turtle

turtle = Turtle()
LINE_LENGTH = 100
FULL_TURN_ANGLE = 360
GREYSCALE_COLOR_RANGE = 256


def draw_polygons():
    global turtle
    global LINE_LENGTH
    global FULL_TURN_ANGLE
    global GREYSCALE_COLOR_RANGE

    for i in range(3, 11):
        red = randrange(GREYSCALE_COLOR_RANGE)
        green = randrange(GREYSCALE_COLOR_RANGE)
        blue = randrange(GREYSCALE_COLOR_RANGE)
        turtle.pencolor(red/GREYSCALE_COLOR_RANGE,
                        green/GREYSCALE_COLOR_RANGE,
                        blue/GREYSCALE_COLOR_RANGE)
        angle = FULL_TURN_ANGLE / i
        for j in range(i):
            turtle.forward(100)
            turtle.right(angle)


draw_polygons()
screen = Screen()
screen.exitonclick()
