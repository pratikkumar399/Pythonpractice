from turtle import Turtle, Screen

timmy = Turtle()
timmey = Screen()

# timmy.shape("square")
# timmy.shapesize(2,3,1)
# timmy.shapesize(2,3,1)
timmy.color("red")
for lines in range(4):
    timmy.forward(100)
    timmy.left(90)

# timmy.backward(100)

# timmy.left(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
print(timmy.position())

timmey.exitonclick()
