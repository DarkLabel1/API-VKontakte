from KEY.key import API_KEY_FRIENDS
import requests
import json

USER_ID = 222247555
q = "Саня"

r = requests.get("https://api.vk.com/method/friends.search", params={
    "user_id": USER_ID,
    "q": q,
    "count": 1000,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]["items"]

with open("FriendsSearch.json", "w") as f:
    f.write(json.dumps(r))
f.close()

print("Выполненно")