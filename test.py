import pyautogui

# Move the mouse to specific coordinates
pyautogui.moveTo(100, 100)

# Click at the current mouse position
pyautogui.click()

# Type some text
pyautogui.typewrite("Hello, world!")

# You can also capture the screen or take screenshots
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")
