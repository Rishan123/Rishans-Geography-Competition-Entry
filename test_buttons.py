import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.IN)

while True:
    if GPIO.input(12):
        print('hi')
    else:
        print('bye')
    time.sleep(0.1)