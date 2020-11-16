from KEY.key import API_KEY_AUTHORISATIONS #токен с доступом к методам friends
from KEY.key import PHONES
import requests
import json


FILELDS = "nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities"

r = requests.get("https://api.vk.com/method/friends.getByPhones", params={
    "phones": PHONES,
    "fields": FILELDS,
    "access_token": API_KEY_AUTHORISATIONS,
    "v": 5.122
}).json()

with open("friendsGetByPhones.json", "w") as f:
    f.write(json.dumps(r))