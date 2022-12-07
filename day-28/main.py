from tkinter import *

window = Tk()
window.title("ChiGUI Chekutanga!")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a label!", font=("Arial", 24, "italic"))
my_label.pack()


# Button
def button_clicked():
    my_label["text"] = "Button rapfanywa!"


button = Button(text="Click me!", command=button_clicked)
button.pack()

#Entry


window.mainloop()
