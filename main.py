import requests
from datetime import datetime

PIXELA_END = "https://pixe.la/v1/users"
TOKEN = "Your token"
USERNAME = "your Username"

my_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=PIXELA_END, json=my_params)
# print(response.text)

GRAPH_END = f"{PIXELA_END}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cardio",
    "unit": "Min",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_END, json=graph_params,headers=header)
# print(response.text)

today = datetime.now()
POST_END = f"{PIXELA_END}/{USERNAME}/graphs/graph1"
post_param = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many minutes you have done cardio today" ),
}

response = requests.post(url=POST_END, json=post_param, headers=header)
print(response.text)

