import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
repetition = 0
timer_running = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global repetition, timer_running
    window.after_cancel(timer_running)
    repetition = 0
    canvas.itemconfig(timer, text="00:00")
    headline.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetition
    repetition += 1

    if repetition % 8 == 0:
        headline.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif repetition % 2 == 0:
        headline.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        headline.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_running

    count_min = math.floor(count / 60) #Only takes last whole number
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer_running = window.after(1000, count_down, count - 1 )
    else:
        start_timer()
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