import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

to_email = input('recipient:')
servername = input('mail servername:')
serverport = input('mail port:')
username = input('mail username:')
password = getpass.getpass()

msg = MIMEText('Messaga wazazzzzz')
#msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(('recipient',to_email))
msg['From'] = email.utils.formataddr(('author', username))
msg['Subject'] = 'Simple test message'

#server = smtplib.SMTP('smtp.yandex.ru', 587)

servername = servername.lstrip().rstrip()
serverport = int(serverport)
connection = smtplib.SMTP(servername, serverport)

try:
    connection.set_debuglevel(True)
    connection.ehlo()
    if connection.has_extn('STARTTLS'):
        connection.starttls()
        connection.ehlo()
#    connection.login(username, password)
    connection.sendmail(msg['From'],[msg['To']], msg.as_string())
finally:
    connection.quit()

