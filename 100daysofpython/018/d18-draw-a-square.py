from turtle import Screen
from turtle import Turtle

turtle = Turtle()


def draw_square(length: int):
    global turtle
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


draw_square(100)
screen = Screen()
screen.exitonclick()
