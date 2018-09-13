# a class to represent an item on an LCD menu. What it knows about itself:
#
# - it's title (how it should be displayed in the menu)
# - whether is is a parent menu or an action leaf
# = what menu item is it's parent
# - if menu, what menu choices lie beneath it
# - if leaf, what action to take when it's selected

class MenuElement(object):
    MENU = 1
    LEAF = 2

    def __init__(self, title="", menu_type=LEAF, message=""):
        self.title = title
        self.type = menu_type
        self.message = message
        self.choices = []
        self.action = None
        self.parent = None

    def add_choice(self, choice):
        if self.type == MenuElement.MENU:
            self.choices.append(choice)
            choice.parent = self

    def set_action(self, action):
        if self.type == MenuElement.LEAF:
            self.action = action
