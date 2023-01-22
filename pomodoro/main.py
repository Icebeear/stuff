PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SHORT_BREAK_SEC = 300
LONG_BREAK_SEC = 1200
WORK_SEC = 1500
REPS = 0 
entity = None


import tkinter 
import math 

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(bg=YELLOW, width=200, height=224, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.grid(column=1, row=1)

label = tkinter.Label(text="Timer", bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 50))
label.grid(column=1, row=0)

timer = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

marks = ""
mark = tkinter.Label(bg=YELLOW, fg=GREEN, font=(35))
mark.grid(column=1, row=3)


def count(time):
    global REPS
    global entity
    mins = math.floor(time / 60)
    sec = time % 60 
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer, text=f"{mins}:{sec}")
    if time == 0:
        REPS += 1
        start_timer()
        return
    entity = window.after(1000, count, time - 1)


def start_timer():
    global marks
    global REPS
    if REPS in [0, 2, 4, 6]:
        count(WORK_SEC)
        label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50))
    elif REPS in [1, 3, 5]:
        count(SHORT_BREAK_SEC)
        label.config(text="Brake", fg=PINK, font=(FONT_NAME, 50))
        marks += "✔"
        mark.config(text=marks)
    else:
        REPS = -1
        count(LONG_BREAK_SEC)
        label.config(text="Long Brake", fg=RED, font=(FONT_NAME, 35))
        marks += "✔"
        mark.config(text=marks)


def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(entity)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50))
    mark.config(text="")
    

start = tkinter.Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)


window.mainloop()