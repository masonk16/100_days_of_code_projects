import datetime as dt
import random
import smtplib

# Email credentials
EMAIL = "mabasics175@gmail.com"
PASSWORD = "wllaqeaotxnaitmu"

# Determine day of the week
now = dt.datetime.now()
day = now.weekday()
if day == 0:
    # Get a quote from the quotes file.
    with open("quotes.txt", "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        todays_quote = random.choice(quotes_list)

    # Setup SMTP connection
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)

        # Send email with todays_quote as message body.
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="grey.pafotisevheni@yahoo.com",
            msg=f"Subject: Monday Motivation\n\n {todays_quote}"
        )
