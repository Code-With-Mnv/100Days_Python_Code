import datetime as dt

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "Y6OAOGDC4PLJPN7H"
NEWS_API = "4e5207872f99422f8da86690b8d59cd1"
YESTERDAY = dt.date.today() - dt.timedelta(1)
DAY_B4_YESTERDAY = dt.date.today() - dt.timedelta(2)
OPEN_TIME = "04:00:00"
CLOSE_TIME = "19:00:00"


# STEP 1: Fetch and process stocks data

stock_paras = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "TSLA",
    "interval": "60min",
    "apikey": "Y6OAOGDC4PLJPN7H"
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_paras)

stock_data = stock_response.json()

yesterday_value = float(stock_data["Time Series (60min)"][f"{YESTERDAY} {CLOSE_TIME}"]["4. close"])
day_b4_yesterday_value = float(stock_data["Time Series (60min)"][f"{DAY_B4_YESTERDAY} {CLOSE_TIME}"]["4. close"])

value_rise = value_fall = 0

if yesterday_value > day_b4_yesterday_value:
    value_rise = yesterday_value - day_b4_yesterday_value
elif day_b4_yesterday_value > yesterday_value:
    value_fall = day_b4_yesterday_value - yesterday_value
else:
    pass

# STEP 2: Fetch relevant news regarding rise/fall of stocks

news_paras = {
    "q": "tesla",
    "from": dt.date.today()-dt.timedelta(2),
    "apiKey": "4e5207872f99422f8da86690b8d59cd1"
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_paras)

news_data = news_response.json()

news = {}

for i in range(0,3):
    headline = news_data['articles'][i]['title']
    summary = news_data['articles'][i]['description']
    news[headline] = summary


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# NOT COMPLETING THE CODE

# RUN A CONDITION TO CHECK IS THE STOCK PRICES RAISED OR FELL BY >1%
# IF SO SEND THE SMS ALERT ALONG WITH 3 NEWS ARTICLES


# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or 
"TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
