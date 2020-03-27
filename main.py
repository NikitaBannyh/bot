import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random

TOKEN = "d1d2310c1b6efd9276a673ffd6ff0164f1e756d892083911f93410b99a36bcfb1da89480ead0e4ad5c50d"


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 193460958)
    message_count = 0
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message_count += 1
            vk = vk_session.get_api()
            if message_count == 1:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Добро пожаловать в ЯндексБота \n Как дела?",
                                 random_id=random.randint(0, 2 ** 64))
            elif message_count == 2:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="У меня тоже " + str(event.obj.message['text']) + "\n Что делаешь?",
                                 random_id=random.randint(0, 2 ** 64))
            elif message_count == 3:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Я тоже часто " + str(event.obj.message['text']),
                                 random_id=random.randint(0, 2 ** 64))
            else:
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message="Я устал,давай отдохнём,это уже " + str(message_count) + " по счёту сообщение",
                                 random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
