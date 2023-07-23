import requests
from datetime import datetime

#https://pixe.la/v1/users/fnilvu/graphs/graph1.html
TOKEN = TOKEN
USERNAME = USERNAME
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Workout Graph",
    "unit": "calory",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220402"

today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_config = {
    # "date": today.strftime("%Y%m%d"),
    "quantity": "100",
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
response = requests.delete(url=pixel_endpoint, headers=headers)

print(response.text)