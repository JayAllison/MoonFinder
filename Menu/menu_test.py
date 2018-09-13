from MenuElement import MenuElement
from menu_layout import top_menu

spacer = "    "


def dump_choices(menu, level=0):
    if len(menu.choices) == 0:
        print spacer*level + "(none)"
    for item in menu.choices:
        print spacer*level + "[ ] " + item.title,
        if item.type == MenuElement.MENU:
            print "->"
            dump_choices(item, level+1)
        else:
            print " "


dump_choices(top_menu)
