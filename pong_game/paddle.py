from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def up(self):

        ney_y = self.ycor() + 30
        self.goto(self.xcor(), ney_y)

    def down(self):
        ney_y = self.ycor() - 30
        self.goto(self.xcor(), ney_y)
