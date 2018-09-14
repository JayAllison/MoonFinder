# define the menu structure, from the bottom to the top
from MenuElement import MenuElement

# - Navigate
#   - <auto-filled>
# - Information
#   - <TBD>
# - Diagnostics
#   - Compass
#   - GPS
#   - Screen

test11 = MenuElement("Deep Menu 11", MenuElement.LEAF)
test1 = MenuElement("Deep Menu 1", MenuElement.MENU)
test1.add_choice(test11)

test21 = MenuElement("Deep Menu 21", MenuElement.LEAF)
test22 = MenuElement("Deep Menu 22", MenuElement.LEAF)
test2 = MenuElement("Deep Menu 2", MenuElement.MENU)
test2.add_choice(test21)
test2.add_choice(test22)

test31 = MenuElement("Deep Menu 31", MenuElement.LEAF)
test32 = MenuElement("Deep Menu 32", MenuElement.LEAF)
test33 = MenuElement("Deep Menu 33", MenuElement.LEAF)
test3 = MenuElement("Deep Menu 3", MenuElement.MENU)
test3.add_choice(test31)
test3.add_choice(test32)
test3.add_choice(test33)

test41 = MenuElement("Deep Menu 41", MenuElement.LEAF)
test42 = MenuElement("Deep Menu 42", MenuElement.LEAF)
test43 = MenuElement("Deep Menu 43", MenuElement.LEAF)
test44 = MenuElement("Deep Menu 44", MenuElement.LEAF)
test4 = MenuElement("Deep Menu 4", MenuElement.MENU)
test4.add_choice(test41)
test4.add_choice(test42)
test4.add_choice(test43)
test4.add_choice(test44)

test51 = MenuElement("Deep Menu 51", MenuElement.LEAF)
test52 = MenuElement("Deep Menu 52", MenuElement.LEAF)
test53 = MenuElement("Deep Menu 53", MenuElement.LEAF)
test54 = MenuElement("Deep Menu 54", MenuElement.LEAF)
test55 = MenuElement("Deep Menu 55", MenuElement.LEAF)
test5 = MenuElement("Deep Menu 5", MenuElement.MENU)
test5.add_choice(test51)
test5.add_choice(test52)
test5.add_choice(test53)
test5.add_choice(test54)
test5.add_choice(test55)

test61 = MenuElement("Deep Menu 61", MenuElement.LEAF)
test62 = MenuElement("Deep Menu 62", MenuElement.LEAF)
test63 = MenuElement("Deep Menu 63", MenuElement.LEAF)
test64 = MenuElement("Deep Menu 64", MenuElement.LEAF)
test65 = MenuElement("Deep Menu 65", MenuElement.LEAF)
test66 = MenuElement("Deep Menu 66", MenuElement.LEAF)
test6 = MenuElement("Deep Menu 6", MenuElement.MENU)
test6.add_choice(test61)
test6.add_choice(test62)
test6.add_choice(test63)
test6.add_choice(test64)
test6.add_choice(test65)
test6.add_choice(test66)

test0 = MenuElement("Deep Menu", MenuElement.MENU)
test0.add_choice(test1)
test0.add_choice(test2)
test0.add_choice(test3)
test0.add_choice(test4)
test0.add_choice(test5)
test0.add_choice(test6)

navigate = MenuElement("Navigate", MenuElement.MENU)

information = MenuElement("Information", MenuElement.LEAF, "Gathering Information...")
information.set_action(None)

compass_diagnostics = MenuElement("Compass", MenuElement.LEAF, "Testing Compass...")
gps_diagnostics = MenuElement("GPS", MenuElement.LEAF, "Testing GPS...")
screen_diagnostics = MenuElement("Screen", MenuElement.LEAF, "Testing Screen...")

diagnostics = MenuElement("Diagnostics", MenuElement.MENU)
diagnostics.add_choice(compass_diagnostics)
diagnostics.add_choice(gps_diagnostics)
diagnostics.add_choice(screen_diagnostics)

top_menu = MenuElement("MENU", MenuElement.MENU)
top_menu.add_choice(navigate)
top_menu.add_choice(information)
top_menu.add_choice(diagnostics)
top_menu.add_choice(test0)