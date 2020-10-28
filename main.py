import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor_pins = [4,17,27,22]
button_pins = [23,24,25,12]
question = 1
asked = False
for pin in motor_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
for pin in button_pins:
    GPIO.setup(pin,GPIO.IN)
GPIO.setup(8,GPIO.OUT)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

while True:
    d = GPIO.input(23)
    c = GPIO.input(24)
    b = GPIO.input(25)
    a = GPIO.input(12)
    if question == 1:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if d:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    
    elif question == 2:
        GPIO.output(8,False)
        incorrect_buttons = [d,c,a]
        if b:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    elif question == 3:
        GPIO.output(8,False)
        incorrect_buttons = [d,c,b]
        if a:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
        
    elif question == 4:
        GPIO.output(8,False)
        incorrect_buttons = [d,b,a]
        if c:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    
    elif question == 5:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if d:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    
    elif question == 6:
        GPIO.output(8,False)
        incorrect_buttons = [d,b,a]
        if c:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')

    elif question == 7:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if d:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    

    elif question == 8:
        GPIO.output(8,False)
        incorrect_buttons = [c,d,b]
        if a:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    

    elif question == 9:
        GPIO.output(8,False)
        incorrect_buttons = [a,d,c]
        if b:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    

    elif question == 10:
        GPIO.output(8,False)
        incorrect_buttons = [c,b,a]
        if d:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')  
    

    elif question == 11:
        GPIO.output(8,False)
        incorrect_buttons = [d,c,b]
        if a:
            GPIO.output(8,True)
            print('well done, moving on to next question')
            question += 1
            time.sleep(0.5)
            # Green LED is on
        else:
            if any(incorrect_buttons) == True:
                GPIO.output(8,False)
                print('incorrect, keep on trying')
    time.sleep(0.15)
    
    
    
    
    
    
    
    
    