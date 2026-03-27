import requests

MY_LAT = -25.413166
MY_LONG = 28.257792


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()

print(data["results"]["sunset"])