import requests
import json
from urllib.parse import urlencode

url = 'http://itranslate4.eu/api/Translate'
parameters = urlencode(dict(auth='8afe1c99-26b3-4cc3-b1e2-47a1336a3696',
                            src='en',
                            trg='ru',
                            dat='world is mine'))
resp = requests.get(url+'?'+parameters, proxies={'http': 'http://dv.krasnov:S73ps61@IAS.corp.tensor.ru:8080'})
resp = json.loads(resp.text)
print(resp)
