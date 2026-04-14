from turtle import *
import random



def generate_random_hex_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

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

def forward_balls(turtle,list):
    turtle.fd(5)
    if turtle.xcor() > 245 or turtle.xcor() < -245:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle_list.append(make_turtle())
        turtle.speed(0)
        turtle.fd(10)
    elif turtle.ycor() > 245 or turtle.ycor() < -245:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle_list.append(make_turtle())
        turtle.speed(0)
        turtle.fd(10)
    return turtle_list

def make_turtle():
    t = Turtle()
    t.color(generate_random_hex_color())
    t.shape("turtle")
    t.setheading(random.randint(0,360))
    return t


def XY(turtle, X, Y):
    newX = turtle.xcor() + X
    newY = turtle.ycor() + Y
    if newX > 245 or newX() < -245:
        newX *= -1
        newX = turtle.xcor()
    if newY > 245 or newY() < -245:
        newY *= -1
        newY = turtle.ycor()  

screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)

polygon(4)

t = Turtle()
t.color("green")
t.shape("turtle")
t.setheading(random.randint(0,360))

turtle_list = [t]

while True:
    for thing in turtle_list:
        turtle_list = forward_balls(thing, turtle_list)

screen.exitonclick()