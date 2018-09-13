from gpiozero import Button
from PIL import ImageFont
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
        self.current_menu = top_menu

        self.error_led = error_led

        self.top_button = Button(top_button_gpio)
        self.center_button = Button(center_button_gpio)
        self.bottom_button = Button(bottom_button_gpio)
        self.left_button = Button(left_button_gpio)
        self.right_button = Button(right_button_gpio)

        self.font = ImageFont.truetype("Fonts/Perfect DOS VGA 437 Win.ttf", 16)
        self.menu_color = (255, 255, 255)

    def run(self):
        self.top_button.when_pressed = self.top_pressed
        self.center_button.when_pressed = self.center_pressed
        self.bottom_button.when_pressed = self.bottom_pressed
        self.left_button.when_pressed = self.left_pressed
        self.right_button.when_pressed = self.right_pressed

        # show the menu to the user
        self.show_menu(self.current_menu)

        # now wait for the user's actions
        pause()

    def show_menu(self, menu):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), menu.title, font=self.font, fill=self.menu_color)
        self.display.display()

    def top_pressed(self):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), "TOP", font=self.font, fill=self.menu_color)
        self.display.display()

    def center_pressed(self):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), "CENTER", font=self.font, fill=self.menu_color)
        self.display.display()

    def bottom_pressed(self):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), "BOTTOM", font=self.font, fill=self.menu_color)
        self.display.display()

    def left_pressed(self):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), "LEFT", font=self.font, fill=self.menu_color)
        self.display.display()

    def right_pressed(self):
        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        canvas.text((10, 10), "RIGHT", font=self.font, fill=self.menu_color)
        self.display.display()
