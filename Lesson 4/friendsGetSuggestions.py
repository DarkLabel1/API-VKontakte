from KEY.key import API_KEY_FRIENDS #наш токен, полученный в 1-ом уроке.
import requests
import json


#Делаем get запрос к vk api с параметрами
#filter - ипы предлагаемых друзей, которые нужно вернуть, перечисленные через запятую.
#Может принимать следующие значения:
#mutual — пользователи, с которыми много общих друзей;
#По умолчанию будут возвращены все возможные друзья.
#access_token - токен vk с разрешением доступа к друзьям
#v - версия api (5.122 последняя версия)


r = requests.get("https://api.vk.com/method/friends.getSuggestions", params={
    "filter": "mutual",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()


#Запишем результат в файл *.json
with open("friends.getSuggestions", "w") as f:
    f.write(json.dumps(r["response"]["items"]))
f.close()


#Можем также посмотреть кол-во рекомендованных друзей
print(f"Всего записей: {r['response']['count']}")


print("Выполненно")