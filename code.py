# A quick template and troubleshooting help App 
# for the Adafruit Mini Color TFT with Joystick FeatherWing
# Included is the DisplayIO library to modify the screen output
# If you connected everything correctly this code should work

import time
import displayio
import terminalio
from adafruit_display_text.label import Label
from adafruit_featherwing import minitft_featherwing

minitft = minitft_featherwing.MiniTFTFeatherWing()

uiGroup = displayio.Group(max_size=20)

text_area = Label(terminalio.FONT, text=' ', max_glyphs=20)
text_area.x = 40
text_area.y = 32

uiGroup.append(text_area)
minitft.display.show(uiGroup)

while True:
    buttons = minitft.buttons

    if buttons.right:
        text_area.text = "Button RIGHT!"

    if buttons.down:
        text_area.text = "Button DOWN!"

    if buttons.left:
        text_area.text = "Button LEFT!"

    if buttons.up:
        text_area.text = "Button UP!"

    if buttons.select:
        text_area.text = "Button SELECT!"

    if buttons.a:
        text_area.text = "Button A!"

    if buttons.b:
        text_area.text = "Button B!"

    time.sleep(0.2)
    text_area.text = "Press a Button"