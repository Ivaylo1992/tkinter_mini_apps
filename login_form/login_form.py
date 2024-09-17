from tkinter import *
from tkinter import messagebox


def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" and password == "":
        messagebox.showinfo("Warning!", "Blank not allowed")

    elif username == "some_user" and password == "some_password": #put your credentials here
        messagebox.showinfo("Welcome!", "Login successful")

    else:
        messagebox.showinfo("Error!", "Invalid credentials")


root = Tk()
root.title("Login")
root.geometry("300x200")

global entry1
global entry2

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry1 = Entry(root, bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(root, bd=5)
entry2.place(x=140, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120)

root.mainloop()
