import pyautogui
import time


class Gundrop:
    WIDTH, HEIGHT = pyautogui.size()

    @classmethod
    def drop_gun(cls, x, y):
        pyautogui.press('b')
        time.sleep(0.5)
        pyautogui.leftClick(x, y)
        time.sleep(0.5)
        pyautogui.press('`')
        pyautogui.press('Esc')

    @classmethod
    def drop_phantom(cls):
        cls.drop_gun(cls.WIDTH / 2, cls.HEIGHT / 2)

    @classmethod
    def drop_guardian(cls):
        cls.drop_gun(cls.WIDTH / 2, cls.HEIGHT / 3)

    @classmethod
    def drop_vandal(cls):
        cls.drop_gun(cls.WIDTH / 2, cls.HEIGHT / 1.6)


if __name__ == '__main__':
    pyautogui.hotkey('Alt', 'Tab')
    time.sleep(1)
    Gundrop.drop_vandal()
