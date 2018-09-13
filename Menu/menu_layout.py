# build the menu structure, from the bottom to the top
from MenuElement import MenuElement

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
