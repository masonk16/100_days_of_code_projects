from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
svombonoro = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=svombonoro)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", pady=10)
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", pady=10)
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", pady=10)
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(column=2, row=3)

add_pass_button = Button(text="Add Password", width=36)
add_pass_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
