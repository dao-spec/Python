from wsgiref.simple_server import make_server
from html import apploication

httpd = make_server('', 8000, apploication)
print('Serving HTTP on port 8000 ....')
httpd.serve_forever()