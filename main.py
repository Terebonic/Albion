import pyautogui
import time
import pygetwindow as gw
import argparse


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


def seller(itemscount):
    game_window_title = "Albion Online Client"
    game_window = gw.getWindowsWithTitle(game_window_title)

    if game_window:
        game_window[0].activate()
        print(f"Окно игры '{game_window_title}' активировано.")

        for x, y in precoordinations:
            pyautogui.click(x, y)
            time.sleep(0.03)

        for i in range(0, itemscount):
            for x, y in coordinates:
                pyautogui.click(x, y)
                time.sleep(0.03)
    else:
        print(f"Окно игры '{game_window_title}' не найдено.")


def cmdparser():
    parser = argparse.ArgumentParser(description="Albion online fast seller")

    parser.add_argument(
        'itemscount', type=int, help='Count of all your items in inventory')

    args = parser.parse_args()

    seller(args.itemscount)


if __name__ == "__main__":
    cmdparser()
