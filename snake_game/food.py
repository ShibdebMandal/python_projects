from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('cyan')
        self.penup()
        self.refresh()

    def refresh(self):
        self.goto(x=random.choice(range(-270, 270, 20)), y=random.choice(range(-270, 270, 20)))

