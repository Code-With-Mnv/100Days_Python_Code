import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.json())

print(response.json()["iss_position"]["longitude"])

print(response.json()["iss_position"]["latitude"])
