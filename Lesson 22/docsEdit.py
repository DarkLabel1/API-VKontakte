from KEY.key import API_KEY_DOCS
import requests


OWNER_ID = 533763262
DOC_ID = 568100331
DOC_TITLE = "Какой-то договор в Ижевске"
DOC_TAGS = "Договор,ижевск"

r = requests.get("https://api.vk.com/method/docs.edit", params={
    "owner_id": OWNER_ID,
    "doc_id": DOC_ID,
    "title": DOC_TITLE,
    "tags": DOC_TAGS,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()

if r["response"] == 1:
    print(f"Договор изменен. Название договора: {DOC_TITLE}.")