import requests
from datetime import datetime
import smtplib

MY_LAT = -25.413166 # Your latitude
MY_LONG = 28.257792 # Your longitude
my_password = "roovlzcgemazhhmh"
my_email = "ofankiedad@gmail.com"
recep_email = "kbokaba3@gmail.com"
letter = ""
iss_location = {
    "iss_lat": 0,
    "iss_long": 0,
}
my_sunset = 0
my_sunrise = 0
iss_time = ""

my_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def check_time():
    global my_sunset, my_sunrise
    dt = datetime.now()
    time_now = dt.hour

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_parameters)
    response.raise_for_status()
    my_data = response.json()

    my_sunset = int(my_data["results"]["sunset"].split("T")[1].split(":")[0])
    my_sunrise = int(my_data["results"]["sunrise"].split("T")[1].split(":")[0])
    
    if time_now >= my_sunset or time_now <= my_sunrise:
        return True
    else:
        return False

def check_iss():
    global iss_location
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    iss_location["iss_lat"] = data["iss_position"]["latitude"]
    iss_location["iss_long"] = data["iss_position"]["longitude"]

def generate_letter():
    global letter

    letter = "The ISS is passing near you please go outside bro or you will miss it"

def send_letter():
    generate_letter()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recep_email, msg=f"Subject:It's Your Birthday\n\n{letter}")

def main():
    check_iss()
    if iss_location["iss_lat"] != my_parameters["lat"]:
        if check_time() == False:
            send_letter()

main()