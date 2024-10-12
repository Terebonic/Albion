import pygetwindow as gw
import time
import pyautogui

precoordinations = [
    (1390, 410),
    (1275, 430),
    (560, 515),
    (1505, 335),
    (1205, 310),
]
coordinates = [
    (1275, 430),
    (830, 630),
    (1140, 730),
]


def prescneshotpositions():
    screenshotxy = [
        (1390, 410),
    ]
    for x, y in screenshotxy:
        pyautogui.click(x, y)
    screenshot = pyautogui.screenshot(region=(1230, 420, 90, 25))
    screenshot.save("reference_image.png")


def seller():
    game_window_title = "Albion Online Client"
    game_window = gw.getWindowsWithTitle(game_window_title)

    if game_window:
        game_window[0].activate()
        prescneshotpositions()

        for x, y in precoordinations:
            pyautogui.click(x, y)
            time.sleep(0.03)

        while True:
            try:
                location = pyautogui.locateOnScreen(
                    'reference_image.png', confidence=0.8)

                for x, y in coordinates:
                    pyautogui.click(x, y)
                    time.sleep(0.03)

            except pyautogui.ImageNotFoundException:
                break

    else:
        print(f"Окно игры '{game_window_title}' не найдено.")


if __name__ == "__main__":
    seller()
