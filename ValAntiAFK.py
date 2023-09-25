import time
import pyautogui
import sys
from pynput import keyboard
from gundopper import Gundrop


class Main:
    stop = False
    keylistner = None

    @classmethod
    def kuit(cls, key):
        if key == keyboard.Key.ctrl_l:
            print('[+] stopping...')
            cls.stop = True
            cls.keylistner.stop()
            sys.exit(0)

    @classmethod
    def start_keylistening(cls):
        cls.keylistner = keyboard.Listener(on_press=lambda x: print(x), on_release=cls.kuit)
        cls.keylistner.start()

    @classmethod
    def start(cls):
        cls.start_keylistening()
        print('[+] Program Started.')
        while True:
            if cls.stop:
                break
            Gundrop.drop_vandal()
            time.sleep(28)

        print('[+] Program Stopped.')


if __name__ == '__main__':
    pyautogui.hotkey('Alt', 'Tab')
    time.sleep(5)
    Main.start()
