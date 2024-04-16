from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer_sleep = True
tick = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_sleep
    global reps
    global tick
    tick = ""
    timer_sleep = True
    reps = 1
    window.after(1000, texts_reset)

def texts_reset():
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_tick.config(text=tick)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer_sleep
    global reps
    global lbl_timer
    timer_sleep = False

    if reps % 8 == 0:
        round_time = int(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Long break", fg=RED)
    elif reps % 2 != 0:
        round_time = int(WORK_MIN * 60)
        lbl_timer.config(text="Work", fg=GREEN)
    else:
        round_time = int(SHORT_BREAK_MIN * 60)
        lbl_timer.config(text="Short break", fg=PINK)

    reps += 1
    count_down(round_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = 0
    sec = 0
    remainder = count % 60
    if count / 60 < 1:
        min = "00"
    elif (count / 60 >= 1) and (count / 60 < 10):
        min = "0" + str(int(count / 60))
    elif count / 60 >= 10:
        min = str(int(count / 60))

    if remainder < 10:
        sec = "0" + str(remainder)
    elif remainder >= 10:
        sec = str(remainder)

    time_formatted = f"{min}:{sec}"

    canvas.itemconfig(timer_text, text=time_formatted)
    if timer_sleep:
        pass
    elif count > 0:
        window.after(1000, count_down, count-1)
    else:
        global tick
        if reps % 2 == 1:
            tick += "✔"
            lbl_tick.config(text=tick)
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=2, column=2)

image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(100, 130,  text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

lbl_timer = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
lbl_timer.grid(row=1, column=2)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(row=3, column=1)

btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(row=3, column=3)

lbl_tick = Label(text=tick, fg=GREEN, font=(FONT_NAME, 15, "normal"), bg=YELLOW)
lbl_tick.grid(row=4, column=2)


mainloop()