import bs4
from urllib.request import build_opener, Request, urlopen, HTTPCookieProcessor
from urllib.parse import urljoin, urlencode
from http import cookiejar


class Loginer:

    def __init__(self, cookiefilename, domain):
        self.cj = cookiejar.LWPCookieJar(cookiefilename)
        self.opener = build_opener(HTTPCookieProcessor(self.cj))
        self.domain = domain

    def set_initial_cookies(self):
        resp = self.opener.open(self.domain + '/login')
        print('init ___', str(self.cj._cookies))

    def auth(self, username, password):
        self.set_initial_cookies()
        data = urlencode(dict(username=username, password=password))
        req = Request(urljoin(self.domain, 'login'), data=data.encode())
        req.add_header('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
        print(req.header_items())
        print(vars(self.opener.process_request['http'][1]))
        resp = self.opener.open(req)
        print(req.header_items())
        self.cj.save()
        print('auth ___', str(self.cj._cookies))

    def logout(self):
        self.cj.clear()


def get_bookmarks(sessionid, domain):
    c = cookiejar.Cookie(version=0, name='sessionid', value=sessionid, port=None,
                          port_specified=False, domain=domain, domain_specified=True, domain_initial_dot=False,
                          path='/', path_specified=True, secure=False, expires=None, discard=False, comment=None,
                          comment_url=None, rest=None)
    req = Request(urljoin(domain, 'bookmarks'))
    cj = cookiejar.CookieJar()
    cj.set_cookie(c)
    cj.add_cookie_header(req)
    resp = urlopen(req)
    soup = bs4.BeautifulSoup(resp.read())
    return soup.prettify()

if __name__ == '__main__':
    b = Loginer('cookie.txt', 'http://127.0.0.1:8000')
    b.auth('dim', "1")
