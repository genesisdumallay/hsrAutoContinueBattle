import pyautogui
import time

CHECK_INTERVAL = 5

time.sleep(10) # Make sure the OS loads everything before running

while True:
    time.sleep(CHECK_INTERVAL)

    try:
        # Locate button on the screen
        button_location = pyautogui.locateCenterOnScreen("images/battle_button.png", confidence=0.8)

        if button_location:
            pyautogui.click(button_location)
            print("Battle button found")

    except pyautogui.ImageNotFoundException:
        print("Battle button not detected")
