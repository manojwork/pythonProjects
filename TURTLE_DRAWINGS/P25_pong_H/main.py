from turtle import Screen
from pabale import Pabale
from ball import Ball
from screen import Screens
import time
s=Screen()
s.tracer(0)
s.setup(800,600)
s.bgcolor("black")
p=Pabale((360,0))
p1=Pabale((-360,0))
ball=Ball()
def up():
    y=p.ycor()+20
    p.goto(p.xcor(),y)
def down():
    y=p.ycor()-20
    p.goto(p.xcor(),y)
def up1():
    y=p1.ycor()+20
    p1.goto(p1.xcor(),y)
def down1():
    y=p1.ycor()-20
    p1.goto(p1.xcor(),y)
s.listen()
s.onkey(up, "Up")
s.onkey(down, "Down")
s.onkey(up1, "w")
s.onkey(down1, "s")
sc=Screens()
race=True
while race:
    s.update()
    time.sleep(0.0096)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bouncey()
    if ball.xcor()>=p.xcor() and ball.distance(p)<50 or ball.xcor()>=p1.xcor() and ball.distance(p1)<50:
        ball.bouncex()   
    if ball.xcor()>400 :
        ball.refresh_r()
        sc.left+=1
        sc.up()
    if ball.xcor()<-400 :
        ball.refresh_l()
        sc.right+=1
        sc.up()    
s.exitonclick()