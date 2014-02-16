import socket

for k in socket.__dict__:
    if k.startswith('IPPROTO_'): print(k)

for name in ['tcp', 'udp', 'icmp']: #numbers of named protocols
    print(socket.getprotobyname(name))