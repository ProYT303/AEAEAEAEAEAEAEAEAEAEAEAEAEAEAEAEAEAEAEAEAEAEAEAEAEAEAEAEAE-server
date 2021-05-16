from replit import db
import json
import string
import random
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class WebserverHandler(BaseHTTPRequestHandler):
  def _set_response(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
  def do_POST(self):
    content_length = int(self.headers['Content-Length']) 
    post_data = self.rfile.read(content_length)
    self._set_response()
    
    if self.path == "/api":
      try:
        data = json.loads(post_data.decode('utf-8'))
        LINK = data["link"]
      except:
        message = "{'message': 'Failed.'}"
        self.wfile.write(bytes(message, "utf8"))
        return 0
      s = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
      print(LINK)
      db[f"{s}"] = LINK
      Outputlink = f'https://AEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAEAE-1.mewhenamongusss.repl.co/{s}'
      message = "{'message': 'Success.', 'link': '",Outputlink,"'}"
      message = list(message)
      message = "".join(message)
      
    else:
      message = 'bruh its /api not this one'
    self.wfile.write(bytes(message, "utf8"))
  def do_GET(self):
    self._set_response()
    if self.path == '/':
      message = 'Made by the worlds most based man - Walter#8951'
    else:
      message = ""
      try:
        replaced = self.path.replace('/', '')
        if db[replaced]:
          message += f"<script>window.location = '{db[self.path]}'</script>"
      except:
        message += 'Hello.'
    self.wfile.write(bytes(message, "utf8"))
  def log_message(self, format, *args):
      pass
def run(server_class=HTTPServer, handler_class=WebserverHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("starting http server..")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('stopping http server...')
run()
