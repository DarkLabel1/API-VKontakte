from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests

r = requests.get("https://api.vk.com/method/friends.deleteAllRequests", params={
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

try:
    print("Возникла ошибка: " + str(r['error']['error_msg']))
except:
    print("Успешно выполненно.")