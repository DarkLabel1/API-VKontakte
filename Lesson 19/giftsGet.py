from KEY.key import API_KEY_FRIENDS
import requests
import json

USER_ID = 222247555
COUNT = 1000


r = requests.get("https://api.vk.com/method/gifts.get", params={
    "user_id": USER_ID,
    "count": COUNT,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

with open("giftsGet.json", "w") as f:
    f.write(json.dumps(r["response"]["items"]))

print("Выполненно")