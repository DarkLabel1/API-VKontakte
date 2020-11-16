from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests
import json

USER_ID = "621131182"
RETURN_SYSTEM = 1

r = requests.get("https://api.vk.com/method/friends.getLists", params={
    "user_id": USER_ID,
    "return_system": RETURN_SYSTEM,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

with open("friendsGetLists.json", "w") as f:
    f.write(json.dumps(r))