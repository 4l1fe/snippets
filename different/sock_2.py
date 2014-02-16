import sys, os
from sock_1 import server, client
from threading import Thread


mode = int(sys.argv[1])
if mode == 1:
    server()
elif mode == 2:
    client('client:process={}'.format(os.getpid()))
else:
    for i in range(5):
        Thread(target=client, args=('client:thread={};process={}'.format(i, os.getpid()),)).start()


#class Some():
#    def __init__(self):
#        self.a = 'a1'
#        self.b = 'b1'
#
#class Some2():
#    def __init__(self):
#        self.b = d['key1']
#        self.a = ''
#
#d = {'key1': 'value', 'key2': Some2()}
#
#if d.get('key2').a:
#    print('self.a gotten')
#else:
#    print(d.get('key2').b)

#взять второй ключ
#проверить у экземпляра наличие значения у атрибута self.а
#если нету, то self.b