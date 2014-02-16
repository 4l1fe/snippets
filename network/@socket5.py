import socket
import pdb

#pdb.set_trace()

def get_constans(prefix):
    return dict( (getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix))

families = get_constans('AF_')
types = get_constans('SOCK_')
protocols = get_constans('IPPROTO_')

for response in socket.getaddrinfo('www.vk.com', 'http'):
    family, socktype, proto, cannoname, sockaddr = response

    print('F:', families[family])
    print('ST:', types[socktype])
    print('P:', protocols[proto])
    print('CN:', cannoname)
    print('SA:', sockaddr)
    print('.'*20)