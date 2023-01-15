from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

tim = Player()
tim.control()

scoreboard = Scoreboard()

car = Car()
speed = 5

state = True
while state:

    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move(speed)

    for mashina in car.cars:
        if tim.distance(mashina) < 25:
            scoreboard.end_game()
            state = False

    if tim.finish() == True:
        scoreboard.update()
        speed += 10


screen.exitonclick()