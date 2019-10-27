import signal
from sys import exit
import datetime

import ws_server
import http_server


def main():
	#start ws server
	
	ws_server.start()
	print("PARI Websocket server started at port {}\non {}"\
		.format(ws_server.WS_PORT, datetime.datetime.now()))

	def close_sig_handler(signal, frame):
		print("\nInterrupt signal received, cleaning up..")
		ws_server.close()
		http_server.close()
		exit()
		

	signal.signal(signal.SIGINT, close_sig_handler)

	http_server.start()
	print("PARI HTTP server started at port {}\non {}"\
		.format(http_server.PORT, datetime.datetime.now()))


	while True:
		ws_server.serveonce()


if __name__ == '__main__':
	main()