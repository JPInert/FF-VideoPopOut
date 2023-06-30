from pynput import mouse, keyboard

remap_button = None  # Variable to store the remap button

def on_click(x, y, button, pressed):
    global remap_button

    if remap_button is None:
        if pressed:
            # Ask the user to press a mouse button to remap
            print("Press the desired mouse button to remap:")
            remap_button = button
    elif button == remap_button:
        if pressed:
            # Perform the key combination Ctrl+Shift+]
            keyboard.Controller().press(keyboard.Key.ctrl_l)
            keyboard.Controller().press(keyboard.Key.shift)
            keyboard.Controller().press(']')
            keyboard.Controller().release(']')
            keyboard.Controller().release(keyboard.Key.shift)
            keyboard.Controller().release(keyboard.Key.ctrl_l)

# Create an instance of the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)

# Start listening for mouse events
mouse_listener.start()

# Keep the script running
mouse_listener.join()
