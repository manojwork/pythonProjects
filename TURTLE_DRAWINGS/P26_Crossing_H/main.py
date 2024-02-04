import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
p=Player()
car=CarManager()
sc=Scoreboard()
screen.listen()
screen.onkey(p.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    if p.ycor()>300:
        p.levelup()
        car.increase_sp()
        sc.update_score()
    for i in car.allcars:
        if p.distance(i)<20:
            sc.over()
            game_is_on=False
        
screen.exitonclick()