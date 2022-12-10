from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generates a strong password and inputs into the paswword textbox."""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += ([choice(letters) for _ in range(randint(8, 10))])
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """
    Saves the new password as a new line in the file when the Add Password button is clicked.

    Clears website and password fields after button press.
    """

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="HAAAA Mdhara!", message="Hapana zvamanyora ka")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are your password deatils:\n Email: {email}\n"
        #                                               f"Password: {password}\n Is it okay to save?")
        #
        # if is_ok:
        try:
            with open("svombonorodzenyu.json", "r") as masvombonoro:
                # Reading old data
                data = json.load(masvombonoro)
        except FileNotFoundError:
            with open("svombonorodzenyu.json", "w") as masvombonoro:
                # Saving updated data
                json.dump(new_data, masvombonoro, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("svombonorodzenyu.json", "w") as masvombonoro:
                # Saving updated data
                json.dump(data, masvombonoro, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- SEARCH BTN ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("svombonorodzenyu.json", "r") as masvombonoro:
            svombonorodziripo = json.load(masvombonoro)
            email = svombonorodziripo[website]["email"]
            password = svombonorodziripo[website]["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="No data", message="No data in file.")
    except KeyError:
        messagebox.showinfo(title="No password", message="Password does not exist.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")


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

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)


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

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)

add_pass_button = Button(text="Add Password", width=46, command=save)
add_pass_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
