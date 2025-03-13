import requests
from twilio.rest import Client

URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7be7ee376473848e862039a48cde2d41"
CITY = "Mumbai"
ACC_SID = "ACfe7eb812dbc837456551731e5dd2b072"
AUTH_TOKEN = "1629ec9724d71f4b0b18a6608cc28c3d"
CLIENT = Client(ACC_SID, AUTH_TOKEN)

parameters = {"q": CITY, "appid": API_KEY, "cnt": 4}

weather_response = requests.get(url=URL, params=parameters)
weather_response.raise_for_status()

data = weather_response.json()
weather_data_list = data["list"]

will_rain = False

for days in weather_data_list:
    days_weather_id = days["weather"][0]["id"]
    if days_weather_id < 700:
        will_rain = True

if will_rain:
    message = CLIENT.messages.create(
        body="According to today's wheather report, it's going to rain today. Carry an umbrela with you to avoid "
        "inconvenience.",
        from_="+12565769008",
        to="+919920583987",
    )

    message_wtsp = CLIENT.messages.create(
        from_="whatsapp:+14155238886",
        body="According to today's wheather report, it's going to rain today. Carry an umbrela with you to avoid "
        "inconvenience.",
        to="whatsapp:+919920583987",
    )

    print(message_wtsp.sid)
    print(message.status)
