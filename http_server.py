import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json
import threading

PORT = 8080

STATIC_DIR = "public/"

class Request_Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
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

http_server = None
def serve_forever():
    global http_server
    with socketserver.TCPServer(("", PORT), Request_Handler) as httpd:
        http_server = httpd
        httpd.serve_forever()

t = threading.Thread(target = serve_forever)

def start():
    t.start()

def close():
    if http_server:
        http_server.server_close()
        http_server.shutdown()
    if t.is_alive():
        t.join()
