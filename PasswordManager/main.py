from tkinter import *
from tkinter import messagebox
import random
import json

IS_OK = None

# messagebox is not class. So using * will not going to import module called messagebox


windows = Tk()
windows.title("Password Manager")
windows.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
symbols = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "/", "|", "{", "}", "]", "["]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def generate_password():
    password_list = []
    letters_count = random.randint(6, 9)
    symbol_count = random.randint(3, 5)
    number_count = random.randint(4, 6)
    for _ in range(letters_count):
        password_list.append(random.choice(letters))
    for _ in range(symbol_count):
        password_list.append(random.choice(symbols))
    for _ in range(number_count):
        password_list.append(random.choice(numbers))
    random.shuffle(password_list)
    password = ""
    for i in password_list:
        password += i
    password_input.insert(0, password)


def showing_pass():
    with open("user_data.json", "r") as file:
        pass_list = file.readlines()
    all_passwords = ""
    for all_pass in pass_list:
        all_passwords += all_pass
    messagebox.showinfo(title="All Passwords", message=f"Information: {all_passwords}")


def show_confirmation():
    messagebox.showinfo(title="Success", message="You have successfully added the new password for new website")


def search_info():
    web = website_input.get()
    try:
        with open("user_data.json", "r") as user_info:
            info = json.load(user_info)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data Found with website name, {web}")
    else:
        if web in info:
            email = info[web]["email"]
            passwd = info[web]["password"]
            messagebox.showinfo(title="Information", message=f"Email: {email}\n Password: {passwd}")
        else:
            messagebox.showinfo(title="Error", message=f"No Website Found with name, {web}")


def save():
    global IS_OK
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        IS_OK = messagebox.askokcancel(title="Confirmation",
                                       message=f"These are the details entered: \nEmail: {email} "f"\nPassword:{password} \nIt is ok to save?")
        if IS_OK:
            try:
                with open("user_data.json", "r") as file:
                    old_data = json.load(file)
            except:
                with open("user_data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                old_data.update(new_data)
                with open("user_data.json", "w") as file:
                    json.dump(old_data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
                email_input.delete(0, END)
    show_confirmation()

    # Message Box
    # messagebox.showinfo(title="Verification", message="Successfully?")


label1 = Label(text="Website")
label1.grid(row=1, column=0)
label2 = Label(text="Email")
label2.grid(row=2, column=0)
label3 = Label(text="Password")
label3.grid(row=3, column=0)
# label4 = Label(text="Show Passwords")
# label4.grid(row=5, column=1)

# User Entry

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
# email_input.insert(0, "anu@gmail.com")
password_input = Entry(width=25)
password_input.grid(row=3, column=1)
passwd_button = Button(text="Generate Password", width=20, command=generate_password)
passwd_button.grid(row=3, column=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=20, command=search_info)
search_button.grid(row=1, column=3)
show_files = Button(text="ShowFiles", width=30, command=showing_pass)
show_files.grid(row=5, column=1, columnspan=2)
windows.mainloop()
