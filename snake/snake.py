from turtle import Turtle, Screen 
screen = Screen()
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
RIGHT = 0 
LEFT = 180 
DOWN = 270

class Snake():
    
    def __init__(self):
        self.segments = []
        self.parts = -1
        for position in POSITIONS:
            self.add(position)
        self.head = self.segments[0]

    def control(self):
        def up():
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def right():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        def left():
           if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        def down():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def close():
            screen.bye()
        
        screen.onkey(up, "w")
        screen.onkey(right, "d")
        screen.onkey(left, "a")
        screen.onkey(down, "s")
        screen.onkey(close, "space")


    def move(self):
        for num in range(self.parts, 0, -1):
            self.segments[num].setpos(self.segments[num - 1].xcor(), self.segments[num - 1].ycor())
        self.head.forward(20)

    def walls(self):
        return (self.head.xcor() < -280 or self.head.xcor() > 280) or (self.head.ycor() < -280 or self.head.ycor() > 280) 
        
    def heads(self):    
        for x in self.segments:
            if x == self.head:
                pass
        else:
            return self.head.distance(x) < 10

    def add(self, position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.setpos(position)
        self.segments.append(part)
        self.parts += 1 

    def extend(self):
        self.add(self.segments[-1].pos())