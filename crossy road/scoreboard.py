
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update()

    def update(self):
        self.clear()
        self.setpos(-200, 250)
        self.level += 1
        self.write(f"Level: {self.level}", True, align="center", font=("Courier", 24, "normal"))
    
    def end_game(self):
        self.setpos(0, 0)
        self.write(f"Game over", True, align="center", font=("Courier", 24, "normal"))
