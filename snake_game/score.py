from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.high_score}", False, align='center',
                   font=('Arial', 15, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align='center', font=('Arial', 20, 'bold'))
