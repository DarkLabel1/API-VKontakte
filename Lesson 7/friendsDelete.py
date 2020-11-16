from KEY.key import API_KEY_FRIENDS #токен доступа к api vk, с разрешением friends, получали в 1-ом уроке
import requests

USER_ID = "473016308"


#Делаем get запрос с параметрами:
#user_id - id друга которого надо удалить из друзей, либо отклонить заявку в друзья
#access_token - токен доступа к vk api
#v - версия vk api (5.122 последняя версия)

r = requests.get("https://api.vk.com/method/friends.delete", params={
    "user_id": USER_ID,
    "access_token": API_KEY_FRIENDS,
    "v": 5.122
}).json()["response"]

if r["success"] == 1:
    print(f"{str(USER_ID)} удалось успешно удалить друга")
elif r["success"] == 2:
    print(f"{str(USER_ID)} заявка в друзья данного пользователя удалена")
elif r["success"] == 3:
    print(f"{str(USER_ID)} рекомендация добавить в друзья данного пользователя удалена")