from turtle import *
screen = Screen()
screen.bgcolor("black")
pen = Turtle()
pen.speed(0)
pen.color("blue")
pen.ht()

def polygon(turtle, sides):
    turtle.begin_fill()
    for i in range(sides):
        turtle.fd(200/sides)
        turtle.rt(360/sides)
    turtle.end_fill()
    
name = Turtle()
name.speed(0)
name.color("blue")
name.ht()

while True:    
    sides = int(input("how many sides "))
    pen.clear()
    if sides == 3:
        polygon(pen, sides)
        name.write("triangle"),
    if sides == 4:
        
    if sides == 5:
        polygon(pen, sides)
        name.write("pentagon"),
    if sides == 6:
        polygon(pen, sides)
        name.write("hexagon"),  
    if sides == 7:
        polygon(pen, sides)
        name.write("heptagon"),
    if sides == 8:
        polygon(pen, sides)
        name.write("octogon"),
    if sides == 9:
        polygon(pen, sides)
        name.write("nonagon"),
    if sides == 10:
        polygon(pen, sides)
        name.write("decagon"),     



screen.exitonclick()