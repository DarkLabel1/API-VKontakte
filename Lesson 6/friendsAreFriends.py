from KEY.key import API_KEY_FRIENDS
from LAYER.layer import friend_status
import requests
import json

USER_IDS = "222247555, 611946161, 19902804, 368551886"
USER_INFO = []

r = requests.get("https://api.vk.com/method/friends.areFriends", params={
    "user_ids": USER_IDS,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

for item in r:
    st = friend_status[item["friend_status"]]
    user = requests.get("https://api.vk.com/method/users.get", params={"user_ids":  item["user_id"], "fields": "first_name, last_name", "access_token": API_KEY_FRIENDS, "v": 5.122}).json()["response"][0]
    USER_INFO.append({
        "friends_status": st,
        "user": user
    })

with open("FriendsAreFriends.json", "w") as f:
    f.write(json.dumps(USER_INFO))
f.close()

print("Выполненно")