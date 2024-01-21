from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 200

# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle north


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.goto(STARTING_POS)

    def finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
