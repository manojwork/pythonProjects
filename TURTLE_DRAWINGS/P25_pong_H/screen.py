from turtle import Turtle
class Screens(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.left=0
        self.right=0
        self.penup()
        self.hideturtle()
        self.up()
    def up(self):
        self.clear()
        self.goto(100,200)
        self.write(self.right,align="center",font=("Courier",80,"normal"))
        self.goto(-100,200)
        self.write(self.left,align="center",font=("Courier",80,"normal"))
        self.goto(0,360)
        self.setheading(270)
        self.pensize(5)
        for i in range(100):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()