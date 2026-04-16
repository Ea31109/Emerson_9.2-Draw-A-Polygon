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

def forward_balls(turtle, list):
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

def make_player():
    global player 
    player = Turtle()
    player.color("green")
    player.shape("turtle")
    player.speed(0)
    
def up():
    global player
    player.setheading(90)
    player.sety(player.ycor() + 5)

def down():
    global player
    player.setheading(270)
    player.sety(player.ycor() - 5)

def left():
    global player
    player.setheading(180)
    player.setx(player.xcor() - 5)

def right():
    global player
    player.setheading(0)
    player.setx(player.xcor() + 5)

def turn_right():
    global player
    player.right(10)

def turn_left():
    global player
    player.left(10)





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

screen.listen()
screen.onkeypress(make_player, "space")
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")

polygon(4)

t = Turtle()
t.color("green")
t.shape("turtle")
t.setheading(random.randint(0,360))

turtle_list = [t]

player = None

while True:
    if player != None:
        turtle_list = forward_balls(player, turtle_list)
    for thing in turtle_list:
        turtle_list = forward_balls(thing, turtle_list)
        if player != None and thing.distance(player) < 20:
            thing.hideturtle()
            turtle_list.remove(thing)


screen.exitonclick()