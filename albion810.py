import pyautogui
import time
import pygetwindow as gw


precoordinations = [
    (1357, 428),
    (1240, 442),
    (1478, 339),
    (834, 515),
    (1190, 322)
]
coordinates = [
    (1245, 440),
    (835, 630),
    (1140, 720),
]


def prescneshotpositions():
    screenshotxy = [
        (1357, 428),
    ]
    for x, y in screenshotxy:
        pyautogui.click(x, y)
    screenshot = pyautogui.screenshot(region=(1210, 430, 90, 25))
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
