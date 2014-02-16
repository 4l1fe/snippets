from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
<<<<<<< HEAD
from os.path import split
=======
from os.path import join, basename, normpath, relpath
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
import sys


HOST = 'localhost'
PORT = 8080
<<<<<<< HEAD
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

=======
BOOTSTRAP_DIR = 'bootstrap'
BOOTSTRAP_CSS_DIR = join(BOOTSTRAP_DIR, 'css')
BOOTSTRAP_JS_DIR = join(BOOTSTRAP_DIR, 'js')
BOOTSTRAP_FONTS_DIR = join(BOOTSTRAP_DIR, 'fonts')
ARROW_IMG = 'D:\download\\arrow.png'

>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
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
<<<<<<< HEAD
            png_name = split(self.path)[1]
            image = open(png_name, 'rb')
            self.wfile.write(image.read())
=======
            png_name = basename(self.path)
            image_file = open(png_name, 'rb')
            self.wfile.write(image_file.read())
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
            return
        elif self.path.endswith('.css'):
            self.send_header('Content-type', 'text/css')
            self.end_headers()
<<<<<<< HEAD
            css_name = split(self.path)[1]
=======
            css_name = basename(self.path)
            css_name = normpath(join(BOOTSTRAP_CSS_DIR, css_name))
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
            css_file = open(css_name, 'rb')
            self.wfile.write(css_file.read())
            return
        elif self.path.endswith('.js'):
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
<<<<<<< HEAD
            js_name = split(self.path)[1]
            js_file = open(js_name, 'rb')
            self.wfile.write(js_file.read())
            return
=======
            js_name = basename(self.path)
            js_name = normpath(join(BOOTSTRAP_JS_DIR, js_name))
            js_file = open(js_name, 'rb')
            self.wfile.write(js_file.read())
            return
        elif self.path.endswith('.ttf') or self.path.endswith('.otf'):
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            font_name = basename(self.path)
            font_name = normpath(join(BOOTSTRAP_FONTS_DIR, font_name))
            font_file = open(font_name, 'rb')
            self.wfile.write(font_file.read())
            return
        elif self.path.endswith('.eot'):
            self.send_header('Content-type', 'application/vnd.ms-fontobject')
            self.end_headers()
            font_name = basename(self.path)
            font_name = normpath(join(BOOTSTRAP_FONTS_DIR, font_name))
            font_file = open(font_name, 'rb')
            self.wfile.write(font_file.read())
            return

>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078

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
<<<<<<< HEAD
            with open('main_page.html', 'r') as main_page:
=======
            with open('main_page.html', 'r', encoding='utf-8') as main_page:
>>>>>>> ce9a77f711412ed0152e9e5fe3ef527b937c8078
                content = main_page.read()
                content = content.format(host=HOST, port=PORT)
            self.wfile.write(content.encode())
        return

if __name__ == '__main__':
    httpd = HTTPServer((HOST, PORT), CustomHandler)
    httpd.serve_forever()