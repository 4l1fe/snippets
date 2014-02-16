import socket

print('='*40)
for host in ['mojo', 'www', 'www.python.org', 'nosuchname']:
    try:
#        print('{0}: {1}'.format(host, socket.gethostbyname(host)))
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
#        hostname, aliases, addresses = socket.gethostbyaddr('192.168.1.2')
        print('HN:', hostname)
        print('AL:', aliases)
        print('AD:', addresses)

    except socket.error as msg:
        print('{0} {1}'.format(host, msg))
    finally:
        print('.'*20)

