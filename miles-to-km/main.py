from tkinter import *

my_window = Tk()
my_window.minsize(width=150, height=150)
my_window.title('Miles to Kilometer')
my_window.config(padx=20, pady=20)

miles_label = Label(text='miles', font=('Ariel', 15, 'bold'))
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)
equal_label = Label(text='is equal to', font=('Ariel', 15, 'bold'))
equal_label.grid(row=1, column=0)
equal_label.config(padx=10, pady=10)
km_int_label = Label(text='0', font=('Ariel', 15, 'bold'))
km_int_label.grid(row=1, column=1)
km_int_label.config(padx=10, pady=10)
km_label = Label(text='km', font=('Ariel', 15, 'bold'))
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)


def m_to_k():
    ml = int(my_inbox.get())
    km = int(ml * 1.6)
    km_int_label.config(text=str(km))


my_button = Button(text='calculate', command=m_to_k)
my_button.grid(row=2, column=1)
my_button.config(padx=10, pady=10)

my_inbox = Entry(width=10)
my_inbox.insert(END, string='0')
my_inbox.grid(row=0, column=1)

my_window.mainloop()