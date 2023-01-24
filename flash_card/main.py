import tkinter
import pandas 
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    words = data.to_dict(orient="records")

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


def next_card():
    global current_card, flip_timer
    if len(words) == 0:
        canvas.itemconfig(language, text="Good", fill="black")
        canvas.itemconfig(word, text="Job", fill="black")
        btn_right.config(state=["disabled"])
        btn_wrong.config(state=["disabled"])
        window.after_cancel(flip_timer)
    else:
        window.after_cancel(flip_timer)
        current_card = random.choice(words)
        canvas.itemconfig(card, image=card_front)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)
    

def is_known():
    words.remove(current_card)
    df = pandas.DataFrame(words)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


right = tkinter.PhotoImage(file="./images/right.png")
btn_right = tkinter.Button(image=right, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=1)

wrong = tkinter.PhotoImage(file="./images/wrong.png")
btn_wrong = tkinter.Button(image=wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(column=0, row=1)


flip_timer = window.after(3000, flip_card)
next_card()
window.mainloop()