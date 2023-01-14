from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
r_paddle.control("Up", "Down")
l_paddle.control("w", "s")

ball = Ball()
scoreboard = ScoreBoard()

state = True
while state:
    screen.update()
    time.sleep(0.01)
    ball.move()
    ball.bounce(r_paddle)
    ball.bounce(l_paddle)
    if ball.xcor() > 400:
        ball.home()
        scoreboard.l_add()
    elif ball.xcor() < -400:
        ball.home()
        scoreboard.r_add()

screen.exitonclick()