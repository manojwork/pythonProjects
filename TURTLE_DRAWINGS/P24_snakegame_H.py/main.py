from turtle import Screen
from Snake import Snake
from Food import Food
from score import Score
import time
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.tracer(0)
snake=Snake()
food=Food()
score=Score()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Left")
s.onkey(snake.left, "Right")
race=True
while race:
    s.update()
    time.sleep(0.25)
    if  snake.move()==False:
        score.end()
        race=False
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extent()
        score.score+=1
        score.scoreboard()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        
        score.end()
        race=False  
    for seg in snake.segments:
        if seg==snake.head:
            pass
        elif(seg.distance(snake.head)<10):
            score.end()
            race=False       
with open("TURTLE_DRAWINGS/P24_snakegame_H.py/data.txt","w") as f:
                f.write(score.highscore)
         
s.exitonclick()