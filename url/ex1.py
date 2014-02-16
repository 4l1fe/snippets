<<<<<<< HEAD
from urllib import request


URL = 'http://www.yandex.ru'
psw_mgr = request.HTTPPasswordMgrWithDefaultRealm()
psw_mgr.add_password(None, URL, 'dv.krasnov', 'S73ps61')
auth = request.ProxyBasicAuthHandler(psw_mgr)
opener = request.build_opener(auth)
request.install_opener(opener)
resp = request.urlopen(URL)
print(resp)

=======
# from urllib import request
import urllib2

# import pdb
# pdb.set_trace()
URL = 'http://www.yandex.ru'
psw_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
psw_mgr.add_password(None, URL, 'dv.krasnov', 'S73ps61')
auth = urllib2.ProxyBasicAuthHandler(psw_mgr)
opener = urllib2.build_opener(auth)
urllib2.install_opener(opener)
resp = urllib2.urlopen(URL)
print(resp)
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
