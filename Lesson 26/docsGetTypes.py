from KEY.key import API_KEY_DOCS
import requests
import json


OWNER_ID = 533763262

r = requests.get("https://api.vk.com/method/docs.getTypes", params={
    "owner_id": OWNER_ID,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()


with open("docsGetTypes.json", "w") as f:
    f.write(json.dumps(r["response"]["items"]))
f.close()

print(f"Выполненно. Всего вариантов: {r['response']['count']}")