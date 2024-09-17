import tkinter as tk
from textblob import TextBlob

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")


def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())

    cs = tk.Label(
        root,
        text="Correct text is:",
        font=("poppins", 20),
        bg="#dae6f6",
        fg="#364971",
    )

    cs.place(x=100, y=250)
    spell.config(text=right)


heading = tk.Label(
    root,
    text="Spelling Checker",
    font=("Trebuchet MS", 30, "bold"),
    bg="#dae6f6",
    fg="#364971",
)

heading.pack(pady=(50, 0))

enter_text = tk.Entry(
    root,
    justify="center",
    width=30,
    font=("poppins", 25),
    bg="white",
    border=2,
)

enter_text.pack(pady=10)
enter_text.focus()

button = tk.Button(
    root,
    text="Check",
    font=("arial", 20, "bold"),
    fg="white",
    bg="red",
    command=check_spelling
)

button.pack()

spell = tk.Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

root.mainloop()
