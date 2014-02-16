# -*- coding: utf-8 -*-
from http import server
from urllib import parse

HOST = '127.0.0.1'
PORT = 80




class GetHandler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        message_parts = [
            'CLIENT VALUES:',
            'client_address={0} ({1})'.format(self.client_address, self.address_string()),
            'command={0}'.format(self.command),
            'path={0}'.format(self.path),
            'real path={0}'.format(parsed_path.path),
            'query={0}'.format(parsed_path.query),
            'request_version={0}'.format(self.request_version),
            '',
            'SERVER VALUES:',
            'server_version={0}'.format(self.server_version),
            'sys_version={0}'.format(self.sys_version),
            'protocol_version={0}'.format(self.protocol_version),
            '',
            'HEADERS RECEIVED:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append('{0}={1}'.format(name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server...')
    server.serve_forever()