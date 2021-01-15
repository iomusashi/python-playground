from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)
screen.exitonclick()
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axes = [-88, -50, -16, 16, 50, 88]

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")
turtles = []
for i in range(0, 6):
    tutle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-250, y=y_axes[i])
    turtles.append(turtle)
if user_bet in colors:
    print("betcolor")
else:
    print("Invalid color to bet")
