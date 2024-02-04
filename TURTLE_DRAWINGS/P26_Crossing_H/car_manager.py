COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.allcars=[]
        self.move_speed=STARTING_MOVE_DISTANCE
    def move(self):
        a=random.randint(1, 6)
        if a==1:
            car=Turtle()
            car.shape("square")
            car.shapesize(1,2)
            car.penup()
            car.color(random.choice(COLORS))
            y=random.randint(-260,260)
            car.goto(300,y)
            self.allcars.append(car)
            y=0
        for i in self.allcars:
            i.backward(self.move_speed)
    
    def increase_sp(self):
        self.move_speed+=MOVE_INCREMENT
    
