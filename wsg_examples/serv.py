from wsgiref.simple_server import make_server


def simple(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')] # HTTP Headers
    start_response(status, headers)
    ret = ['[{k}] == [{v}]\n'.format(k=k,v=v) for k,v in environ.items()]
    ret = [line.encode() for line in ret]
    return ret

httpd = make_server('', 8070, simple)
httpd.serve_forever()