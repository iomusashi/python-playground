from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()


def move_forward(blocks=10):
    global turtle
    turtle.forward(blocks)


def move_backward(blocks=10):
    global turtle
    turtle.backward(blocks)


def move_left(angle=10):
    global turtle
    turtle.left(angle)


def move_right(angle=10):
    global turtle
    turtle.right(angle)

def clear():
    global turtle
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
