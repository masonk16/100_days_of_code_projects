from tkinter import *


def calculate():
    my_label["text"] = input.get()


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Entry
input = Entry(width=15)
input.grid(column=3, row=2)

# Labels
label_1 = Label(text="Miles", font=("Arial", 14, "italic"))
label_1.grid(column=4, row=2)
label_1.config(padx=10, pady=10)

label_2 = Label(text="is equal to", font=("Arial", 14, "italic"))
label_2.grid(column=2, row=3)
label_2.config(padx=10, pady=10)

label_3 = Label(text="0", font=("Arial", 14, "italic"))
label_3.grid(column=3, row=3)
label_3.config(padx=10, pady=10)

label_4 = Label(text="Km", font=("Arial", 14, "italic"))
label_4.grid(column=4, row=3)
label_4.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=4)


window.mainloop()
