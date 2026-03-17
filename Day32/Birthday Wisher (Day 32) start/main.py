import datetime as dt
import random
import smtplib

my_email = "ofankiedad@gmail.com"
password = "roovlzcgemazhhmh"
now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt", "r") as f:
    quotes = f.readlines()

if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="kbokaba3@gmail.com", msg=f"Subject:Quote Of The Day\n\n{random.choice(quotes)}")

