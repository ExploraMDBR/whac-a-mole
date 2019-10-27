#!/usr/bin/env python3

import signal
from sys import exit
import datetime
import time
import json
import threading

import ws_server
import http_server
import riflessi

delays = {
	"INSTRUCTIONS" : 5,
	"PRE_COUNT" : 3,
	"FINAL": 10
}

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
		print("-"*counter , counter)
		time.sleep(1)
		if counter < 1 : return

def main():
	import argparse

	parser = argparse.ArgumentParser(description='Explora\'s Gioco dei Riflessi controller' )
	parser.add_argument('-t','--time',type=int, default=riflessi.ROUND_DURATION,  help='Seconds on each round')
	args = parser.parse_args()

	#START SERVERS
	ws_server.start()
	print("PARI Websocket server started at port {}\non {}"\
		.format(ws_server.WS_PORT, datetime.datetime.now()))

	http_server.start()
	print("PARI HTTP server started at port {}\non {}"\
		.format(http_server.PORT, datetime.datetime.now()))
	
	#HANDLE SIGTERM
	def close_sig_handler(signal, frame):
		print("\nInterrupt signal received, cleaning up..")
		ws_server.close()
		http_server.close()
		exit()

	signal.signal(signal.SIGINT, close_sig_handler)

	#PLAY LOOP

	while 1:
		ws_server.send(get_control_json("IDLE"))
		a = input("(for now) Enter your code manually to start the game ")
		print("your code is", a)

		ws_server.send(get_control_json("INSTRUCTIONS"))
		print("INSTRUCTIONS screen, waiting ", delays["INSTRUCTIONS"], "seconds")
		time.sleep(delays["INSTRUCTIONS"])

		ws_server.send(get_control_json("PRE_COUNT"))
		print("PRE_COUNT screen, waiting ", delays["PRE_COUNT"], "seconds")
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
		print("FINAL screen, waiting ", delays["FINAL"], "seconds")
		time.sleep(delays["FINAL"])

		for i,btn in enumerate(riflessi.buttons):
			btn.when_pressed = riflessi.no_button 


	


if __name__ == '__main__':
	main()