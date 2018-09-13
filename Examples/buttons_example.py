from gpiozero import LED
from gpiozero import Button

error_led = LED(4)

up_button = Button(7)
center_button = Button(12)
down_button = Button(16)
left_button = Button(20)
right_button = Button(21)

while True:
    any_held = False
    if up_button.is_held:
        print "UP"
        any_held = True
    if center_button.is_held:
        print "CENTER"
        any_held = True
    if down_button.is_held:
        print "DOWN"
        any_held = True
    if left_button.is_held:
        print "LEFT"
        any_held = True
    if right_button.is_held:
        print "RIGHT"
        any_held = True
    error_led.value = any_held
