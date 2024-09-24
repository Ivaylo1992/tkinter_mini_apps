import tkinter as tk
import pyttsx3

engyne = pyttsx3.init()


# Creating the function which executes the whole functionality
def speaknow():
    engyne.say(textv.get())
    engyne.setProperty("rate", 115)  # Slowing down the speach rate
    engyne.runAndWait()
    engyne.stop()


root = tk.Tk()

textv = tk.StringVar()

# The outside label
obj = tk.LabelFrame(root, text="Text to speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# The inside label
lbl = tk.Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

# The text entry
text = tk.Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

# The button
btn = tk.Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

# Packing the whole root
root.title("Text to speech")
root.geometry("500x250")
root.resizable(False, False)

root.mainloop()
