import pandas
from datetime import datetime
import random
import smtplib


# Obtain todays date
today = (datetime.now().month, datetime.now().day)

# Read csv into dataframe and create a dictionary
birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_data.iterrows()}

# Check if a birthday matches todays date
if today in birthdays_dict:
    file = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file, "r") as letter:
        contents = letter.read()
        birthday_message = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)

        # Send email with birthday_message as message body.
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="grey.pafotisevheni@yahoo.com",
            msg=f"Subject: Happy Birthday\n\n {birthday_message}"
        )




