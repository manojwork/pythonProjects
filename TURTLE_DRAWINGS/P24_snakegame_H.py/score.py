from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("TURTLE_DRAWINGS/P24_snakegame_H.py/data.txt","r") as f:
            self.highscore=f.read()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.scoreboard()
    def scoreboard(self):
        self.clear()
        self.goto(0,260)
        self.write(f" score : {self.score} ",align="center",font=FONT)
    def inc(self):
        self.score+=1
        self.scoreboard()
    def end(self):
        self.goto(0,0)
        self.color("white")
        self.write(f" game over .",align="center",font=FONT)
   