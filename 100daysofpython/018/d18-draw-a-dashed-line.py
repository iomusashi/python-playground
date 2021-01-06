from turtle import Screen
from turtle import Turtle

turtle = Turtle()


def draw_dashed_line(length: int):
    global turtle
    pen_down = False
    for i in range(50):
        turtle.pendown() if not pen_down else turtle.penup()
        turtle.forward(length)
        pen_down = not pen_down


draw_dashed_line(10)
screen = Screen()
screen.exitonclick()
