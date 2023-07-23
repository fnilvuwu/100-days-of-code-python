##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv
file = pandas.read_csv("birthdays.csv")
birthdays_list = file.to_dict("records")

# 2. Check if today matches a birthday in the birthdays.csv
for item in birthdays_list:
    if item["year"] == dt.datetime.now().year and item["month"] == dt.datetime.now().month and item["day"] == dt.datetime.now().day:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_list = []
        letter_list.append(open("letter_templates/letter_1.txt").read())
        letter_list.append(open("letter_templates/letter_2.txt").read())
        letter_list.append(open("letter_templates/letter_3.txt").read())

        random_letter = random.choice(letter_list)
        new_letter = random_letter.replace("[NAME]", item["name"])
        print(new_letter)

# 4. Send the letter generated in step 3 to that person's email address.
        my_email = ""
        password = ""

        to_send_email = item["email"]

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, to_send_email,
                            msg=f"Happy Birthday!\n\n{new_letter}")
        connection.close()
