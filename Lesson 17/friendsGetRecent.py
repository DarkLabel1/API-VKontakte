from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests
import json

COUNT = 100

r = requests.get("https://api.vk.com/method/friends.getRecent", params={
    "count": COUNT,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

with open("friendsGetRecent.json", "w") as f:
    f.write(json.dumps(r))