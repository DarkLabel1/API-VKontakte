from KEY.key import API_KEY_FRIENDS #API токен который получили в 1-ом уроке
import requests
import json


USER_ID = 533763262#ID пользователя у которого хоти посмотреть друзей онлайн
ONLINE = []#Словарь куда мы поместим тех кто сидит с телефона, и тех кто сидит с компьютера

#Делаем get запрос к api vk с такими параметрами:
#user_id - id пользователя
#online_mobile - сортировать ли пользователей которые сидят с телефона либо нет (0 либо 1) тип данных bool
#access_token - токен vk
#v - версия vk (5.122 последняя)


###
###Первый раз не прошло так как у меня сменился ip адресс.
###
r = requests.get("https://api.vk.com/method/friends.getOnline", params={
    "user_id": USER_ID,
    "online_mobile": bool(1),
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]


i_online = ""
for item1 in r["online"]:
    i_online += str(item1) + ","

i_mobile = ""
for item2 in r['online_mobile']:
    i_mobile += str(item2) + ","


#Теперь сделаем так чтобы у нас были не id друзей а информация о них
#Для тех кто сидит с компьютера
u_desktop = requests.get("https://api.vk.com/method/users.get", params={
    "user_ids": i_online,
    "fields": "photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]


#Для тех кто сидит с телефона
u_mobile = requests.get("https://api.vk.com/method/users.get", params={
    "user_ids": i_mobile,
    "fields": "photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]


ONLINE.append({
    "ONLINE_DESKTOP": u_desktop,
    "ONLINE_MOBILE": u_mobile
})


#запишем полученный результат в файл *.json
with open("FriendsOnline.json", "w") as f:
    f.write(json.dumps(ONLINE))
f.close()


print("Выполненно")


#Не спешите что-то писать. Будет меньше ошибок!!