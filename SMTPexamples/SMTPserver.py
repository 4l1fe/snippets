import smtpd
import asyncore

class CustomSMTPserv(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print('receiving from:', peer)
        print('addressed from', mailfrom)
        print('addressed to', rcpttos)
        print('msg len:', len(data))
        return

server = smtpd.PureProxy(('localhost', 1025), None)
asyncore.loop()


