import random
from turtle import Turtle,Screen,colormode
colormode(255)
def setcolour():
    r=random.randint(1, 255)
    g=random.randint(1, 255)
    b=random.randint(1, 255)
    t=(r,g,b)
    return t
tim=Turtle()
s=Screen()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(400)
tim.setheading(0)

for i in range(1,101):
    tim.dot(15,setcolour())
    tim.forward(50)
    if i%10==0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)
s.exitonclick()