import socket

try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse


ports = []
for url in ['http://www.python.org',
    'https://www.mybank.com',
    'ftp://prep.ai.mit.edu',
    'gopher://gopher.micro.umn.edu',
    'smtp://mail.example.com',
    'imap://mail.example.com',
    'imaps://mail.example.com',
    'pop3://pop.example.com',
    'pop3s://pop.example.com',]:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)#The port numbers for network services with standardized names
                                                  #socket.getservbyport() is the reverse function
    print(parsed_url.scheme, ':', port)
    ports.append(port)

print('='*40)
for port in ports:
    print(socket.getservbyport(port))

