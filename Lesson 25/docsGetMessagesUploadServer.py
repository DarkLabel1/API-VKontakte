from KEY.key import API_KEY_DOCS
import requests

TYPE = "doc"
PEER_ID = 226933620

r = requests.get("https://api.vk.com/method/docs.getMessagesUploadServer", params={
    "type": TYPE,
    "peer_id": PEER_ID,
    "access_token": API_KEY_DOCS,
    "v": 5.122
}).json()

print(f"Ваш url для отправки файла: {r['response']['upload_url']}")