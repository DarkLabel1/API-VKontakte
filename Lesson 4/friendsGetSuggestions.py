from KEY.key import API_KEY_FRIENDS
import requests
import json

r = requests.get("https://api.vk.com/method/friends.getSuggestions", params={
    "filter": "mutual",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]["items"]

with open("FriendsSuggestions.json", "w") as f:
    f.write(json.dumps(r))
f.close()

print("Выполненно")
