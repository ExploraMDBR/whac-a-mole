#!/usr/bin/env python3

import signal
from sys import exit
import datetime
import time
import json
import threading
from sys import stdout

import ws_server
import http_server
import riflessi

delays = {
	"INSTRUCTIONS" : 5,
	"PRE_COUNT" : 3,
	"FINAL": 10
}

def dump_to_console(*args):
	args = [str(a) for a in args]
	print("[MAIN]", " ".join(args))
	stdout.flush()

def get_control_json(state, count = 0):
	return json.dumps({
		"msg": "",
		"state": state,
		"count": count
		})

def countdown(counter):
	while 1:
		ws_server.send(get_control_json("COUNTDOWN", counter))
		counter -= 1
		# print("-"*counter , counter)
		time.sleep(1)
		if counter < 1 : return

def main():
	import argparse

	parser = argparse.ArgumentParser(description='Explora\'s Gioco dei Riflessi controller' )
	parser.add_argument('-t','--time',type=int, default=riflessi.ROUND_DURATION,  help='Seconds on each round')
	args = parser.parse_args()

	#START SERVERS
	ws_server.start()
	dump_to_console("PARI Websocket server started at port {}\non {}"\
		.format(ws_server.WS_PORT, datetime.datetime.now()))

	http_server.start()
	dump_to_console("PARI HTTP server started at port {}\non {}"\
		.format(http_server.PORT, datetime.datetime.now()))
	
	#HANDLE SIGTERM
	def close_sig_handler(signal, frame):
		dump_to_console("\nInterrupt signal received, cleaning up..")
		ws_server.close()
		http_server.close()
		exit()

	signal.signal(signal.SIGINT, close_sig_handler)

	#PLAY LOOP

	while 1:
		ws_server.send(get_control_json("IDLE"))
		with ws_server.__TEMP_condition:
			while not ws_server.__TEMP_user_creation:
				ws_server.__TEMP_condition.wait()

		dump_to_console("your code is", ws_server.__TEMP_user_creation)
		ws_server.__TEMP_user_creation = 0

		ws_server.send(get_control_json("INSTRUCTIONS"))
		dump_to_console("INSTRUCTIONS screen, waiting ", delays["INSTRUCTIONS"], "seconds")
		time.sleep(delays["INSTRUCTIONS"])

		ws_server.send(get_control_json("PRE_COUNT"))
		dump_to_console("PRE_COUNT screen, waiting ", delays["PRE_COUNT"], "seconds")
		time.sleep(delays["PRE_COUNT"])

		t = threading.Thread(target=countdown, args=(args.time,))
		t.start()
		# -----------  Start  -----------
		 
		game = riflessi.Riflessi_Game()
		for i,btn in enumerate(riflessi.buttons):
			btn.when_pressed = game.press_button 
		
		game.light_button()

		# -----------  PLAY  -----------
		
		t.join() #--- Block here ---
		del(game)
		
		
		# -----------  END  -----------
		ws_server.send(get_control_json("FINAL"))
		dump_to_console("FINAL screen, waiting ", delays["FINAL"], "seconds")
		time.sleep(delays["FINAL"])

		for i,btn in enumerate(riflessi.buttons):
			btn.when_pressed = riflessi.no_button 


	


if __name__ == '__main__':
	main()