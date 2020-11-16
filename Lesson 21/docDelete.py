from KEY.key import API_KEY_DOCS
import requests
import json


OWNER_ID = 533763262
DOC_ID = 568099152


r = requests.get("https://api.vk.com/method/docs.delete", params={
    "owner_id": OWNER_ID,
    "doc_id": DOC_ID,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()

if r["response"] == 1:
    print(f"Файл {OWNER_ID} удален из ваших документов.")