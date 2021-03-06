# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

from Adafruit_LED_Backpack import BicolorBargraph24

import sys
# Create display instance on default I2C address (0x70) and bus number.
display = BicolorBargraph24.BicolorBargraph24()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = BicolorBargraph24.BicolorBargraph24(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through all bars and colors at different brightness levels.

brightness = 15
val = int(float(sys.argv[1]))
print('VALUE SHOULD BE INTEGER: ', val)
val = val % 23
display.set_brightness(brightness)
display.clear()
if val > 0:
     for x in range(val):
        # if val > 14:
            display.set_bar(x, BicolorBargraph24.RED)
            display.write_display()
        # else:
        #     if val > 7 and val<15:
        #         display.set_bar(x, BicolorBargraph24.YELLOW)
        #         display.write_display()
        #     else:
        #         display.set_bar(x, BicolorBargraph24.GREEN)
        #         display.write_display()
else:
    j = 1
    #m = 1
    #for m in range(20):
    while True:
        if j == 1:
            display.set_bar(0, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(1, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(2, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(3, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(4, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(5, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(6, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(7, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(8, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(9, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(10, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(11, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(12, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(13, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(14, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(15, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(16, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(17, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(18, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(19, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(20, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(21, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(22, BicolorBargraph24.RED)
            display.write_display()
            display.set_bar(23, BicolorBargraph24.RED)
            display.write_display()

            j -= 1
        else:
            display.set_bar(0, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(1, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(2, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(3, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(4, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(5, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(6, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(7, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(8, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(9, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(10, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(11, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(12, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(13, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(14, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(15, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(16, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(17, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(18, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(19, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(20, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(21, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(22, BicolorBargraph24.OFF)
            display.write_display()
            display.set_bar(23, BicolorBargraph24.OFF)
            display.write_display()

            j += 1
i = 1
while val > 0:
    # if val > 14:
        if i == 1:
            display.set_bar(val, BicolorBargraph24.RED)
            display.write_display()
            i -= 1
        else:
            display.set_bar(val, BicolorBargraph24.OFF)
            display.write_display()
            i += 1
        time.sleep(0.5)
    # else:
        # if val > 7 and val<15:
        #     if i == 1:
        #         display.set_bar(val, BicolorBargraph24.YELLOW)
        #         display.write_display()
        #         i -= 1
        #     else:
        #         display.set_bar(val, BicolorBargraph24.OFF)
        #         display.write_display()
        #         i += 1
        #     time.sleep(0.5)
        # else:
        #     if i == 1:
        #         display.set_bar(val, BicolorBargraph24.GREEN)
        #         display.write_display()
        #         i -= 1
        #     else:
        #         display.set_bar(val, BicolorBargraph24.OFF)
        #         display.write_display()
        #         i += 1
        #     time.sleep(0.5)
##    if i == 1:
##        display.set_bar(val, BicolorBargraph24.RED)
##        display.write_display()
##        i -= 1
##    else:
##        display.set_bar(val, BicolorBargraph24.OFF)
##        display.write_display()
##        i += 1
##    time.sleep(0.5)

##while True:
##    # Set display brightness (15 is max, 0 is min).
##    display.set_brightness(brightness)
##    for i in range(24):
##        # Clear the display buffer.
##        display.clear()
##        # Light up 3 bars, each a different color and position.
##        display.set_bar(i,   BicolorBargraph24.RED)
##        display.set_bar(i+1, BicolorBargraph24.GREEN)
##        display.set_bar(i+2, BicolorBargraph24.YELLOW)
##        # Write the display buffer to the hardware.  This must be called to
##        # update the actual display LEDs.
##        display.write_display()
##        # Delay for half a second.
##        time.sleep(0.5)
##    # Decrease brightness, wrapping back to 15 if necessary.
##    brightness -= 1
##    if brightness == 0:
##        brightness = 15
