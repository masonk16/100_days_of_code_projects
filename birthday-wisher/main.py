import pandas
import datetime as dt
import random
import smtplib

EMAIL = "mabasics175@gmail.com"
PASSWORD = "wllaqeaotxnaitmu"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# Read csv into dataframe
birthdays = pandas.read_csv("birthdays.csv")

# Obtain date and check against birthdays
now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)



letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

if birth_day is not None and birth_month is not None:
    with open(random.choice(letters), "r") as letter:
        contents = letter.read()
        name =
        birthday_message = contents.replace("[NAME}", name)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)

    # Send email with birthday_message as message body.
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs="grey.pafotisevheni@yahoo.com",
        msg=f"Subject: Happy Birthday\n\n {birthday_message}"
    )




