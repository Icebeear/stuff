from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

apple = Food()
snake = Snake()
scoreboard = Scoreboard()
snake.control()

state = True 
while state:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    
    if (snake.walls() or snake.heads()) == True:
        state = False
        scoreboard.game_over()

    if (snake.head.distance(apple)) <= 10:
        apple.move()
        scoreboard.add()
        snake.extend()

screen.exitonclick()