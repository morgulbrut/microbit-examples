# Add your Python code here. E.g.
from microbit import *
import neopixel
counter = 0
no_of_leds = 10
# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin2, no_of_leds)

def bitfield(n):
    return [n >> i & 1 for i in range (no_of_leds-1,-1,-1)]

def show_number(n):
    leds = bitfield(n)
    for i in range(0,len(np)):
        try:
            if leds[i] == 1:
                np[i] = (0,0,255)
            else:
                np[i] = (0,0,0)
        except IndexError:
            np[i] = (0,0,0)
    np.show()
