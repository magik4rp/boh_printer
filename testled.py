import time

from Adafruit_LED_Backpack import BicolorBargraph24

import sys
import RPi.GPIO as GPIO

display = BicolorBargraph24.BicolorBargraph24()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = BicolorBargraph24.BicolorBargraph24(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through all bars and colors at different brightness levels.

brightness = 15

display.set_brightness(brightness)
display.clear()

display.set_bar(1, BicolorBargraph24.RED)
display.write_display()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(6,GPIO.OUT)

GPIO.output(6,GPIO.HIGH)

GPIO.setup(5,GPIO.OUT)

GPIO.output(5,GPIO.HIGH)
GPIO.setup(21,GPIO.OUT)

GPIO.output(21,GPIO.HIGH)
                        
GPIO.setup(26,GPIO.OUT)

GPIO.output(26,GPIO.HIGH)
        

