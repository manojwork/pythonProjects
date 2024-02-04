from turtle import Turtle,Screen
import random
colors=["red","brown","blue","green","orange","black"]
y=[-80,-40,20,60,100,140]
s=Screen()
all_turtles=[]
s.setup(width=400,height=400)
race=False
user_input=s.textinput("turtle race", " guess the winner : ")
for i in range(6):
    tim=Turtle("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-180,y[i])
    all_turtles.append(tim)
if user_input:
    race=True
while race:
    for i in all_turtles:
        if i.xcor()>180:
            race=False
            if user_input==i.pencolor():
                print(f" you won! {i.pencolor()} won the match  .")
            else:
                print(f" you loss! {i.pencolor()} won the match  .")
        i.pensize(5)
        i.pendown()
        i.forward(random.randint(1, 10))

s.exitonclick()