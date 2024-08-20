import colorgram
import turtle
import random

def extract_colors():
    ''' extracts the colors to be used for painting'''
    colors = colorgram.extract('data/image.jpg', 20)
    rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    return rgb_colors

def init_turtle():
    ''' initializes the turtle'''
    tim = turtle.Turtle()
    tim.speed(0)
    tim.penup()
    tim.setposition(-100, -100)
    tim.hideturtle()
    return tim

def init_screen():
    ''' initializes the screen'''
    screen = turtle.Screen()
    screen.colormode(255)
    return screen

def paint_dot(tim, colorList, i, j):
    ''' paints a dot at the given position'''
    tim.penup()
    tim.setposition(-250 + i * 50, -250 + j * 50)
    tim.pendown()
    chosen_color = random.choice(colorList)
    tim.pencolor(chosen_color)
    tim.dot(20)

def draw_painting(dots = 10):
    ''' draws the painting'''
    tim = init_turtle()
    screen = init_screen()
    colorList = extract_colors()
    
    for i in range(dots):
        for j in range(dots):
            paint_dot(tim, colorList, j, i)
            
    screen.exitonclick()
            
  
draw_painting()