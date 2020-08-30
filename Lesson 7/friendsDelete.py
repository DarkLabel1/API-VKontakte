from KEY.key import API_KEY_FRIENDS
import requests
import json

USER_ID = 473016308

r = requests.get("https://api.vk.com/method/friends.delete", params={
    "user_id": USER_ID,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

if r["success"] == 1:
    print(f"{str(USER_ID)} удалось успешно удалить друга.")