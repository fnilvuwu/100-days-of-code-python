import smtplib
import datetime as dt
import random

my_email = EMAIL
password = PASSWORD

with open("quotes.txt") as file:
    quotes_list = file.readlines()

if dt.datetime.now().weekday() == 5:
    message_to_send = random.choice(quotes_list)
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Monday Motivation\n\n{message_to_send}"
    )
    connection.close()


print(message_to_send)
