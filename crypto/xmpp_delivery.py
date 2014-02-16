import shelve
import rpc
import sleekxmpp
import time
from socket import gethostbyname
from contextlib import closing
from copy import deepcopy


#=================Глобальные переменные=================#
XMPP_HOST = 'test-autotest4'
XMPP_PORT = 5222
XMPP_SENDER = 'admin@test-autotest4'  #  JID отправителя
XMPP_SENDER_PASSWORD = 'admin'
XMPP_GROUP = XMPP_HOST + '/announce/all'
TIMEOUT = 10 # Время в секундах, по истечении которго будет посылаться запрос на получение данных.

#=================Класс клиента для отправки xmpp-уведомлений=================#
class Notifier(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, group, message):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.message = message
        self.group = group

        self.add_event_handler("session_start", self.start)

    def start(self, event):
         self.get_roster()
         self.send_presence()
         self.send_message(mto=self.group, mbody=self.message)
         self.disconnect(wait=True)

#=================Функция получения ответа с сервера и формирования по нему xmpp-уведомлений=================#
def check_new_questions_and_answers():
    # Ответ с сервера приходит отсортированный по убыванию даты,
    # и будет содержать только нерешенные\открытые вопросы.
    client = rpc.Client('wi.sbis.ru')
    response = client.call('Вопрос.СписокВопросов', ДопПоля=[], Навигация=None, Сортировка=None,
                           Фильтр={'d': [True], 's': [{'t': 'Логическое', 'n': 'ТолькоНеРешенные'}]})
    message = ''
    new_answers = []
    new_questions = []
    with closing(shelve.open('xmpp_delivery', writeback=True)) as DATABASE:

        # Чистим DATABASE, если все вопросы закрыты\решены.
        if len(response['d']) == 0:
            DATABASE['response'] = []
            DATABASE['last_question'] = []

        if len(response['d']) > 0:  # ответ может быть пустой.
            response['d'].reverse()  # для сортировки по возрастанию даты\времени.
            if not DATABASE.get('response'):
                    DATABASE['response'] = deepcopy(response['d'])  # ключ d - список данных по всем вопросам.
                    DATABASE['last_question'] = deepcopy(response['d'][len(response['d'])-1])  # самый свежий вопрос.

            else:
                # Поиск новых вопросов и добавление их в DATABSE.
                for question in response['d']:
                    if question[7] > DATABASE['last_question'][7]: # 7 - индекс поля "ДатаВремя".
                        new_questions.append(question)
                        DATABASE['response'].append(question)
                        DATABASE['last_question'] = question
                if new_questions:
                    message += '==================НОВЫЕ ВОПРОСЫ==================\n\n'
                    for q in new_questions:
                        message += 'ЗАГОЛОВОК: {title}\n'
                        message += 'ТЕКСТ ВОПРОСА: {description}\n'
                        message += 'ДАТА: {dt}\n\n'
                        message = message.format(title=q[1], description=q[2], dt=q[7])

                # Проверяем, закрылись ли какие-либо вопросы в новом ответе response
                # и есть ли удалённые.
                # При новых вопросах, длина DATABASE всегда больше.
                pop_indexes = []
                if len(DATABASE['response']) > len(response['d']):
                    for i, old_question in enumerate(DATABASE['response']):
                        if old_question[0] not in [response['d'][q][0] for q in range(len(response['d']))]:
                            pop_indexes.append(i)
                for i, index in enumerate(pop_indexes):
                    DATABASE['response'].pop(index-i)

                zip_ = zip(DATABASE['response'], response['d'])  # zip ведёт себя неявно
                for i, (old_question, question) in enumerate(zip_):  # enumerate ведёт себя неявно
                    if old_question[4] < question[4]:  # 4 - индекс поля "Количество ответов".
                        new_answers.append(question)
                        DATABASE['response'][i] = deepcopy(response['d'][i])
                    if new_answers:
                        message = '==================НОВЫЕ ОТВЕТЫ==================\n\n'
                        for a in new_answers:
                            message += 'ПОЛУЧЕН ОТВЕТ НА ВОПРОС: {number} {title}\n'.format(number=a[0], title=a[1])

    # Отправка сообщений по XMPP
    if message:
        print(message)
        notifier = Notifier(XMPP_SENDER, XMPP_SENDER_PASSWORD, XMPP_GROUP, message)
        notifier.register_plugin('xep_0030') # Service Discovery
        notifier.register_plugin('xep_0004') # Data Forms
        notifier.register_plugin('xep_0060')
        notifier.register_plugin('xep_0199') # XMPP Ping
        notifier.connect((gethostbyname(XMPP_HOST), XMPP_PORT), use_tls=False)
        notifier.process(block=True)


if __name__ == '__main__':
    while True:
        check_new_questions_and_answers()
        time.sleep(TIMEOUT)
