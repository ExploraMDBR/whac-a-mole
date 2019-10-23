import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json

PORT = 8080

STATIC_DIR = "public/"

class Request_Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.parsed = urlparse(self.path)

        if self.path == "/status":
            self.respond(json.dumps({"status": "running"}), 200)
            return

        # is_command = self.cmd_lookup.match(self.parsed.path)

        # if is_command:
        #     self.notochord_command(is_command.group(1))
        # elif self.path in self.redirs:
        #     self.respond(get_comm_json(self.redirs[self.path]["msg"]),\
        #                                  self.redirs[self.path]["status"])
        # else:
        self.path = STATIC_DIR + self.path

        print("STATIC_RESPONSE", http.server.SimpleHTTPRequestHandler.do_GET(self))
        #STATIC SERVER



    def handle_http(self, msg, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        return msg

    def respond(self, msg, code = 418):
            response = self.handle_http(msg, code)
            self.wfile.write(response.encode('utf-8'))


with socketserver.TCPServer(("", PORT), Request_Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()