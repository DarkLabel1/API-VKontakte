from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
from LAYER.layer import add_user #словарь с исходами на добавление в друзья пользователя
import requests


USER_ID = 473016308

#Делаем get запрос к vk api с параметрами:
#user_id - поьзователь которого мы собираемся добавить в друзья
#access_token - токен доступа к vk, с разрешением с доступом к friends
#v - версия api vk (5.122 последняя)

r = requests.get("https://api.vk.com/method/friends.add", params={
    "user_id": USER_ID,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()

#Запрос выполнился правильно, но возникла какая-то ошибка, сейчас наёдём
#Данные приходят не в success, а напрямую в response
status = add_user[r["response"]] #сопоставляем наш список с возвращённым от vk значением
print(status)