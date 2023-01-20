from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
cars = []


def starting_position():
    number_of_cars = random.randint(3, 25)
    for _ in range(1, number_of_cars):
        car = Turtle()
        car.up()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.color(random.choice(COLORS))
        x_random = random.randint(-250, 250)
        y_random = random.randint(-250, 250)
        car.goto(x_random, y_random)
        cars.append(car)
    return cars


class CarManager:

    def __init__(self):
        self.cars = starting_position()
        self.speed = STARTING_MOVE_DISTANCE

    def car_moving(self):
        for car in self.cars:
            car.forward(self.speed)
        self.move_car()

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def move_car(self):
        for car in self.cars:
            if car.xcor() < -350:
                y_random = random.randint(-250, 250)
                car.goto(300, y_random)

    def create_new_car(self):
        is_one = random.randint(1, 10)
        if is_one == 1:
            car = Turtle()
            car.up()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(random.choice(COLORS))
            y_random = random.randint(-250, 250)
            car.goto(300, y_random)
            self.cars.append(car)
