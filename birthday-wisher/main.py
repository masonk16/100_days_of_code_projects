import pandas
import datetime as dt
import random
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
# Read csv into dataframe
birthdays = pandas.read_csv("birthdays.csv")

# Obtain date and check against birthdays
now = dt.datetime.now()
day = now.day
month = now.month

birth_day = birthdays[birthdays["day"] == 2]
birth_month = birthdays[birthdays["day"] == 7]

letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

if birth_day is not None and birth_month is not None:
    with open(random.choice(letters), "r") as letter:
        contents = letter.read()
        name =
        message = contents.replace("[NAME}", name)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




