from score import Score
from snake import Snake
from turtle import Screen
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)
my_snake = Snake()
my_food = Food()
my_score = Score()
screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key='Down')
screen.onkey(fun=my_snake.left, key='Left')
screen.onkey(fun=my_snake.right, key='Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    my_snake.move()

    if my_snake.head.distance(my_food) < 15:
        my_food.refresh()
        my_score.increase_score()
        my_snake.extend()

    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        my_snake.reset()
        my_score.reset()

    for block in my_snake.blocks[1:]:
        if my_snake.head.distance(block) < 15:
            my_snake.reset()
            my_score.reset()

screen.exitonclick()
