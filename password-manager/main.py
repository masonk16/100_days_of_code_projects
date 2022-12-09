from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """
    Saves the new password as a new line in the file when the Add Password button is clicked.

    Clears website and password fields after button press.
    """

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="HAAAA Mdhara!", message="Hapana zvamanyora ka")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are your password deatils:\n Email: {email}\n"
                                                      f"Password: {password}\n Is it okay to save?")

        if is_ok:

            with open("svombonorodzenyu.txt", "a") as masvombonoro:
                masvombonoro.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
svombonoro = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=svombonoro)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:", pady=10)
website_label.grid(column=0, row=1)

website_input = Entry(width=55)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

# Email
email_label = Label(text="Email/Username:", pady=10)
email_label.grid(column=0, row=2)

email_input = Entry(width=55)
email_input.insert(0, "kudyausavi@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

# Password
password_label = Label(text="Password:", pady=10)
password_label.grid(column=0, row=3)

password_input = Entry(width=35)
password_input.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password")
gen_pass_button.grid(column=2, row=3)

add_pass_button = Button(text="Add Password", width=46, command=save)
add_pass_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
