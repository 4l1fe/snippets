#coding: utf-8
import ftplib

client = ftplib.FTP('78.47.37.5', 'ftp_user', '-p')
#sended_file = open('sended_file', 'rb')
#transmission = client.storbinary('STOR sended_file', sended_file)
client.cwd('portfolio/portfolio/')
print(client.dir())
db = open('db', 'wb+')
client.retrbinary('RETR portfolio_db.sqlite3', db.write)
db.close()
client.close()


#ABOR — Прервать передачу файла
#CDUP — Сменить директорию на вышестоящую.
#CWD — Сменить директорию.
#DELE — Удалить файл (DELE filename).
#EPSV — Войти в расширенный пассивный режим. Применяется вместо PASV.
#HELP — Выводит список команд принимаемых сервером.
#LIST — Возвращает список файлов директории. Список передаётся через соединение данных.
#MDTM — Возвращает время модификации файла.
#MKD — Создать директорию.
#NLST — Возвращает список файлов директории в более кратком формате, чем LIST. Список передаётся через соединение данных.
#NOOP — Пустая операция
#PASV — Войти в пассивный режим. Сервер вернёт адрес и порт, к которому нужно подключиться, чтобы забрать данные. Передача начнётся при введении следующих команд: RETR, LIST и т.д.
#PORT — Войти в активный режим. Например PORT 12,34,45,56,78,89. В отличие от пассивного режима для передачи данных сервер сам подключается к клиенту.
#PWD — Возвращает текущую директорию.
#QUIT — Отключиться
#REIN — Реинициализировать подключение
#RETR — Скачать файл. Перед RETR должна быть команда PASV или PORT.
#RMD — Удалить директорию
#RNFR и RNTO — Переименовать файл. RNFR — что переименовывать, RNTO — во что.
#SIZE — Возвращает размер файла
#STOR — Закачать файл. Перед STOR должна быть команда PASV или PORT.
#SYST — Возвращает тип системы (UNIX, WIN, …)
#TYPE — Установить тип передачи файла (бинарный, текстовый)
#USER — Имя пользователя для входа на сервер


#import socket
#
#socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_obj.connect(('78.47.37.5', 21))
#response = socket_obj.recv(1024)
#print(response)
#socket_obj.close()