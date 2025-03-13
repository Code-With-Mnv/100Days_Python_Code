import requests

url = "https://api.sheety.co/Sheet1/flightDeals/prices"

response = requests.get(url=url)

print(response.json())