import turtle
import random


t = turtle.Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randcol = (r, g, b)
    return randcol


t.speed('fastest')


def create_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
        # t.circle(100)

create_spiro(3)


turtle.exitonclick()
