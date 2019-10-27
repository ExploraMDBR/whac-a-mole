import threading

from os.path import join, realpath, dirname
import random
import sys, os, time
from gpiozero import Button, LED, TonalBuzzer
from gpiozero.tones import Tone


# =====================================
# =           CONFIGURATION           =
# =====================================
ROUND_DURATION = 30
GENERIC_DELAY = 2
DELAY_GAMEOVER = 5
MAX_BUTTONS = 4

_INTERNAL_SLEEP = 0.1
# ======  End of CONFIGURATION  =======


# ===============================
# =           GLOBALS           =
# ===============================
tonal_buzzer = TonalBuzzer(6)

buttons = [ Button(17), Button(27), Button(22), Button(23) ]
# leds = { 17:LED(25), 23:LED(26), 27:LED(24), 22:LED(16) }
leds = [LED(25), LED(24), LED(16), LED(26)]

sounds = [ 220,  220 * 10/8,  220 * 15/8, 220 * 18/8 ]
wrong = [ 220 * 18/8, 220 * 15/8, 220 ]

# ======  End of GLOBALS  =======

def error_sound():
	tonal_buzzer.play(wrong[0])
	time.sleep(GENERIC_DELAY/3)
	tonal_buzzer.play(wrong[1])
	time.sleep(GENERIC_DELAY/3)
	tonal_buzzer.play(wrong[2])
	time.sleep(GENERIC_DELAY/3)
	tonal_buzzer.stop()


def light_led(number):
	led = leds[number]
	led.on()
	tonal_buzzer.play(sounds[number])
	time.sleep(_INTERNAL_SLEEP)
	led.off()
	tonal_buzzer.stop()
	time.sleep(_INTERNAL_SLEEP)


def light_all(but = None):
	to_light = leds[:]
	if but:
		to_light.pop(but)

	for led in to_light:
		led.on()

	error_sound()	

	for led in to_light:
		led.off()

	time.sleep(_INTERNAL_SLEEP)


class Riflessi_Game:
	def __init__(self):
		self.start_at = time.time()
		self.last_button = -1
		self.available = False
		self.score = 0
		print('Game started')

	def __del__(self):
		print("Game OVER")

	def light_button(self):
		self.last_button = random.randint(0, MAX_BUTTONS -1)
		light_led(self.last_button)
		
		self.available = True
		print("LAST BLINKED=", self.last_button)

	def press_button(self, button):
		if not self.available: return
		self.available = False

		number = buttons.index(button)
		print("YOU PRESSED =", number)
		
		if number == self.last_button:
			light_led(number)
			self.score += 1
			print("========= SCORE %s ========== (+1)! " % self.score)
			time.sleep(GENERIC_DELAY)
			self.light_button()
		else:
			light_all(number)
			self.available = True
			print("###### SCORE %s ######" % self.score)



def no_button():
	print("no playing now, keep your dirty hands out of the buttons!")


def countdown(counter):
	while 1:
		counter -= 1
		print("-"*counter , counter)
		time.sleep(1)
		if counter < 1 : return

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Explora\'s Gioco dei Riflessi controller' )
	parser.add_argument('-t','--time',type=int, default=ROUND_DURATION,  help='Seconds on each round')
	args = parser.parse_args()


	while 1:
		a = input("(for now) Enter your code manually to start the game ")
		print("your code is", a)
		time.sleep(GENERIC_DELAY)
		t = threading.Thread(target=countdown, args=(args.time,))
		t.start()
		# -----------  Start  -----------
		 
		game = Riflessi_Game()
		for i,btn in enumerate(buttons):
			btn.when_pressed = game.press_button 
		
		game.light_button()

		# -----------  PLAY  -----------
		
		t.join()
		del(game)
		#Block here---
		
		# -----------  END  -----------
		

		for i,btn in enumerate(buttons):
			btn.when_pressed = no_button 
		
