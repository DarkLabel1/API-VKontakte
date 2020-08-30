from KEY.key import API_KEY_FRIENDS
import requests
import json

SOURCE_UID = 222247555
TARGET_UID = 533763262

r = requests.get("https://api.vk.com/method/friends.getMutual", params={
    "source_uid": SOURCE_UID,
    "target_uid": TARGET_UID,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

users_id = ""

for item in r:
    users_id += str(item) + ","


u = requests.get("https://api.vk.com/method/users.get", params={
    "user_ids": users_id,
    "fields": "photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

with open("MutualFriends.json", "w") as f:
    f.write(json.dumps(u))
f.close()

print("Выполненно.")