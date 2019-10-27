from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
from datetime import datetime
import threading

WS_PORT = 8001
clients = []

def get_comm_json(msg):
	return json.dumps({
		"msg": msg,
		"state": "system",
		"count": 0
		})

def dump_to_console(msg):
	print("[WS] {} {}".format(datetime.now(), msg))

class Pari_Websocket_Handler(WebSocket):


	def handleMessage(self):
		dump_to_console("incoming MSG: {}".format(self.data))

	def handleConnected(self):
		clients.append(self)
		self.sendMessage(
			get_comm_json("Pari WS server: UP (%d clients connected)")
			% len(clients)
		)
		dump_to_console(
			"Client connected: ({}:{}), total {} clients".format(
				self.address[0], self.address[1], len(clients)
			)
		)

	def handleClose(self):
		dump_to_console(
			"[Client removed: ({}:{}), total {} clients".format(
				self.address[0], self.address[1], len(clients)
			)
		)
		clients.remove(self)
		
def send(content):
	for c in clients:
		c.sendMessage(content)

ws_server = None

def serveforever():
	global ws_server
	ws_server = SimpleWebSocketServer("", WS_PORT, Pari_Websocket_Handler)
	try:
		ws_server.serveforever()
	except ValueError as e:
		pass

t = threading.Thread(target = serveforever)

def start():
	t.start()


def close():
	if ws_server:
		ws_server.close()
	if t.is_alive():
		t.join()

