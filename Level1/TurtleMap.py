# Imports the init.py file and the turtle module
from init import *
import turtle

# Creates our screen
SCREEN = turtle.Screen()
SCREEN.title("Mapster Spacebook")
SCREEN.setup(1280, 800)
SCREEN.bgpic(get_file("Assets/Background.gif"))

# Sets the shape to be a green turtle
turtle.shape("turtle")
turtle.color("green")

# This code moves the turtle to its starting location
turtle.penup()
turtle.setx(460)
turtle.sety(-275)
turtle.pendown()

#TODO: Uncomment these lines by removing the hashtags
#turtle.left(180)
#turtle.forward(510)

#TODO: Copy the two lines Grafika gives you here



#TODO: Write the last 4 lines, following Grafika's instructions





# This line stops the window from closing, once we make it to the end
turtle.done()
