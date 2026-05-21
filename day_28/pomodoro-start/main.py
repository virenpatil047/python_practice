from tkinter import *
from pathlib import Path

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_IMG = Path(__file__).parent / "tomato.png"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    global reps
    reps += 1
    if reps % 8 == 0: 
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count >= 0:
        min = count // 60
        sec = count % 60
        canvas.itemconfig(timer_text, text=f"{min}:{sec if sec > 9 else '0' + str(sec)}")
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        if reps % 2 == 0:
            tick.config(text="✔" * (reps // 2))
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=TOMATO_IMG)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "normal"))
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

tick = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
tick.grid(row=3, column=1)

window.mainloop()
