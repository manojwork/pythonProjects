FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score=0
        self.write_score()
    def write_score(self):
        self.clear()
        self.goto(-250,250)
        self.write(f" level : {self.score} ",align="left",font=FONT)
    def update_score(self):
        self.score+=1
        self.write_score()
    def over(self):
        self.clear()
        self.goto(0,0)
        self.write(f" GAME OVER ! ",align="center",font=FONT)
 