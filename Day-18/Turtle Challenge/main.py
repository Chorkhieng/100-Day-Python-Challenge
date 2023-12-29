from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(45)
# timmy_the_turtle.forward(200)


# draw circle
# for _ in range(360):
#     timmy_the_turtle.forward(1)
#     timmy_the_turtle.left(1)

# generate random walk
direction = [0, 90, 180, 270, 360]
tim = Turtle()
tim.shape("turtle")
tim.color("blue")

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()