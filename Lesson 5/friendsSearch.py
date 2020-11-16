from KEY.key import API_KEY_FRIENDS #токен доступа к api
import requests
import json

USER_ID = 222247555 #id пользователя у кого будем искать друга
q = "Саня" #строка поиска

#Делаем get запрос к api vk с параметрами:
#user_id - id пользователь у которого ищем
#q - значение по которому ищем пользователя
#count - если значения не отсылается в параметрах то автоматически ставиться 20, а максимальное знеачение поиска 1000 человек
#access_token - токен доступа с правами на friends (полученный в 1-ом уроке)
#v - версия api vk

r = requests.get("https://api.vk.com/method/friends.search", params={
    "user_id": USER_ID,
    "q": q,
    "count": 1000,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]["items"]

#Теперь запишем всё в файл *.json
with open("FriendsSearch.json", "w") as f:
    f.write(json.dumps(r))
f.close()

print("Выполненно")