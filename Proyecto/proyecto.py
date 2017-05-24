import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
A = turtle.Turtle()
A.speed(0)
A.color('violet')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(A,100,10)
S = turtle.Turtle()
S.speed(0)
S.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(S,100,10)
B = turtle.Turtle()
B.speed(0)
B.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(B,100,10)
T = turtle.Turtle()
T.speed(0)
T.color('red')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(T,100,10)
W = turtle.Turtle()
W.speed(0)
W.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(W,100,10)
print("bla")




import turtle
ab = turtle.Turtle()
ab.speed(0)
turtle.hideturtle()

turtle.left(75)
turtle.forward(50)

turtle.showturtle()
turtle.bgcolor("black")
turtle.penup()
for i in range(632):
    ab.forward(100)
    ab.right(1)
    ab.forward(25)
    ab.setpos(350,210)
    ab.left(1.57)
    ab.pencolor("skyblue")
print("dfbd")

import turtle
turtle.pencolor("black")
turtle.bgcolor("black")

def direccion(x1,x2):
    turtle.goto(x1,x2)

direccion(-180,180)
turtle.pencolor("yellow")

for i in range (13):
    turtle.fillcolor("yellow")
    turtle.forward(10)
    turtle.left(100)
    turtle.forward(10)
    turtle.right(40)
turtle.pencolor("black")
direccion(-250,-230)
turtle.pencolor("yellow")
for i in range (13):
    turtle.fillcolor("yellow")
    turtle.forward(10)
    turtle.left(100)
    turtle.forward(10)
    turtle.right(40)
turtle.pencolor("black")
direccion(190,-190)
turtle.pencolor("yellow")
for i in range (13):
    turtle.fillcolor("yellow")
    turtle.forward(10)
    turtle.left(100)
    turtle.forward(10)
    turtle.right(40)
print("dfd")















































import random
import turtle
from turtle import *
from random import randint, uniform

def random_move(turtle, distance):

  angle = uniform(-10,10)
  d = uniform(0,distance)
  turtle.left(angle)
  turtle.forward(d)

def randcolor():

  return (randint(0,255), randint(0,255), randint(0,255))

def gohome(turtle):

  turtle.penup()
  turtle.goto(0,0)
  turtle.pendown()

def random_walk(turtle, distance, steps):

  turtle.color(randcolor(), randcolor())
  for step in range(0,steps):
    random_move(turtle, distance)
  gohome(turtle)

def repeat(steps, trials):

  for trial in range(0,trials):
    random_walk(fred, 5, steps)

def saveImage(turtle, filename):

  ts = turtle.getscreen()
  tc = ts.getcanvas()
  tc.postscript(file=filename)

fred = Turtle()
fred.speed("fastest")
turtle.colormode(255)
N = 1000

fred.dot(10, "black")
repeat(1000, 20)

saveImage(fred, "fred1234.eps")
turtle.exitonclick()
turtle.mainloop()
print("45")
