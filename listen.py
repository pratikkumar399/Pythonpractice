from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def reset_screen():
    tim.clear()
    tim.reset()

screen.listen() 
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='w',fun=move_forwards)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=reset_screen)
screen.exitonclick()


