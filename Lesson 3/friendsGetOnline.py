from KEY.key import API_KEY_FRIENDS
import requests
import json

USER_ID = "222247555"
ONLINE = []

r = requests.get("https://api.vk.com/method/friends.getOnline", params={
    "user_id": USER_ID,
    "online_mobile": bool(1),
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]


u_desktop = requests.get("https://api.vk.com/method/users.get", params={
    "user_ids": r["online"],
    "fields": "photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

u_mobile = requests.get("https://api.vk.com/method/users.get", params={
    "user_ids": r["online_mobile"],
    "fields": "photo_id, verified, sex, bdate, city, country, home_town, has_photo, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, domain, has_mobile, contacts, site, education, universities, schools, status, last_seen, followers_count, common_count, occupation, nickname, relatives, relation, personal, connections, exports, activities, interests, music, movies, tv, books, games, about, quotes, can_post, can_see_all_posts, can_see_audio, can_write_private_message, can_send_friend_request, is_favorite, is_hidden_from_feed, timezone, screen_name, maiden_name, crop_photo, is_friend, friend_status, career, military, blacklisted, blacklisted_by_me, can_be_invited_group",
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

ONLINE.append({
    "ONLINE_DESKTOP": u_desktop,
    "ONLINE_MOBILE": u_mobile
})

with open("FriendsOnline.json", "w") as f:
    f.write(json.dumps(ONLINE))
f.close()

print("Выполненно")