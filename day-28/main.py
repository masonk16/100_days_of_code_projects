from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("ChiGUI Chekutanga!")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label!", font=("Arial", 24, "italic"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)

# Button
button = Button(text="Ndipfanye", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Ndipfanyewo", command=button_clicked)
button2.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
