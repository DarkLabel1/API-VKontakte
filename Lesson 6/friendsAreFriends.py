from KEY.key import API_KEY_FRIENDS #наш токен доступа к api vk
from LAYER.layer import friend_status #словарь в котором перечислены все возможные статусы
import requests
import json

USER_IDS = "222247555,611946161,19902804,368551886"
USER_INFO = [] #Словарь в котором будет хранится вся информация о друзьях

#Делаем get запрос к api vk с такими параметрами:
#user_ids - id пользователей которых хот проверить


r = requests.get("https://api.vk.com/method/friends.areFriends", params={
    "user_ids": USER_IDS,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]


#Сделаем так чтобы статусы друзей были нам понятны, и прведём id к нормальному виду
for item in r: #Ошибка заключается в том что я брал полный ответ от сервера, а требуется только элементы в списке.
    st = friend_status[item["friend_status"]]
    user = requests.get("https://api.vk.com/method/users.get", params={"user_ids": item["user_id"], "fields": "first_name,last_name", "access_token": API_KEY_FRIENDS, "v": 5.122}).json()
    USER_INFO.append({
        "friends_status": st,
        "user": user['response'][0]
    })
#Скорее всего я просто допустил ошибку в написании слова response, вот по этому и не срабатывало


#Запишем всё получившиесе в файл и проверим результат
with open("FriendsAreFriends.json", "w") as f:
    f.write(json.dumps(USER_INFO))
f.close()

print("Выполненно")