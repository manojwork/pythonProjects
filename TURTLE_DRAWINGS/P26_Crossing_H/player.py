STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.starting()
        self.setheading(90)
    def starting(self):
        self.goto(STARTING_POSITION)
    def levelup(self):
        self.starting()
    def up(self):
        self.forward(MOVE_DISTANCE)