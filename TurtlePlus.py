#turtleplus.py An enhanced library for Turtle Paint, based on Python.
#version：0.0.1
#2023© Copyright BobLv.
#Contact: system_help@yeah.net
# Draw a square
#Options a is a side length
#Options b is a speed
def square(a,b):
    import turtle
    turtle.speed(b)
    turtle.hideturtle()
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)
    input()
#Draw a polygon   
#Options a is a side length
#Options b is a number of sides
#Options c is a speed
def polygon(a,b,c):
    import turtle
    turtle.speed(c)
    turtle.hideturtle()
    for i in range(b):
        turtle.forward(a)
        turtle.right(360/b)
    input()
#Draw a pentagram    
#Options a is a side length
#Options b is a speed
def pentagram(a,b):
    import turtle
    turtle.speed(b)
    for i in range(5):    
        turtle.forward(a)      
        turtle.right(180-180/5)


