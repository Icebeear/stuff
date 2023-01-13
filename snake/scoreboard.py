from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0 
        self.add()
        
    def add(self):
        self.score += 1
        self.setpos(0, 270)
        self.clear()
        self.write(f"Score: {self.score}", True, align="center", font=("Calibri", 20, "normal"))

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game over", True, align="center", font=("Times new roman", 25, "normal"))
        