from tkinter import *


def calculate():
    result = round(int(miles_input.get()) * 1.609)
    result_label.config(text=result)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=15)
miles_input.grid(column=3, row=2)

# Labels
miles_label = Label(text="Miles", font=("Arial", 14, "italic"))
miles_label.grid(column=4, row=2)
miles_label.config(padx=10, pady=10)

equal_to_label = Label(text="is equal to", font=("Arial", 14, "italic"))
equal_to_label.grid(column=2, row=3)
equal_to_label.config(padx=10, pady=10)

result_label = Label(text="0", font=("Arial", 14, "italic"))
result_label.grid(column=3, row=3)
result_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 14, "italic"))
km_label.grid(column=4, row=3)
km_label.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=4)


window.mainloop()
