from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label1.config(text="Timer", fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counting():
    global reps
    reps += 1
    true = True
    work_sec = round(WORK_MIN * 60)
    short_break_sec = round(SHORT_BREAK_MIN * 60)
    long_break_sec = LONG_BREAK_MIN * 60

    #2nd/4th/6th
    if reps % 2 == 0 and reps < 7:
        countdown(short_break_sec)
        label1.config(text="Short Break", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=PINK)
        print(reps)
    #8th
    elif reps == 8:
        label1.config(text="Long Break", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=RED)
        countdown(long_break_sec)
        print(reps)
        reps = 0
    #1st/3rd/5th/7th
    else:
        label1.config(text="Working", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 0:
        count_sec = f"0{count % 60}"

    if count > 0:
       timer = window.after(1000, countdown, count-1)
    elif count == 0:
        start_counting()
        if reps == 2:
            checkmark.config(text="✔")
        elif reps == 4:
            checkmark.config(text="✔✔")
        elif reps == 6:
            checkmark.config(text="✔✔✔")
        elif reps == 8:
            checkmark.config(text="✔✔✔✔")
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
poms = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=poms)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

#Labels
label1 = Label(text="Timer", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

checkmark = Label(font=(20), bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

#Buttons
Start_button = Button(text="Start", command=start_counting, highlightthickness=0)
Start_button.grid(column=0, row=2)

Reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer   )
Reset_button.grid(column=2, row=2)

window.mainloop()