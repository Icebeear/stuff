import requests
import datetime as dt

now = dt.datetime.now()

USERNAME = "lox"
TOKEN = "adun2281337"
user_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=user_endpoint, json=user_params)

graph = f"{user_endpoint}/{USERNAME}/graphs"
graph_params = {
    "X-USER-TOKEN": TOKEN,
    "id": "working1",
    "name": "leetcode",
    "unit": "hours",
    "type": "int",
    "color": "sora",
}

head = {
    "X-USER-TOKEN": TOKEN
}

graph_response = requests.post(url=graph, json=graph_params, headers=head)
print(graph_response.text)

post = f"{user_endpoint}/lox/graphs/working1"

post_config = {
    "date": f"{now.strftime('%Y%m%d')}",
    "quantity": "2"
}

post_response = requests.post(url=post, json=post_config, headers=head)
print(post_response.text)

delete = f"{user_endpoint}/lox/graphs/working1/{now.strftime('%Y%m%d')}"
delete_response = requests.delete(url=delete, headers=head)
print(delete_response.text)