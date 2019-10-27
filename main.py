#!/usr/bin/env python3

import signal
from sys import exit
import datetime
import time
import json

import ws_server
import http_server

def get_control_json(state, count = 0):
	return json.dumps({
		"msg": "",
		"state": state,
		"count": count
		})


def main():
	
	ws_server.start()
	print("PARI Websocket server started at port {}\non {}"\
		.format(ws_server.WS_PORT, datetime.datetime.now()))

	http_server.start()
	print("PARI HTTP server started at port {}\non {}"\
		.format(http_server.PORT, datetime.datetime.now()))
	
	def close_sig_handler(signal, frame):
		print("\nInterrupt signal received, cleaning up..")
		ws_server.close()
		http_server.close()
		exit()
		

	signal.signal(signal.SIGINT, close_sig_handler)

	while 1:
		ws_server.send(get_control_json("IDLE"))
		time.sleep(1)

		ws_server.send(get_control_json("INSTRUCTIONS"))
		time.sleep(1)

		ws_server.send(get_control_json("PRE-COUNT"))
		time.sleep(1)

		ws_server.send(get_control_json("PLAY"))
		time.sleep(1)

		ws_server.send(get_control_json("COUNTDOWN"))
		time.sleep(1)

		ws_server.send(get_control_json("FINAL"))
		time.sleep(1)
	


if __name__ == '__main__':
	main()