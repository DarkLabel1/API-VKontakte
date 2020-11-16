from KEY.key import API_KEY_DOCS
import requests
import json


Q = "Договор"
SEARCH_OWN = bool(0)
COUNT = 1000,
RETURN_TAGS = bool(1)

r = requests.get("https://api.vk.com/method/docs.search", params={
    "q": Q,
    "search_own": SEARCH_OWN,
    "count": COUNT,
    "return_tags": RETURN_TAGS,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()

with open("docsSearch.json", "w") as f:
    f.write(json.dumps(r["response"]["items"]))
f.close()

print(f"Выполненно. Кол-ыо найденных файлов: {r['response']['count']}")