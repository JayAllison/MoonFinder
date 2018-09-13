from gpiozero import LED
from gpiozero import Button

# this is how I've built my telescope handset
error_led = LED(4)

up_button = Button(7)
center_button = Button(12)
down_button = Button(16)
left_button = Button(20)
right_button = Button(21)

print "      ",

while True:
    up = up_button.value
    center = center_button.value
    down = down_button.value
    left = left_button.value
    right = right_button.value

    up_symbol = "U" if up else "-"
    center_symbol = "C" if center else "-"
    down_symbol = "D" if down else "-"
    left_symbol = "L" if left else "-"
    right_symbol = "R" if right else "-"

    print "\b\b\b\b\b\b" + up_symbol + center_symbol + down_symbol + left_symbol + right_symbol,

    error_led.value = up or center or down or left or right
