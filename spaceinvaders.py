# Space invaders
# Set up the screen
import turtle
import os


# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.screensize(800, 600)

# Draw border
border_pen = turtle.Turtle()
# speed = 0 is instant
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-500, -500)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(1000)
    border_pen.lt(90)

# Create player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)


border_pen.hideturtle()

# To keep screen up
delay = input("Press enter to finish.")
