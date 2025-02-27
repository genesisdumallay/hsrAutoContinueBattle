import pyautogui
import time


CHECK_INTERVAL = 5

time.sleep(10) # Make sure the OS loads everything before running

while True:
    time.sleep(CHECK_INTERVAL)

    try:
        button_location = pyautogui.locateCenterOnScreen("images/battle_button.png", confidence=0.8)
    except pyautogui.ImageNotFoundException:
        try:
            button_location = pyautogui.locateCenterOnScreen("images/battle_button_2.png", confidence=0.6)
        except pyautogui.ImageNotFoundException:
            print("Error finding button")

    if button_location:
        x, y = button_location
        pyautogui.moveTo(x, y, duration=0.4)
        pyautogui.click()
        print("Battle button found! Moving cursor and clicking...")

    else:
        print("Battle button not detected. Waiting...")
