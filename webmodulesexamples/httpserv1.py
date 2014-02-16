from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from os.path import split
import sys


HOST = 'localhost'
PORT = 8080
ARROW_IMG = 'D:\download\\arrow.png'

# main_page = '''
# <html>
# <head>
# </head>
# <body>
# <img src='arrow.png'><a href="http://{host}:{port}/sys_info">SYS INFO</a>
# <br>
# <img src='arrow.png'><a href="http://{host}:{port}/date_time">DATE TIME</a>
# </body>
# </html>
# '''
# main_page = main_page.format(host=HOST, port=PORT)

sys_info_page = '''
SYS INFO: {}'''.format(sys.platform)

date_time_page = '''
DATE: {date}
TIME: {time}'''
date_time_page = date_time_page.format(date=datetime.today().strftime('%d.%m.%Y'),
                                       time=datetime.now().strftime('%H:%M'))

class CustomHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        end = '\n[=====================================]\n'
        print('COMMON INFO')
        print('clien_address ', self.client_address, end=end)
        print('server ', self.server, end=end)
        print('command ', self.command, end=end)
        print('path ', self.path, end=end)
        print('request_version ', self.request_version, end=end)
        print('headers ', self.headers, end=end)

        self.send_response(200)

        if self.path.endswith('.png'):
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            png_name = split(self.path)[1]
            image = open(png_name, 'rb')
            self.wfile.write(image.read())
            return
        elif self.path.endswith('.css'):
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            css_name = split(self.path)[1]
            css_file = open(css_name, 'rb')
            self.wfile.write(css_file.read())
            return
        elif self.path.endswith('.js'):
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            js_name = split(self.path)[1]
            js_file = open(js_name, 'rb')
            self.wfile.write(js_file.read())
            return

        # ссылки
        if self.path.endswith('sys_info'):
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(sys_info_page.encode())
        elif self.path.endswith('date_time'):
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(date_time_page.encode())
        else:
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('main_page.html', 'r') as main_page:
                content = main_page.read()
                content = content.format(host=HOST, port=PORT)
            self.wfile.write(content.encode())
        return

if __name__ == '__main__':
    httpd = HTTPServer((HOST, PORT), CustomHandler)
    httpd.serve_forever()