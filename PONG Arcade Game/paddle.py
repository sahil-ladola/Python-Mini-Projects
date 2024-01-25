from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
