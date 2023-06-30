from pynput import mouse, keyboard

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

# Create instances of the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)

# Start listening for mouse events
mouse_listener.start()

# Keep the script running
mouse_listener.join()