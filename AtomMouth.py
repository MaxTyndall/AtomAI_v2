# AtomMouth.py

from time import sleep
import board
import neopixel
from config import *

class Mouth:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(
            board.D18,
            NUM_PIXELS,
            brightness=BRIGHTNESS,
            auto_write=False
        )
        self.clear()

    def set_all(self, color):
        for i in range(NUM_PIXELS):
            self.pixels[i] = color
        self.pixels.show()

    def clear(self):
        self.set_all((0, 0, 0))

    def neutral(self):
        self.set_all((20, 20, 20))

    def happy(self):
        self.set_all((0, 255, 80))

    def listening(self):
        self.set_all((0, 100, 255))

    def thinking(self):
        for _ in range(3):
            self.set_all((120, 0, 255))
            sleep(0.2)
            self.clear()
            sleep(0.2)

    def talking(self):
        for _ in range(8):
            self.set_all((0, 255, 0))
            sleep(0.08)
            self.set_all((0, 60, 0))
            sleep(0.08)

    def error(self):
        self.set_all((255, 0, 0))
