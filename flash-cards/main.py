from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

#>>>> WORD DATA <<<<<#
words = pandas.read_csv("data/french_words.csv")
#print(words)



# >>>>UI SETUP<<<<< #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 264, image=front_img)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 264, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

# Right button
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)


window.mainloop()
