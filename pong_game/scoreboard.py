from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-20, 260)
        self.write(self.left_score, False, 'center', ('Arial', 25, 'bold'))
        self.goto(20, 260)
        self.write(self.right_score, False, 'center', ('Arial', 25, 'bold'))

    def left_score_increase(self):
        self.left_score += 1
        self.update_score()

    def right_score_increase(self):
        self.right_score += 1
        self.update_score()
