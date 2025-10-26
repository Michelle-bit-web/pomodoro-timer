import tkinter
from tkinter import *
import time

from pycparser.c_ast import While

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    print('reset')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1 )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(
    100,
    130,
    text="00:00",
    font=(FONT_NAME, 35, "bold"),
    justify="center",
    fill="white")
canvas.grid(column=1, row=1)

#Buttons
start_button = tkinter.Button(text="Start", command=start_timer, border=0, bg="#E6D8C3")
reset_button = tkinter.Button(text="Reset", command=reset_timer, border=0, bg="#E6D8C3")

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

#Label
headline = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, justify="center")
headline.grid(column=1, row=0)

check_mark = tkinter.Label(text="✔", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=2)

window.mainloop()