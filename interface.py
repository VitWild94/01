import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import access_token, community_token


class BotInterface:

    def __init__(self, token):
        self.bot = vk_api.VkApi(token=community_token)

    def message_send(self, user_id, message):
        self.bot.method('messages.send',
                        {'user_id': user_id,
                         'message': message,
                         'random_id': get_random_id()
                         }
                        )

    def hendler(self):
        longpull = VkLongPoll(vk)
        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                if event.text.lower() == 'привет':
                    self.message_send(event.user_id, 'Добрый день')

                elif event.text.lower() == 'поиск':
                    pass
                elif event.text.lower() == 'далее':
                    pass
                else:
                    self.message_send(event.user_id, 'Неизвестная команда')
    
    def listen(self):
        longpoll = VkLongPoll(self.bot)
        for event in longpoll.listen():
            self.handle_event(event)

        return
        print(event.text)

        if event.to_me:
            request = event.text

            if request == "привет":
                write_msg(event.user_id, f"Хай, {event.user_id}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")