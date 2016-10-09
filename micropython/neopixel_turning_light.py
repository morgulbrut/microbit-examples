# Add your Python code here. E.g.
from microbit import *
import neopixel

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin2, 8)

# Fills a strip with a colour
def fade_strip(begin,end,delay=20,colour=(0,0,0)):
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
        sleep(delay)
        
while True:
    if accelerometer.get_x() < -400:
        print('left')
        fade_strip(0,8,20,(255,200,0))
        fade_strip(0,8,20)
    if accelerometer.get_x() > 400:
        print('right')
        fade_strip(8,0,20,(255,200,0))
        fade_strip(8,0,20)
    
    np.clear()