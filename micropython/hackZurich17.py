# Haked together at/for MakeZürich 17.
# Based on:
# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
import radio, music
from microbit import *
# Create the "flash" animation frames. Can you work out how it's done?
def flash_image(image):
    return [image*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

def image2string(image):
    return ''.join(str(image).split('\'')[1::2])

def sound2string(sound):
   return(','.join(sound[:]))
 
# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send(image2string(Image.HEART))  
    if button_b.was_pressed():
        radio.send('S:'+sound2string(music.BA_DING))
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming:
        incoming_u = str(incoming)
        print('[RX]: '+incoming_u)
        if incoming_u[0:2] == 'T:':      #Print text
            for i in range(3):
                display.show(incoming_u[2:]+' ')
        if incoming_u[0:2] == 'S:':    #Play sound
            music.play(incoming_u[2:].split(','),wait=False)
        else: 
            try:
                display.show(flash_image(Image(incoming_u)),delay=100,wait=False)
            except:
                pass
