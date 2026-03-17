from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
reps = 1
current_card = {}
words_to_learn = {}

#==================== Reading the data file ====================#
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")
#==================== Functions ====================#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=new_image)
    flip_timer = window.after(3000, card_flip)

def right_pressed():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    words_to_learn = to_learn

    if current_card in words_to_learn:
        words_to_learn.remove(current_card)
        data = pd.DataFrame.from_dict(words_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=new_image)
    flip_timer = window.after(3000, card_flip)
    #print(current_card)


def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    current_image = canvas.itemcget(canvas_image, "image")

    if current_image == str(new_image):
        canvas.itemconfig(canvas_image, image=old_image)
    else:
        canvas.itemconfig(canvas_image, image=new_image)
    
#==================== UI Code ====================#
window = Tk()
window.title("Flash Quiz")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, card_flip)

#Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
new_image = PhotoImage(file="images/card_front.png")
old_image = PhotoImage(file="images/card_back.png")
card_background = canvas_image = canvas.create_image(400, 256, image=new_image)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, fill="black", font="Ariel 25 italic", text="")
card_word = canvas.create_text(400, 263, fill="black", font="Ariel 40 bold", text="")

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=right_pressed)
right_btn.grid(column=1, row=1)

#Labels
language = Label(text="Language", font=("Ariel", 40, "italic"), bg="#ffffff", height=2, width=8)
#language.grid(row=0, column=0, sticky="n")

next_card()

window.mainloop()