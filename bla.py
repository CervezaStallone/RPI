import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
pinList = [3, 5, 37]
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
x = 0
p = 1
Ron = GPIO.LOW
Roff = GPIO.HIGH
while p == 1:
    try:
        while GPIO.input(37) == GPIO.HIGH:
            if x == 0:
                GPIO.output(3, Ron)
                GPIO.output(5, Ron)
                x = 1
        while GPIO.input(37) == GPIO.LOW:
            if x == 1:
                GPIO.output(3, Roff)
                GPIO.output(5, Roff)
                x = 0
        
                
    except KeyboardInterrupt:
         GPIO.cleanup()
