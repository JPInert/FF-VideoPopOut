import sys
from pynput import mouse, keyboard
import pystray
from pystray import MenuItem as item
from PIL import Image
import subprocess
import os 

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle:
        if pressed:
            # Perform the key combination Ctrl+Shift+]
            keyboard.Controller().press(keyboard.Key.ctrl_l)
            keyboard.Controller().press(keyboard.Key.shift)
            keyboard.Controller().press(']')
            keyboard.Controller().release(']')
            keyboard.Controller().release(keyboard.Key.shift)
            keyboard.Controller().release(keyboard.Key.ctrl_l)

# Embed icon and enable relative paths
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Kill process on exit
def exit_action(icon, item):
    icon.stop()
    subprocess.call(["taskkill", "/f", "/im", "VideoPopOut_win.exe"])

# Create instances of the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)

# Start listening for mouse events
mouse_listener.start()

# Include icon image
icon_image = Image.open(resource_path("icon.ico"))

menu = (item('Exit', exit_action),)

# Create the system tray icon
icon = pystray.Icon("FF PopOut", icon_image, "FF PopOut", menu)
icon.run()

# Keep the script running
mouse_listener.join()