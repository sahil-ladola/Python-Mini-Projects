from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen. No cars should be generated in the top
# and bottom 50px of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_new_car(self):
        random_gen = random.randint(1, 6)
        if random_gen == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
