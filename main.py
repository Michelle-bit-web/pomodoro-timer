import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(
    100,
    130,
    text="00:00",
    font=(FONT_NAME, 35, "bold"),
    justify="center",
    fill="white")
canvas.grid(column=1, row=1)

#Buttons
def start_timer():
    print('started')

def reset_timer():
    print('reset')

start_button = tkinter.Button(text="Start", command=start_timer)
reset_button = tkinter.Button(text="Reset", command=reset_timer)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

#Label
headline = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, justify="center")
headline.grid(column=1, row=0)

check_mark = tkinter.Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=2)

window.mainloop()