import tkinter as tk
import pyttsx3


def speak():
    text = entry.get()
    if text:
        engine.say(text)
        engine.runAndWait()


def clear():
    entry.delete(0, tk.END)


def update_speed(value):
    engine.setProperty('rate', int(value))


# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 135)

# GUI setup
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x220")


entry = tk.Entry(root, width=40, font=('Arial', 12))
entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

speak_button = tk.Button(button_frame, text="Speak", width=10, command=speak)
speak_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", width=10, command=clear)
clear_button.pack(side=tk.LEFT, padx=5)


root.mainloop()
