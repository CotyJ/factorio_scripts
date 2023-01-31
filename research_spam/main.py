import mouse
import keyboard
import time


def click_spam(occurrences, wait):
    for num in range(occurrences):
        mouse.move(125, 560)
        time.sleep(wait)
        mouse.double_click(button='left')
        time.sleep(wait)
        mouse.move(465, 420)
        time.sleep(wait)
        keyboard.press('shift')
        time.sleep(wait)
        mouse.double_click(button='left')
        time.sleep(wait)
        keyboard.release('shift')
        time.sleep(wait)


click_spam(20, 0.01)

