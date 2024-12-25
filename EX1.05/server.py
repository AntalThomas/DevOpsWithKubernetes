from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 3000
with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
  print("serving at port", PORT)
  httpd.serve_forever()