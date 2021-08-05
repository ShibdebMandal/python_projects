from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.levelboard()

    def levelboard(self):
        self.goto(-280, 260)
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.write(f'Level:{self.level}', False, 'left', FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', FONT)

    def level_up(self):
        self.clear()
        self.level += 1
