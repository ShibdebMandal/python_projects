import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
pl = Player()
car_manager = CarManager()
my_scoreboard = Scoreboard()
screen.onkey(fun=pl.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if pl.is_crossed():
        pl.goto(0,-280)
        car_manager.level_up()
        my_scoreboard.level_up()
        my_scoreboard.levelboard()
    for car in car_manager.all_cars:
        if car.distance(pl)<20:
            my_scoreboard.game_over()
            game_is_on=False



screen.exitonclick()