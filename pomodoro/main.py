from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    my_window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    check_label.config(text='')
    my_canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    #print(reps)
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    if count_min < 10:
        count_min = f'0{count_min}'
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    my_canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = my_window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = reps//2
        check_mark = ''
        for c in range(work_session):
            check_mark += '✔'
        check_label.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #


my_window = Tk()
my_window.title('POMODORO')
my_window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file='tomato.png')
my_canvas.create_image(100, 112, image=pomodoro_img)
timer_text = my_canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 20, 'bold'))
my_canvas.grid(row=1, column=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text='Reset', command=timer_reset)
reset_button.grid(row=2, column=2)

check_label = Label(font=('Segoe UI Symbol', 20, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

my_window.mainloop()
