from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
# ------------------------------------ Functions -------------------------------------
current_data = {}
words = {}
try:
    data = pandas.read_csv("data/yet_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/de_to_en.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_word():
    global current_data, flip_timer
    window.after_cancel(flip_timer)
    current_data = random.choice(words)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_data["German"], fill="black")
    canvas.itemconfig(card_background, image=bg_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_data["English"], fill="white")
    canvas.itemconfig(card_background, image=bg_back_image)


def learn_word():
    words.remove(current_data)
    data = pandas.DataFrame(words)
    data.to_csv("data/yet_to_learn.csv", index=False)
    next_word()


# ------------------------------------ UI -------------------------------------


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# bg image
canvas = Canvas(width=800, height=526)
bg_front_image = PhotoImage(file="images/card_front.png")
bg_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=bg_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# text
card_title = canvas.create_text(400, 150, font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 270, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# right / wrong buttons
right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=next_word)
right_btn.grid(row=1, column=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=learn_word)
wrong_btn.grid(row=1, column=0)

next_word()

window.mainloop()
