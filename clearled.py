import time

from Adafruit_LED_Backpack import BicolorBargraph24

import sys
import RPi.GPIO as GPIO
# Create display instance on default I2C address (0x70) and bus number.
display = BicolorBargraph24.BicolorBargraph24()
display.begin()
display.clear()
for x in range(23):
    display.set_bar(x, BicolorBargraph24.OFF)
    display.write_display()
    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.output(21,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(19,GPIO.LOW)
GPIO.output(13,GPIO.LOW)