# Add your Python code here. E.g.
from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin2, 8)

def wheel(wheel_pos):
    wheel_pos = 255 - wheel_pos
    if (wheel_pos < 85):
        return (255-wheel_pos*3,0,wheel_pos*3)
    elif (wheel_pos < 170):
        wheel_pos -= 85
        return (0, wheel_pos*3, 255-wheel_pos*3)
    else:
        wheel_pos -= 170
        return (wheel_pos*3, 255-wheel_pos*3,0)
 
def rainbow(wait_time):
    for i in range(0,256-len(np)):
        for pixel_id in range(0,len(np)):
            np[pixel_id] = wheel(i+pixel_id)
        np.show();
        sleep(wait_time)
        
while True:
    rainbow(20)
