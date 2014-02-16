import requests
import json
from urllib.parse import urlencode

class Translation:

    def __init__(self, trans_url='http://itranslate4.eu/api/Translate',
                  auth_key=''):
        self.auth_key = auth_key
        self.trans_url = trans_url

    def translate(self, src='en', trg='ru', dat='', proxies={}):
        parameters = urlencode(dict(auth=self.auth_key,
                        src=src,
                        trg=trg,
                        dat=dat))
        resp = requests.get(self.trans_url+'?'+parameters, proxies=proxies)
        return json.loads(resp.text)

print(Translation(auth_key='8afe1c99-26b3-4cc3-b1e2-47a1336a3696').translate(dat='game', proxies={'http': 'http://dv.krasnov:S73ps61@IAS.corp.tensor.ru:8080'}))