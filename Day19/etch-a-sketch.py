from turtle import Turtle, Screen

tim = Turtle()
STEP = 10

def init_screen():
    ''' initializes the screen'''
    screen = Screen()
    
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=clear_screen)

    screen.listen()
    screen.exitonclick()


def move_forward():
    ''' moves the turtle forward by STEP units'''
    tim.forward(STEP)
    
def move_backward():
    ''' moves the turtle backward by STEP units'''
    tim.backward(STEP)
    
def turn_left():
    ''' turns the turtle left by STEP degrees'''
    tim.left(STEP)
    
def turn_right():
    ''' turns the turtle right by STEP degrees'''
    tim.right(STEP)
    
def clear_screen():
    ''' clears the screen'''
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

init_screen()