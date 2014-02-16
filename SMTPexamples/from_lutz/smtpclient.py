# -*- coding: utf-8 -*-
import smtplib, sys, email.utils
from . import mailconfig

mailserver = mailconfig.smtpservername

From = input('From? ').strip()      # или импортировать из mailconfig
To   = input('To? ').strip()        # например: python­list@python.org
Tos  = To.split(';')                # допускается список получателей
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()

text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To,
                                                         Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    text += line

print('Connecting...')

server = smtplib.SMTP(mailserver)   # соединиться без регистрации
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:                          # smtplib может возбуждать исключения
    print('Failed recipients:', failed)   # но здесь они не обрабатываются
else:
    print('No errors.')
print('Bye.')


