# Simple Keylogger

This is a lightweight keylogger built using Python and the pynput library. The script logs all keyboard input and saves it to a file once the user exits the program by pressing the ESC key. This project can be used for educational purposes, such as understanding how key logging works.

# Features:

1)Logs every key press, including alphanumeric and special keys.

2)Saves the logged keys to a text file (key_log.txt).

3)Stops the logging process when the ESC key is pressed.

4)Written in Python with simple and readable code for beginners.

# Code Overview

1)on_press: Handles the logging of key presses. It appends alphanumeric keys directly, while special keys (e.g., Shift, Ctrl) are appended in a readable format.

2)on_release: Listens for the ESC key to trigger saving the log and stopping the listener.

3)save_log: Saves all captured key strokes to the file key_log.txt.

4)start_keylogger: Starts the keyboard listener and continues running until ESC is pressed.

# Important Note

This keylogger is intended for educational purposes only. Make sure you have appropriate permissions if you use this on any machine or network other than your own. Unauthorized use of keyloggers may violate privacy laws and can have legal consequences.

# Disclaimer

This tool should only be used in environments where you have explicit permission to monitor keyboard activity. Unauthorized monitoring of personal or corporate systems may be illegal.
