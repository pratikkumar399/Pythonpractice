from turtle import Turtle, Screen
import random


screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="User bet", prompt="Which turtle you want to bet on? Tell your color : ")
y = [-70, -40, -10, 20, 50, 80]
all_turtles = []

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(
                    f"You have won!The {winning_color} turtle is the winner.")
            else:
                print(
                    f"You have lost!The {winning_color} turtle is the winner.")

        random_distant = random.randint(0, 10)
        turtle.forward(random_distant)
       

screen.exitonclick()


# new_turtle.goto(-230,-100)
