from KEY.key import API_KEY_FRIENDS #токен с доступом к методам friends
import requests
import json

COUNT = 100
EXTENDED = 1
NEED_MUTUAL = 1
OUT = 1
FIELDS = "nickname, screen_name, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, counters, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities"


r = requests.get("https://api.vk.com/method/friends.getRequests", params={
    "count": COUNT,
    "extended": EXTENDED,
    "need_mutual": NEED_MUTUAL,
    "out": OUT,
    "fields": FIELDS,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()
with open("friendsGetRequests.json", "w") as f:
    f.write(json.dumps(r))