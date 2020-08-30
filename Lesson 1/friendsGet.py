from KEY.key import API_KEY_FRIENDS
import requests
import json

#https://oauth.vk.com/authorize?client_id=6993599&scope=friends&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1#

USER_ID = 222247555
V = 5.122

r = requests.get("https://api.vk.com/method/friends.get", params={
    "user_id": USER_ID,
    "order": "name",
    "count": 5000,
    "offset": 0,
    "fields": "nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities",
    "access_token": API_KEY_FRIENDS,
    "v": V
}).json()["response"]["items"]

with open("friends.json", "w") as f:
    f.write(json.dumps(r))
f.close()

print("Выполненно")