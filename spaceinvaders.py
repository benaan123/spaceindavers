# Space invaders
# Set up the screen
import turtle
import os
import math
import random

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
player.setposition(0, -450)
player.lt(90)

playerspeed = 25

# Choose number of enemies
number_of_enemies = 5
# Create empty list
enemies = []

# add enemies to the list
for i in range(number_of_enemies):
   
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(200, 450)
    enemy.setposition(x, y)

enemyspeed = 8

# Create bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 50

#define bullet state
# ready - ready to fire
# fire - bullet is actually fired
bulletstate = "ready"


# score
score = 0,

# move player right and left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -480:
        x = -480
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 480:
        x = 480
    player.setx(x)

def fire_bullet():
    # Declare bulletstate
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # bullet starts at player location
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y + 10)
        bullet.showturtle()

def isCollision(turtle1, turtle2):
    distance = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(), 2) + math.pow(turtle1.ycor() - turtle2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False

# create keyboard bindings
# functions for hold-down key
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
#Main game loop
while True:
    
    for enemy in enemies:

        # Move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Reverse enemy at border
        if enemy.xcor() > 480:
            y = enemy.ycor()
            y -= 80
            enemyspeed *= -1
            enemy.sety(y)

        if enemy.xcor() < -480:
            y = enemy.ycor()
            y -= 80
            enemyspeed *= -1
            enemy.sety(y)

                # check collision
        if isCollision(bullet, enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -1200)
            score += 1
            
            # reset enemy
            x = random.randint(-300, 300)
            y = random.randint(200, 450)
            enemy.setposition(x, y)
        
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            print("score")
            break
        

    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    if bullet.ycor() > 475:
        bullet.hideturtle()
        bulletstate = "ready"

   
        




border_pen.hideturtle()

# To keep screen up
delay = input("Press enter to finish.")
