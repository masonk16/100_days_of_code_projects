from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR)
flash_bg = PhotoImage(file="/images/card_front.png")
canvas.create_image(400, 200, image=flash_bg)

window.mainloop()
