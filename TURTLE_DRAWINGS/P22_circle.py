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
def drawcircles(d):
    for i in range(360//d):
        tim.color(setcolour())
        tim.circle(100)
        tim.setheading(tim.heading()+d)
drawcircles(10)
s.exitonclick()        
        