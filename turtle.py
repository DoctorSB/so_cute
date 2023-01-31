from math import sin, pi
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
t.shape("turtle")
wn.bgcolor("lavender blush")
t.speed(1)


colors = ["red", "deep pink", "light pink", "midnight blue", "blue", "dodger blue", "deep sky blue"]

def color(iteration):
    t.pencolor(colors[iteration % len(colors)])
    
def at(x, y):
    t.penup()
    t.home()
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.pendown()

def heart(size, shape):
    t.pensize(5)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.right(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 14):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        
hearts()

t.penup()
t.goto(0,-100)
t.color("red")
t.write("Roses are red.", None, "center", "14pt bold")
t.goto(1,-125)
t.write("Violets are blue.", None, "center", "14pt bold")
t.goto(2,-150)
t.write("I like coding.", None, "center", "14pt bold")
t.goto(3,-175)
t.write("Do you do to?", None, "center", "14pt bold")
t.color("white")
t.goto(0,-300)
