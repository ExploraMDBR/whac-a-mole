from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
from datetime import datetime
import threading
import re
from sys import stdout
__TEMP_condition = threading.Condition()
__TEMP_user_creation = 0

def create_user(code):
	global __TEMP_condition
	global __TEMP_user_creation

	__TEMP_user_creation = code
	with __TEMP_condition:
		__TEMP_condition.notify_all()


WS_PORT = 8001
clients = []

def get_comm_json(msg):
	return json.dumps({
		"msg": msg,
		"state": "system",
		"count": 0
		})

def dump_to_console(msg, xtra=None):
	print("[WS] {} {}".format(msg, xtra))
	stdout.flush()

class Pari_Websocket_Handler(WebSocket):


	def handleMessage(self):
		try:
			is_new_user = re.match("NEW_USER ([0-9]{4})", self.data)
			if is_new_user:
				create_user(is_new_user.group(1))
				

		except Exception as e:
			dump_to_console("Problem creating new user from WS:", e)

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

