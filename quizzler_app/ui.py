from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "normal"))
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(150, 125, text="Question goes here.", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        true_mark = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_mark, highlightthickness=0,  padx=20, pady=20)
        self.true_btn.grid(column=0, row=2)

        false_mark = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_mark, highlightthickness=0, padx=20, pady=20)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()
