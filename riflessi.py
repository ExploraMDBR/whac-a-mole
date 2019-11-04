import threading

from os.path import join, realpath, dirname
import random
import sys, os, time
from gpiozero import Button, LED
# from gpiozero.tones import Tone


# =====================================
# =           CONFIGURATION           =
# =====================================
ROUND_DURATION = 30
NEXT_LED = 0.2
DELAY_GAMEOVER = 5
MAX_BUTTONS = 6

LED_ON_DURATION = 1
# ======  End of CONFIGURATION  =======


# ===============================
# =           GLOBALS           =
# ===============================
# tonal_buzzer = TonalBuzzer(6)

buttons = [ Button(27), Button(9), Button(6),
		Button(19), Button(24), Button(20) ]
# leds = { 17:LED(25), 23:LED(26), 27:LED(24), 22:LED(16) }
leds = [ LED(17), LED(10), LED(5),
		LED(13), LED(23), LED(16) ]

sounds = [ 220,  220 * 10/8,  220 * 15/8, 220 * 18/8 ]
wrong = [ 220 * 18/8, 220 * 15/8, 220 ]

# ======  End of GLOBALS  =======

def error_sound():
	pass
	# tonal_buzzer.play(wrong[0])
	# time.sleep(GENERIC_DELAY/3)
	# tonal_buzzer.play(wrong[1])
	# time.sleep(GENERIC_DELAY/3)
	# tonal_buzzer.play(wrong[2])
	# time.sleep(GENERIC_DELAY/3)
	# tonal_buzzer.stop()


def light_led(number, invert=False):
	led = leds[number]
	if not invert:
		led.on()
	else:
		led.off()
	# tonal_buzzer.play(sounds[number])

	# tonal_buzzer.stop()



def light_all(but = None, invert=False):
	to_light = leds[:]
	if but:
		to_light.pop(but)

	for led in to_light:
		if not invert:
			led.on()
		else:
			led.off()



class Riflessi_Game:
	def __init__(self):
		self.start_at = time.time()
		self.last_button = -1
		self.available = False
		self.score = 0
		light_all(invert= True)
		print('Game started')

	def __del__(self):
		light_all(invert= True)
		print("Game OVER")

	def light_button(self):
		self.last_button = random.randint(0, MAX_BUTTONS -1)
		light_led(self.last_button)
		
		self.available = True
		print("LAST BLINKED=", self.last_button)

	def press_button(self, button):
		print("**************")
		number = buttons.index(button)
		print("YOU PRESSED =", number)
		
		if not self.available: return
		self.available = False

		
		if number == self.last_button:
			light_all(invert= True)
			self.score += 1
			print("========= SCORE %s ========== (+1)! " % self.score)
			time.sleep(NEXT_LED)
			self.light_button()
		else:
			# light_all(number)
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
		time.sleep(0.5)
		t = threading.Thread(target=countdown, args=(args.time,))
		t.start()
		# -----------  Start  -----------
		
		game = Riflessi_Game()
		def press_test_button(button):
			print(button)

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
		
