# from turtle import Turtle , Screen

# timmy = Turtle()
# screen = Screen()
# timmy.shape("turtle")
# timmy.pencolor("blue")
# # timmy.size("large")
# timmy.shapesize(2,3,1)

# print(screen.canvheight)
# screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Python", ["GUI", "IS", "GOOD"])
table.add_column("Cpp", ["GUI", "IS", "BAD"])

table.align = "l"
print(table)

