from gpiozero import Button
from signal import pause

class UserInterface(object):

    def __init__(self,
                 display,
                 top_menu,
                 error_led,
                 top_button_gpio,
                 center_button_gpio,
                 bottom_button_gpio,
                 left_button_gpio,
                 right_button_gpio):

        self.display = display
        self.top_menu = top_menu
        self.error_led = error_led
        self.top_button = Button(top_button_gpio)
        self.center_button = Button(center_button_gpio)
        self.bottom_button = Button(bottom_button_gpio)
        self.left_button = Button(left_button_gpio)
        self.right_button = Button(right_button_gpio)

    def run(self):
        self.top_button.when_pressed = self.top_pressed
        self.center_button.when_pressed = self.center_pressed
        self.bottom_button.when_pressed = self.bottom_pressed
        self.left_button.when_pressed = self.left_pressed
        self.right_button.when_pressed = self.right_pressed

        # now wait for the user's actions
        pause()


    def top_pressed(self):
        print "TOP"

    def center_pressed(self):
        print "CENTER"

    def bottom_pressed(self):
        print "BOTTOOM"

    def left_pressed(self):
        print "LEFT"

    def right_pressed(self):
        print "RIGHT"
