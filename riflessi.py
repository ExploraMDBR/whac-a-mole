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
DELAY_GAMEOVER = 0.5
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

# ======  End of GLOBALS  =======

def light_led(number):
	led = leds[number]
	led.on()
	time.sleep(_INTERNAL_SLEEP)
	led.off()
	time.sleep(_INTERNAL_SLEEP)


def light_all(but = None):
	to_light = leds[:]
	if but:
		to_light.pop(but)

	for led in to_light:
		led.on()

	time.sleep(_INTERNAL_SLEEP)

	for led in to_light:
		led.off()

	time.sleep(_INTERNAL_SLEEP)


class Riflessi_Game:
	def __init__(self):
		self.start_at = time.time()
		self.last_button = -1
		self.score = 0
		print('Game started')

	def light_button(self):
		self.last_button = random.randint(0, MAX_BUTTONS -1)
		light_led(self.last_button)
		print("LAST =", self.last_button)

	def press_button(self, button):
		number = buttons.index(button)
		print("PRESSED =", number)
		if number == self.last_button:
			light_led(number)
			self.score += 1
		else:
			light_all(number)		

		print("========= SCORE %s ==========" % self.score)


if __name__ == '__main__':
	game = Riflessi_Game()

	game.light_button()

	for i,btn in enumerate(buttons):
		btn.when_pressed = game.press_button 

	while 1:
		pass

	# while 1:
	# 	for led in leds:



