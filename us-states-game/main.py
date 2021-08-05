import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title('US states game')
turtle.penup()
turtle.hideturtle()

image = 'blank_states_img.gif'
my_screen.bgpic(image)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()


def visualize(answer, states, color):
    if answer in states:
        if answer not in guessed_states:
            guessed_states.append(answer)
            index = states.index(answer)
            ans_x = x_cor[index]
            ans_y = y_cor[index]
            turtle.goto(ans_x, ans_y)
            turtle.color(color)
            turtle.write(answer)


guessed_states = []
while len(guessed_states) < 50:
    answer = my_screen.textinput(f'{len(guessed_states)}/50 States correct', 'Guess next state').title()
    if answer == 'End':
        missing_states = [state for state in states if state not in guessed_states]
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv('states to learn')
        for state in states:
            visualize(state, states, 'red')
        break
    visualize(answer, states, 'blue')
turtle.mainloop()