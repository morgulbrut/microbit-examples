# Add your Python code here. E.g.
from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin2, 8)

while True:
    #Iterate over each LED in the strip

    for pixel_id in range(0, len(np)):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (blue, green, green)

        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(100)