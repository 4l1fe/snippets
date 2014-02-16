import requests
import json
from urllib import parse


class Token:

    def __init__(self, client_id='id_client_translater', client_secret='LYmgeSn2R6G0k4wS+hV7Lz6yR4GlVb5L+WMEtpDi79k=',
                 scope='http://api.microsofttranslator.com', grant_type='client_credentials'):
        self.data = (dict(client_id = client_id,
            client_secret = client_secret,
            scope = scope,
            grant_type = grant_type,
        ))
        self.headers = {'Content-type': 'application/x-www-form-urlencoded'}

    def get_token(self, oauth_url='https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'):
        encoded_data = parse.urlencode(self.data)
        response = requests.post(oauth_url, headers=self.headers, data=encoded_data)
        return response

    def get_access_token(self):
        goten_token = self.get_token()
        json_response = json.loads(goten_token.text)
        return json_response.get('access_token')

class Translation:

    def __init__(self, trns_url='http://api.microsofttranslator.com/V2/Ajax.svc/Translate'):
        self.trns_url = trns_url

    def translate(self, access_token=None, text='', from_lng='', to_lng='', proxies={}):
        try:
            encoded_data = parse.urlencode({'appId': 'Bearer ' + access_token,
                                            'text': text,
                                            'from': from_lng,
                                            'to': to_lng,
                                            'contentType': 'text/plain'})
            response = requests.get(self.trns_url+'?'+encoded_data, proxies=proxies)
            return response
        except Exception as e:
            return e.args
