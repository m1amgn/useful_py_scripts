# Automate Desktop App

# pip install ahk
from ahk import AHK
from ahk.window import Window


auto = AHK()

# Do Mouse Actions
auto.mouse_move(100, 100)
auto.mouse_down(button='left')
auto.mouse_up(button='left')
auto.click()
auto.double_click()
auto.right_click()
auto.mouse_position()
auto.mouse_drag(100, 100, 200, 200)

# Do Keyboard Actions
auto.key_press('a')
auto.key_down('a')
auto.type('Hello World')

# Get Active Window
active = auto.active_window()
print(active)

# List of Windows 
windows = auto.windows()

# Open a Window
window = auto.run_script('notepad.exe')

# Give focus to window
window.focus()

# Kill or Terminate a Window
window.kill()#

 Maimize or Maximize a Window
window.maximize()
window.minimize()

# Search an image on the screen
cord = auto.image_search('image.png')
print(cord)
