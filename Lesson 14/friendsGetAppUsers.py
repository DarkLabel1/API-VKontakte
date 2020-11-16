from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests

r = requests.get("https://api.vk.com/method/friends.getAppUsers", params={
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

try:
    print("Возникла ошибка: " + str(r['error']['error_msg']))
except:
    i = ""
    if len(r["response"]) != 0:
        for item in r["response"]:
            i += item + ","
        print("Успешно выполненно. \nID пользователей: " + i.replace(i[::1], ""))
    else:
        print("Приложением ещё никто не пользовался.")