# import turtle and screen class and instantiate an object of the class
from turtle import Turtle, Screen

#create a turtle object, use methods to set attributes
timmy  = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
myScreen = Screen()

print (myScreen.canvheight)
myScreen.exitonclick()