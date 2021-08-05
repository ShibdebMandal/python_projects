from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- PASSWORD FINDER ------------------------------- #
def find():
    website_name = (website_entry.get()).title()
    try:
        with open('data.json', 'r') as file:
            data_ii = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(title='Error', message='No Data File Found\n\nOr\n\nNo Data IN File Found')
    else:
        try:
            search_data = data_ii[website_name]
        except KeyError:
            messagebox.showerror('Error', f'No Details For Website {website_name} Exists')
        else:
            email_name = search_data['email']
            password_name = search_data['password']
            messagebox.showinfo(website_name, message=f"EMAIL:  {email_name}\nPASSWORD:  {password_name}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = (website_entry.get()).title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {"email": email,
             "password": password
             }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='oops', message="'Don't leave any entries empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"WEBSITE:  {website}\nEMAIL/USERNAME:  {email}\nPASSWORD:  {password}\n"
                                               f"\nIs ot ok to save?", )
        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            else:
                data.update(new_data)
            finally:
                with open('data.json', 'w') as file:
                    json.dump(obj=data, fp=file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.config(padx=50, pady=50, bg='white')
my_window.title('Password Manger')

my_canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_image = PhotoImage(file='logo.png')
my_canvas.create_image(100, 100, image=lock_image)
my_canvas.grid(row=0, column=1)

website_label = Label(text='Website:', bg='white')
website_label.grid(row=1, column=0)
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky='EW')
website_entry.focus()

email_label = Label(text='Email/Username:', bg='white')
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.insert(END, string='shibdebmandal@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')

password_label = Label(text='Password:', bg='white')
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky='EW')

search_button = Button(text='Search', bg='white', command=find)
search_button.grid(row=1, column=2, sticky='EW')
generate_button = Button(text='Generate Password', bg='white', command=generator)
generate_button.grid(row=3, column=2, sticky='EW')
add_button = Button(text='Add', bg='white', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

my_window.mainloop()
