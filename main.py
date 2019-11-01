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
import database_manager as db

delays = {
	"INSTRUCTIONS" : 5,
	"PRE_COUNT" : 3,
	"PLAY": 2,
	"FINAL": 10
}

barcode_dev = '/dev/hidraw0'

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

def code_to_db(code):
	try:
		gender, age = code.split("2")
	except ValueError as e:
		return "Wrong code: Cannot split in 2 tokens";
	
	gen_convert = ["femmina", "maschio"]
	gender = int(gender)
	if gender > len(gen_convert): return "Wrong code: Not valid gender part"
	gender = gen_convert[gender]
	
	age = "{:2d}".format(int(age))

	db.insert_user(gender, age)
	db.commit()
	return False

def code_input_to_number(input):
	order = [1,2,3,4,5,6,7,8,9,0]
	return order[input-30]

def main():
	import argparse

	parser = argparse.ArgumentParser(description='Explora\'s Gioco dei Riflessi controller' )
	parser.add_argument('-t','--time',type=int, default=riflessi.ROUND_DURATION,  help='Seconds on each round')
	args = parser.parse_args()
	
	#START HTTP SERVER	
	http_server.start()
	dump_to_console("PARI HTTP server started at port {}\non {}"\
		.format(http_server.PORT, datetime.datetime.now()))
	
	#GET BARCODE READER DEVICE
	http_server.last_error = "Opening Barcode reader."
	while 1:
		try:
			time.sleep(5)
			f = open(barcode_dev)
			http_server.last_error = None
			dump_to_console("Barcode reader found at {}".format(barcode_dev))
			break
		except Exception as e:
			http_server.last_error = "Can't open Barcode reader."
			dump_to_console(http_server.last_error)


	#START WS SERVER
	ws_server.start()
	dump_to_console("PARI Websocket server started at port {}\non {}"\
		.format(ws_server.WS_PORT, datetime.datetime.now()))


	#Connect to DB
	db.start()

	
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
		
		the_code = ""
		while 1:
			c = f.read(1)
			if ord(c) == 40: break

			if ord(c):
				the_code += str(code_input_to_number(ord(c)))
				stdout.flush()


		db_error = code_to_db(the_code)
		if db_error:
			dump_to_console(db_error)
			continue


		dump_to_console("Scanned code", the_code)

		ws_server.send(get_control_json("INSTRUCTIONS"))
		# dump_to_console("INSTRUCTIONS screen, waiting ", delays["INSTRUCTIONS"], "seconds")
		time.sleep(delays["INSTRUCTIONS"])

		for i in range(delays["PRE_COUNT"]):
			ws_server.send(get_control_json("PRE_COUNT", str(delays["PRE_COUNT"] - i)))
			time.sleep(1)

		ws_server.send(get_control_json("PLAY"))
		# dump_to_console("PLAY screen, waiting ", delays["PRE_COUNT"], "seconds")
		time.sleep(delays["PLAY"])

		t = threading.Thread(target=countdown, args=(args.time,))
		t.start()
		# -----------  Start  -----------
		 
		game = riflessi.Riflessi_Game()
		for i,btn in enumerate(riflessi.buttons):
			btn.when_pressed = game.press_button 
		
		game.light_button()

		# -----------  PLAY  -----------
		
		t.join() #--- Block here ---

		# -----------  END  -----------
		ws_server.send(get_control_json("FINAL", str(game.score)))
		del(game)
		# dump_to_console("FINAL screen, waiting ", delays["FINAL"], "seconds")
		
		time.sleep(delays["FINAL"])

		for i,btn in enumerate(riflessi.buttons):
			btn.when_pressed = riflessi.no_button 


	


if __name__ == '__main__':
	main()