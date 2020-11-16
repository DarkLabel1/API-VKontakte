from KEY.key import API_KEY_DOCS
import requests
import json


DOCS_ID = "345105594_566011856,189420323_565442007"

r = requests.get("https://api.vk.com/method/docs.getById", params={
    "docs": DOCS_ID,
    "return_tags": bool(1),
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()

with open("docsGetById.json", "w") as f:
    f.write(json.dumps(r["response"]))
f.close()

print("Выполненно.")