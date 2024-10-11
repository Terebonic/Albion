import pyautogui
import time

print("Переместите курсор в нужное место. У вас есть 2 секунды...")
time.sleep(2)


x, y = pyautogui.position()
print(f"Координаты курсора: {x}, {y}")
