from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests


NAME = "Adm"
LIST_ID = "1"
USER_IDS = "473016308,220278425,189720123"

r = requests.get("https://api.vk.com/method/friends.editList", params={
    "name": NAME,
    "list_id": LIST_ID,
    "user_ids": USER_IDS,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

try:
    print("Возникла ошибка: " + str(r['error']['error_msg']))
except:
    print("Успешно выполненно.")