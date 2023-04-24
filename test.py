import requests, json
from pprint import pprint

date = {
    'month': 1,
    'day': 1
}

endpoint = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{date['month']}/{date['day']}"

r = requests.get(endpoint)
data = r.json()
pprint(data["events"][0])