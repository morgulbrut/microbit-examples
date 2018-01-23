# Add your Python code here. E.g.
from microbit import *
import neopixel

no_of_pixels = 8
# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin5, no_of_pixels)

# Fills a strip with a colour
def fade_strip(begin,end,delay=20,colour=(0,0,0),accel=0):
    if begin < end: 
        step = 1
    else: 
        # begin and end decremented because the way range() works.
        step = -1
        begin -= 1
        end -= 1
    for pixel_id in range(begin,end,step):
        np[pixel_id] = colour
        np.show()
        sleep(10000/accel)
        
while True:
    accel = accelerometer.get_x()
    if accel > 400:
        fade_strip(0,no_of_pixels,colour=(255,200,0),accel=accel)
        fade_strip(0,no_of_pixels,accel=accel)
    if accel < -400:
        fade_strip(no_of_pixels,0,colour=(255,200,0),accel=-accel)
        fade_strip(no_of_pixels,0,accel=-accel)
    
    np.clear()