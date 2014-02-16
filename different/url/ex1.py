from urllib import request


URL = 'http://www.yandex.ru'
psw_mgr = request.HTTPPasswordMgrWithDefaultRealm()
psw_mgr.add_password(None, URL, 'dv.krasnov', 'S73ps61')
auth = request.ProxyBasicAuthHandler(psw_mgr)
opener = request.build_opener(auth)
request.install_opener(opener)
resp = request.urlopen(URL)
print(resp)

#8afe1c99-26b3-4cc3-b1e2-47a1336a3696