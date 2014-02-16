import requests
import json
from urllib.parse import urlencode

class Translation:

    def __init__(self, trans_url='http://itranslate4.eu/api/Translate',
                  auth_key=''):
        self.auth_key = auth_key
        self.trans_url = trans_url

    def translate(self, src='en', trg='ru', dat=''):
        parameters = urlencode(dict(auth=self.auth_key,
                        src=src,
                        trg=trg,
                        dat=dat))
        resp = requests.get(self.trans_url+'?'+parameters)
        return json.loads(resp)
