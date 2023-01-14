from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0 
        self.update()

    def update(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(f"{self.l_score}", True, align="center", font=("Calibri", 45, "normal"))
        self.setpos(100, 200)
        self.write(f"{self.r_score}", True, align="center", font=("Calibri", 45, "normal"))

    def r_add(self):
        self.r_score += 1 
        self.update()

    def l_add(self):
        self.l_score += 1 
        self.update() 