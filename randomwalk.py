import turtle 
import random


t = turtle.Turtle()
turtle.colormode(255)
# colors = ["red","green", "blue","yellow","black","orange"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcol = (r,g,b)
    return randcol


direction = [0 ,90,180,270]
t.pensize(10)
t.speed(50)

for i in range(500):
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))

turtle.exitonclick()