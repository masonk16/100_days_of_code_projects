from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card_timer = None


words = pandas.read_csv("data/french_words.csv")
word_dict = words.to_dict(orient="records")
current_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_word, card_timer
    window.after_cancel(card_timer)
    current_word = random.choice(word_dict)
    french_word = current_word["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(bg_img, image=front_img)
    card_timer = window.after(5000, func=show_answer)

def show_answer():
    canvas.itemconfig(bg_img, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = current_word["English"]
    canvas.itemconfig(card_word, text=english_word, fill="white")

def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

# >>>>UI SETUP<<<<< #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_timer = window.after(5000, func=show_answer)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
bg_img = canvas.create_image(400, 264, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 264, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(column=0, row=1)

# Right button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()
