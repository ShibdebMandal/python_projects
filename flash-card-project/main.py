from tkinter import *
from random import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"
french_words_df = pandas.read_csv('data/french_words.csv')
length_of_words = len(french_words_df.index)
french_word = french_words_df.iloc[randint(0, length_of_words-1), 0]


def next_word():
    global title_text, word_text, french_word, flip
    my_window.after_cancel(flip)
    my_canvas.delete(title_text)
    my_canvas.delete(word_text)
    french_word = french_words_df.iloc[randint(0, 100), 0]
    my_canvas.create_image(400, 263, image=front_img)
    title_text = my_canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'))
    word_text = my_canvas.create_text(400, 263, text=french_word, font=('Ariel', 60, 'bold'))
    flip = my_window.after(3000, to_english)


def to_english():
    global title_text, word_text, french_word, french_words_df
    my_canvas.delete(title_text)
    my_canvas.delete(word_text)
    for i in range(0,length_of_words):
        iter_word = french_words_df.loc[i,'French']
        if iter_word==french_word:
            english_word = french_words_df.loc[i,'English']
            my_canvas.create_image(400, 263, image=back_img)
            title_text = my_canvas.create_text(400, 150, text='English', fill='white', font=('Ariel', 40, 'italic'))
            word_text = my_canvas.create_text(400, 263, text=english_word, fill='white', font=('Ariel', 60, 'bold'))


my_window = Tk()
my_window.title('Flashy')
my_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = my_window.after(3000, to_english)

back_img = PhotoImage(file='images/card_back.png')
front_img = PhotoImage(file='C:/Users/USER/PycharmProjects/flash-card-project-start/images/card_front.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

my_canvas = Canvas(my_window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_canvas.create_image(400, 263, image=front_img)
my_canvas.grid(row=0, columnspan=2)

right_button = Button(my_window, command=next_word, image=right_img, relief=FLAT, bg=BACKGROUND_COLOR,
                      highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_button = Button(my_window, command=next_word, image=wrong_img, relief=FLAT, bg=BACKGROUND_COLOR,
                      highlightthickness=0)
wrong_button.grid(row=1, column=0, )

title_text = my_canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
word_text = my_canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))



my_window.mainloop()
