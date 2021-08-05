from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for i in range(0, 3):
            pos = (i * (-20)), 0
            self.add_block(pos)

    def reset(self):
        for block in self.blocks:
            block.goto(-2000, -2000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]

    def add_block(self, position):
        block = Turtle(shape='square')
        block.penup()
        block.goto(position)
        block.color('white')
        self.blocks.append(block)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def move(self):
        for block_index in range(len(self.blocks) - 1, 0, -1):
            x = self.blocks[block_index - 1].xcor()
            y = self.blocks[block_index - 1].ycor()
            self.blocks[block_index].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
