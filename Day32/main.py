##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd

my_email = "ofankiedad@gmail.com"
my_password = "roovlzcgemazhhmh"
recep_email = ""

# 2. Check if today matches a birthday in the birthdays.csv
df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

def check_birthday():
    month = now.month
    day = now.day

    for i in range(0, len(df)):
        if ((df.iloc[i]["month"]) == month) and ((df.iloc[i]["day"]) == day):
            print("Sent")
            return i
        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def random_letter():
    global recep_email
    letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    
    with open(f"letter_templates/{random.choice(letters)}", "r") as f:
        letter_to_send = f.read()

    index = check_birthday()
    letter_to_send = letter_to_send.replace("[NAME]", df.iloc[index]["name"])
    recep_email = df.iloc[index]["email"]
    return letter_to_send

# 4. Send the letter generated in step 3 to that person's email address.
def send_letter():
    letter = random_letter()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recep_email, msg=f"Subject:It's Your Birthday\n\n{letter}")
    

try:
    send_letter()
except:
    print("It is no ones Birthday today")