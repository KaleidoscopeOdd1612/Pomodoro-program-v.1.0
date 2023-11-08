from tkinter import *
from tkinter import messagebox
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2 #15
SHORT_BREAK_MIN = 1 #3
LONG_BREAK_MIN = 3 #12
repeat = 0
time = 0
clock = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(clock)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    time_check.config(text="")
    global repeat
    repeat = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global repeat, time
    repeat += 1
    if repeat % 2 == 1:
        timer_text.config(text="WORK", fg=GREEN)
        time = WORK_MIN
    elif repeat % 2 == 0:
        timer_text.config(text="BREAK", fg=PINK)
        time = SHORT_BREAK_MIN
    if repeat % 7 == 0:
        timer_text.config(text="BE FREE!", fg=RED)
        time = LONG_BREAK_MIN
        repeat = 0
    count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:
        global clock
        clock = window.after(1000, count_down, count-1)
    else:
        start_time()
        checker = ""
        for _ in range(math.floor(repeat/2)):
            checker += "✓"
        time_check.config(text=checker)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

# Label
timer_text = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(column=1, row=0)
time_check = Label(font=(FONT_NAME, 20, "bold"), fg=PINK, bg=YELLOW)
time_check.grid(column=1, row=3)

# Button
start = Button(text="Start", width=10, command=start_time)
start.grid(column=0, row=2)
reset = Button(text="Reset", width=10, command=reset)
reset.grid(column=2, row=2)

window.mainloop()