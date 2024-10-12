import pyautogui
import time

time.sleep(2)

x, y = pyautogui.position()
print(f"Координаты курсора: {x}, {y}")
