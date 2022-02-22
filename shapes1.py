from turtle import Turtle , Screen
import random

t  =  Turtle()
t1 = Screen()
colors = ["red","green", "blue","yellow","black"]

def draw_shape(numofsides):
    angles = 360/numofsides
    for _ in range(numofsides):
        t.forward(100)
        t.left(angles)


for i in range(3,12):
    t.color(random.choice(colors))
    draw_shape(i)

t1.exitonclick()