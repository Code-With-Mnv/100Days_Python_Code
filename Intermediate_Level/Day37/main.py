import datetime as dt

import requests

API_KEY = "JHINGALALA"
USERNAME = "wtfmanav"
GRAPH_ID = "graphy1"
ACC_CREATION_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_CREATION_ENDPOINT = f"{ACC_CREATION_ENDPOINT}/{USERNAME}/graphs"
VALUE_POSTING_ENDPOINT = f"{GRAPH_CREATION_ENDPOINT}/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": API_KEY
    # enhanced protection we provide apikey as X-USER-TOKEN which keeps it hidden and prevents unwanted access.
}

user_paras = {
    "token": API_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# acc_response = requests.post(url=ACC_CREATION_ENDPOINT, json=user_paras)
# print(acc_response.text)

# new user has been created, no need to repeat above two lines everytime we run the code

graph_paras = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}


# graph_response = requests.post(url=GRAPH_CREATION_ENDPOINT, json=graph_paras, headers=HEADERS)
# print(graph_response.text)

# new graph has been created, no need to repeat above two lines everytime we run the code

quantity = float(input("How much distance did u cover: "))
date = dt.datetime.now().date()
date_str = str(date)
year = date_str[0:4]
day = date_str[5:7]
month = date_str[8:10]

value_paras = {
    "date": f"{year+day+month}",
    "quantity": f"{quantity}"
}

value_response = requests.post(url=VALUE_POSTING_ENDPOINT, json=value_paras, headers=HEADERS)
print(value_response.text)
