from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse, urljoin, urlunparse, ParseResult
from bs4 import BeautifulSoup as BS
#import html5lib


get_icon_address = 'http://www.google.com/s2/favicons?domain='

resp = urlopen('http://78.47.37.5/show_publick_bookmarks/ADMIN/')
primary_html = BS(resp.read())
#print(primary_html.head.find('link', rel='icon'))
div = primary_html.body.find('div', class_='row')
hrefs = [a['href'] for a in div.find_all('a')]
#print(hrefs)

for i, href in enumerate(hrefs):
    urlretrieve(get_icon_address+href, 'icon_{}.png'.format(i))


#for i, href in enumerate(hrefs):
#    try:
#        resp = urlopen(href)
#        icon_html = BS(resp.read())
#        print(href)
#        print(icon_html.head.find('link', rel='icon'))
#        icon_tag = icon_html.head.find('link', rel='icon')
#        if icon_tag:
#            icon_href = icon_tag['href']
#            urlparse_result = urlparse(href)
#            print(urlparse_result.scheme)
#            print(urlparse_result.netloc)
#            print(icon_href)
#            icon_url = urlunparse(ParseResult(urlparse_result.scheme, urlparse_result.netloc, icon_href, '', '', ''))
#            print(icon_url)
#            urlretrieve(icon_url, 'some_ico_'+str(i)+'.ico')
#    except HTTPError:
#        pass
#    except ValueError:
#        pass