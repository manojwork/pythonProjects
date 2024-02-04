from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.refresh()
    def refresh(self):
        x=random.randint(-260,260)
        y=random.randint(-260,260)
        self.goto(x,y)