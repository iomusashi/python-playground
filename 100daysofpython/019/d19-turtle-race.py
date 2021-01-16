from turtle import Screen, Turtle

y_pos = [-100, -60, -20, 20, 60, 100]
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
screen = Screen()

def setup_screen_dimensions(width: int, height: int):
    global screen
    screen.setup(width=width, height=height)

def setup_turtles():
    global turtles
    turtles = []
    for i in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[i])
        turtle.penup()
        turtle.goto(-250, y_pos[i])
        turtles.append(turtle)

setup_screen_dimensions(width=500, height=400)
setup_turtles()
screen.exitonclick()
