from gpiozero import Button, LED
from time import sleep

leds = [ LED(17), LED(10), LED(5),
		LED(13), LED(23), LED(16) ]

btns = [ Button(27), Button(9), Button(6),
		Button(19), Button(24), Button(20) ]

def press_button(a):
	print("pres", a)


for btn in btns:
	btn.when_pressed = press_button 

while 1:
	sleep(0.2)
	for led in leds:
		led.on()
	sleep(0.2)
	for led in leds:
		led.off()
