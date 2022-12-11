from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_bg = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 260, image=flash_bg)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()
