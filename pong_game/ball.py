from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.ball_speed = 0.15
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        ney_x = self.xcor() + self.x_move
        ney_y = self.ycor() + self.y_move
        self.goto(ney_x, ney_y)

    def pause(self):
        self.ball_speed = 10

    def restart(self):
        self.ball_speed = .15

    def hit_wall(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        '''Give direction as -1 or +1 '''
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.15
