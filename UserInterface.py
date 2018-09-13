# a class that defines the user interface state machine for the MoonFinder application
# this class drives the LCD display and the menu system

from gpiozero import Button
from Menu.MenuElement import MenuElement
from PIL import ImageFont
from signal import pause

FONT_SIZE = 16
LEFT_MARGIN = 10
TOP_MARGIN = 10
TITLE_SPACING = 5
LINE_SPACING = 16
MENU_COLOR = (255,255,255)
TITLE_COLOR = (128, 128, 128)
SELECTED_COLOR = (255, 255, 0)

class UserInterface(object):

    def __init__(self,
                 title,
                 display,
                 top_menu,
                 error_led,
                 top_button_gpio,
                 center_button_gpio,
                 bottom_button_gpio,
                 left_button_gpio,
                 right_button_gpio):

        self.title = title
        self.display = display
        self.current_menu = top_menu
        self.selected = 0

        self.error_led = error_led

        self.top_button = Button(top_button_gpio)
        self.center_button = Button(center_button_gpio)
        self.bottom_button = Button(bottom_button_gpio)
        self.left_button = Button(left_button_gpio)
        self.right_button = Button(right_button_gpio)

        self.font = ImageFont.truetype("Fonts/Perfect DOS VGA 437 Win.ttf", FONT_SIZE)
        self.menu_color = MENU_COLOR
        self.title_color = TITLE_COLOR
        self.selected_color = SELECTED_COLOR

    def run(self):
        self.top_button.when_pressed = self.top_pressed
        self.center_button.when_pressed = self.center_pressed
        self.bottom_button.when_pressed = self.bottom_pressed
        self.left_button.when_pressed = self.left_pressed
        self.right_button.when_pressed = self.right_pressed

        # show the menu to the user
        self.show_menu()

        # now wait for the user's actions
        pause()

    def show_menu(self):
        # display is 128x128 - our working area is that less the margins and the title
        # each line of 16-pt font takes 10 pixels of space plus some separation
        # we can really only fit in 6 menu choices
        # TODO: scrolling a longer menu is not implemented

        self.display.clear((0, 0, 0))
        canvas = self.display.draw()
        x = LEFT_MARGIN
        y = TOP_MARGIN
        canvas.text((x, y), self.title, font=self.font, fill=self.title_color)
        y += TITLE_SPACING

        count = 0
        for item in self.current_menu.choices:
            y += LINE_SPACING
            color = self.selected_color if count == self.selected else self.menu_color
            canvas.text((x, y), "> " + item.title, font=self.font, fill=color)
            count += 1

        self.display.display()

    # navigate down the menu
    def top_pressed(self):
        self.selected = self.selected - 1
        if self.selected < 0:
            self.selected = 0
        self.show_menu()

    # activate the current menu item
    def center_pressed(self):
        if self.current_menu.type == MenuElement.MENU:
            self.current_menu = self.current_menu.choices[self.selected]
            self.selected = 0
            self.show_menu()
        # TODO: activate the action...

    # navigate up the menu
    def bottom_pressed(self):
        self.selected = self.selected + 1
        if self.selected >= len(self.current_menu.choices):
            self.selected = len(self.current_menu.choices) - 1
        self.show_menu()

    # back out a level on the menu
    def left_pressed(self):
        if self.current_menu.parent:
            self.current_menu = self.current_menu.parent
            self.selected = 0
            self.show_menu()

    # do what???
    def right_pressed(self):
        self.show_menu()
