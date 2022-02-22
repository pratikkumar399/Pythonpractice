from turtle import Turtle, Screen


t = Turtle()
t1 = Screen()

for i in range (15) :
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

t1.exitonclick()
