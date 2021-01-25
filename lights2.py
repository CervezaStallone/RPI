#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.1

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  GPIO.output(9, GPIO.LOW)
  time.sleep(SleepTimeL);
  GPIO.output(3, GPIO.LOW)
  GPIO.output(10, GPIO.LOW)
  time.sleep(SleepTimeL);
  GPIO.output(4, GPIO.LOW)
  GPIO.output(22, GPIO.LOW)
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.LOW)
  GPIO.output(27, GPIO.LOW)
  time.sleep(0.2);
  GPIO.output(2, GPIO.HIGH)
  GPIO.output(9, GPIO.HIGH)
  time.sleep(SleepTimeL);
  GPIO.output(3, GPIO.HIGH)
  GPIO.output(10, GPIO.HIGH)
  time.sleep(SleepTimeL);
  GPIO.output(4, GPIO.HIGH)
  GPIO.output(22, GPIO.HIGH)
  time.sleep(SleepTimeL);
  GPIO.output(17, GPIO.HIGH)
  GPIO.output(27, GPIO.HIGH)
  GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()

