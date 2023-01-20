import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()

player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_moving()
    car_manager.create_new_car()

    # Checking if the player touch the line
    if player.is_finish():
        scoreboard.increase_scoreboard()
        car_manager.increase_speed()

    # Checking if the player touch the car
    for car in car_manager.cars:
        if player.distance(car) < 23:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
