import RPi.GPIO as GPIO
import time

pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.IN)

while True:
    if GPIO.input(pin):
        print('hi')
    else:
        print('bye')
    time.sleep(0.1)