import pyautogui
import time

def wiggle_mouse():
    # Loop indefinitely
    while True:
        # Get the current position of the mouse
        x, y = pyautogui.position()
        
        # Move the mouse slightly to the right
        pyautogui.moveTo(x + 10, y)
        time.sleep(0.1)  # Short delay to make it visible
        
        # Move the mouse back to the original position
        pyautogui.moveTo(x - 10, y)
        time.sleep(4.9)  # Sleep for the remainder of the 5 seconds

        # Right-click the mouse at the current position
        pyautogui.click(button='right')
        
        # Sleep for the remainder of the 5 seconds
        time.sleep(4.8)

if __name__ == "__main__":
    wiggle_mouse()
