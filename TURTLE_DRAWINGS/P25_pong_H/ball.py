from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=1
        self.y=1
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    def bouncey(self):
            self.y*=-1
    def bouncex(self):
            self.x*=-1
    def refresh_r(self):
        self.goto(0,0)
        self.bouncex()
    def refresh_l(self):
        self.goto(0,0)
        self.bouncey()