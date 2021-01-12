from colorgram import extract
from random import choice
from random import randrange
from turtle import Screen
from turtle import Turtle
from turtle import screensize

DOT_SIZE = 20
DISTANCE = 50
GREYSCALE_COLOR_RANGE = 256
rgb_colors = []
turtle = Turtle()
screen = Screen()
screensize(520, 520, "black")


def extract_colors() -> list:
    image = "d18_hirst.jpg"
    colors = extract(image, 30)
    return list(map(lambda color: (color.rgb.r / GREYSCALE_COLOR_RANGE,
                                   color.rgb.g / GREYSCALE_COLOR_RANGE,
                                   color.rgb.b / GREYSCALE_COLOR_RANGE), colors))


def hirst_spots(grid_size=10):
    global DOT_SIZE
    global DISTANCE
    global rgb_colors
    rgb_colors = extract_colors()
    turtle.penup()
    turtle.speed("fastest")
    for i in range(grid_size):
        for j in range(grid_size):
            mid = grid_size / 2
            turtle.setposition((j - mid) * DISTANCE, (i - mid) * DISTANCE)
            turtle.pencolor(choice(rgb_colors))
            turtle.pendown()
            turtle.dot(DOT_SIZE)
            turtle.penup()


hirst_spots()
screen.exitonclick()
