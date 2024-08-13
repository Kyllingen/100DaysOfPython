from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

#1. Draw a square
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)

screen = Screen()
screen.exitonclick()