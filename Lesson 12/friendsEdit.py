from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests

USER_ID = "189720123"
LIST_IDS = "1"

r = requests.get("https://api.vk.com/method/friends.edit", params={
    "user_id": USER_ID,
    "list_ids": LIST_IDS,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

try:
    print("Возникла ошибка: " + str(r['error']['error_msg']))
except:
    print("Успешно выполненно.")