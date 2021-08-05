from turtle import Turtle, Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_score = Scoreboard()
my_screen.tracer(0)
my_screen.setup(width=800, height=600)
my_screen.bgcolor('black')
my_screen.title('Pong')
right_paddle = Paddle(360, 0)
left_paddle = Paddle(-360, 0)
mid_line = Paddle(0, 0)
mid_line.shapesize(stretch_wid=40, stretch_len=0.3)
ball = Ball()

my_screen.listen()
my_screen.onkeypress(fun=right_paddle.up, key="Up")
my_screen.onkeypress(fun=right_paddle.down, key="Down")
my_screen.onkeypress(fun=left_paddle.up, key="w")
my_screen.onkeypress(fun=left_paddle.down, key="s")
my_screen.onkey(fun=ball.pause, key='p')
my_screen.onkey(fun=ball.restart, key='m')
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()
    if (ball.xcor() > 330 or ball.xcor() < -330) and (
            ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50):
        ball.hit_paddle()
    if ball.xcor() > 370:
        ball.reset_position()
        my_score.left_score_increase()
    elif ball.xcor() < -370:
        ball.reset_position()
        my_score.right_score_increase()

my_screen.exitonclick()
