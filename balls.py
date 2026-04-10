from turtle import *
import random


def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)

def polygon(sides):
    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.ht()
    pen.penup
    pen.goto(-250,250)
    pen.pendown
    pen.begin_fill()
    for i in range(sides):
        pen.fd(500)
        pen.rt(360/sides)
    pen.end_fill()

def forward_balls(turtle):
    turtle.fd(5)
    if turtle.xcor() > 245 or turtle.xcor() < -245:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.speed(1)
        turtle.fd(10)
    elif turtle.ycor() > 245 or turtle.ycor() < -245:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.speed(1)
        turtle.fd(10)

def XY(turtle, X, Y):
    newX = turtle.xcor() + X
    newY = turtle.ycor() + Y
    if newX > 245 or newX() < -245:
        newX *= -1
        newX = turtle.xcor()
    if newY > 245 or newY() < -245:
        newY *= -1
        newY = turtle.ycor()  


polygon(4)

t = Turtle()
t.color("green")
t.shape("turtle")
t.setheading(random.randint(0,360))
deltaX = (random.randint(-5,5))
deltaY = (random.randint(-5,5))

while True:
    forward_balls(t)

screen.exitonclick()
