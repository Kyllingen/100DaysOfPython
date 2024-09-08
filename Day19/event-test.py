from turtle import Turtle, Screen

def move_forward():
    tim.forward(10)

tim  = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()