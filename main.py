import vk_api
import random
import time
token = "14ab5dd2960b0b74ba47a091c71f50e25f8d303061b0194928872be52d66e28a8012c371a9f7a373e3194"


vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    #главный цикл
    messages = vk.method ("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "привет":
            vk.method("messages.send", {"peer_id": id, "message": "хай !", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "хай":
             vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "как дела":
            vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "что делаешь":
            vk.method("messages.send", {"peer_id": id, "message":  "норм, а у тебя как ?", "random_id": random.randint(1, 2147483647)})

        elif body.lower() == "норм":
            vk.method("messages.send", {"peer_id": id, "message":  "сколько тебе лет ?", "random_id": random.randint(1, 2147483647)})

        else:
            vk.method("messages.send", {"peer_id": id, "message":  "Я тебя непонял", "random_id": random.randint(1, 2147483647)})

    time.sleep(1)