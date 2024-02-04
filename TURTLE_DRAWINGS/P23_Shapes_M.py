from turtle import Turtle,Screen,colormode
import random
colormode(255)
def setcolour():
    r=random.randint(1, 255)
    g=random.randint(1, 255)
    b=random.randint(1, 255)
    t=(r,g,b)
    return t
tim=Turtle()
tim.pensize(5)
tim.speed("fastest")
s=Screen()
def drawshapes(d):
    s=360/d
    for i in range(d):
        tim.color(setcolour())
        tim.forward(100)
        tim.left(s)
for i in range(3,11):       
        drawshapes(i)
s.exitonclick()