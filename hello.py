# -*- coding: utf-8 -*-


def app(environ, start_response):
    """Simplest possible application object"""
    # data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        # ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return [str(i) + "\n" for i in environ['QUERY_STRING'].split("&")]
