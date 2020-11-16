from KEY.key import API_KEY_DOCS
import requests


OWNER_ID = 73668239
DOC_ID = 566459225


r = requests.get("https://api.vk.com/method/docs.add", params={
    "owner_id": OWNER_ID,
    "doc_id": DOC_ID,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()


print(f"Документ добавлен в наши документы. ID документа: {r['response']} ")