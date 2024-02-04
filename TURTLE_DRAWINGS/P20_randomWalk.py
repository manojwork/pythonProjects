from turtle import Turtle,Screen,colormode
import random
colormode(255)
def setcolour():
    r=random.randint(1, 255)
    g=random.randint(1, 255)
    b=random.randint(1, 255)
    t=(r,g,b)
    return t
dict=[90,180,270]
tim=Turtle()
tim.pensize(5)
tim.speed("fastest")
s=Screen()

for i in range(200):
    tim.pensize(5)
    tim.color(setcolour())
    tim.forward(10)
    tim.setheading(random.choice(dict))
    
s.exitonclick()        
        