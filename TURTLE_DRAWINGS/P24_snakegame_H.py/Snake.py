from turtle import Turtle
position=[(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments=[]
        self.add()
        self.head=self.segments[0]
    def add(self):
        for i in range(3):
            self.create(position[i])
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.head.forward(20)         
    def create(self,position):
        tim=Turtle()
        tim.shape("square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)
    def extent(self):
        self.create(self.segments[-1].position())
        
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(0)
    def right(self):
        self.head.setheading(180)