import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json
import threading

PORT = 8080

STATIC_DIR = "public/"

last_error = None
error_page = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="30">
    <title>PARI error message</title>
</head>
<body>
    <p>{}</p>
    <p>Retriying in 5 seconds..</p>
</body>
</html>'''

class Request_Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global last_error

        if last_error:
            self.error(last_error)
            return

        self.parsed = urlparse(self.path)

        if self.path == "/status":
            self.respond(json.dumps({"status": "running"}), 200)
            return

        self.path = STATIC_DIR + self.path

        #STATIC SERVER
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        

    def handle_http(self, msg, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return msg

    def respond(self, msg, code = 418):
            response = self.handle_http(msg, code)
            self.wfile.write(response.encode('utf-8'))

    def error(self, err):
        self.send_response(500)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = error_page.format(err)
        self.wfile.write(response.encode('utf-8'))

http_server = None
def serve_forever():
    global http_server
    http_server = socketserver.TCPServer(("", PORT), Request_Handler)
    http_server.serve_forever()

t = threading.Thread(target = serve_forever)

def start():
    t.start()

def close():
    if http_server:
        http_server.server_close()
        http_server.shutdown()
    if t.is_alive():
        t.join()
