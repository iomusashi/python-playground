from random import randint
from turtle import Screen, Turtle
import turtle as t

y_pos = [-100, -60, -20, 20, 60, 100]
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
turtles = []
screen = Screen()
user_bet = ""


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


def take_bets():
    global user_bet
    user_bet = screen.textinput(
        title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def start_race():
    global turtles
    while True:
        run_turtle_run()


def run_turtle_run():
    global turtles
    finish_line = int(screen.window_width() / 2)
    for turtle in turtles:
        run = randint(1, 5)
        xcor = turtle.xcor()
        xcor = finish_line if xcor + run >= finish_line else xcor + run
        turtle.setx(xcor)
        if turtle.xcor() == finish_line:
            print(f"Turtle {turtle.pencolor()} won the race!")
            if user_bet == turtle.pencolor():
                print("Congratulations! You won!")
            else:
                print("Sorry, you lost!")
            t.bye()


setup_screen_dimensions(width=500, height=400)
setup_turtles()
take_bets()
start_race()
screen.exitonclick()
