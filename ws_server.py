from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

WS_PORT = 8000

class Pari_Websocket_Handler(WebSocket):
	def respond_json(self, msg):
		self.sendMessage(get_comm_json(msg))

	def respond(self, msg, code = 418):
		self.sendMessage(msg)

	def handleMessage(self):
		tokens = self.data.split()
		cmd = "do_" + tokens[0].upper()
		tokens = tokens[1:]

		u.dump_to_debug("received CMD: {} | TOKENS: {}".format(cmd, tokens))

		run_command(cmd, tokens, self.respond)

	def handleConnected(self):
		clients.append(self)
		self.sendMessage(
			get_comm_json("Notochord server: up\n (%d clients connected)")
			% len(clients)
		)
		u.dump_to_log(
			"Client connected: ({}:{}), total {} clients".format(
				self.address[0], self.address[1], len(clients)
			)
		)

	def handleClose(self):
		global detached
		clients.remove(self)
		u.dump_to_log(
			"Client removed: ({}:{}), total {} clients".format(
				self.address[0], self.address[1], len(clients)
			)
		)
		u.dump_to_debug(detached) 

		if len(clients) == 0 and not detached:
			do_CLOSE()

ws_server = None

def start():
	global ws_server
	ws_server = SimpleWebSocketServer("", WS_PORT, Pari_Websocket_Handler)

def serveonce():
	ws_server.serveonce()

def close():
	ws_server.close()