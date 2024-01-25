import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate_new_car()
    car_manager.move()

    # detect player collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False
    # detect player reach finish line
    if player.finish_line():
        player.start()
        car_manager.level_up()
        score.increase_level()


screen.exitonclick()

