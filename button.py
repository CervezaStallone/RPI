import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
pinList = [3, 5, 37]
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 37 to be an input pin
#Defining VARS
p = 1
i = 0
on = GPIO.HIGH
off = GPIO.LOW
Ron = GPIO.LOW
Roff = GPIO.HIGH
switch = GPIO.input(37)
buttonReleaseTime = 1.5
try:
    while p == 1: #constant loop
        while not GPIO.input(37): #if there is no iput then do nothing
            time.sleep(0.01)
        if i == 0:
            GPIO.output(3, Ron)
            GPIO.output(5, Ron)
            print("ON")
            i = 1
            time.sleep(buttonReleaseTime)
        else:
            GPIO.output(3, Roff)
            GPIO.output(5, Roff)
            print("OFF")
            i = 0
            time.sleep(buttonReleaseTime)
except KeyboardInterrupt:
    GPIO.cleanup()
