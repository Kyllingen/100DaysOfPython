from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("coral")

#1. Draw a dashed line
for i in range(1,15):
    if i % 2 == 0:
        tim.pendown()
    else:
        tim.penup()
        
    tim.forward(10)


screen.exitonclick()