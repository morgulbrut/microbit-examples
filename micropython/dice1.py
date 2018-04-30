# import microbit and random modules
from microbit import *
import random

# create a list of strings called VALS
VALS    = ["Eins",
            "Zwei",
            "Drei",
            "Vier",
            "Fuenf",
            "Sechs"
           ]

# create an endless loop waiting for button_a to be pressed
while True:
    if button_a.is_pressed():
        display.scroll(random.choice(VALS))
    sleep(100)