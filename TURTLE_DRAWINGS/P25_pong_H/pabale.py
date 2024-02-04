from turtle import Turtle
class Pabale(Turtle):
    def __init__(self,tu):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.goto(tu)