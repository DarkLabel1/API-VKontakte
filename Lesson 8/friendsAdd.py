from KEY.key import API_KEY_FRIENDS
from LAYER.layer import add_user
import requests

USER_ID = 473016308

r = requests.get("https://api.vk.com/method/friends.delete", params={
    "user_id": USER_ID,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

status = add_user[r["success"]]
print(status)