# AtomMouth.py

import board
import neopixel
import random
from time import sleep

from config import *

pixels = neopixel.NeoPixel(
    board.D18,
    NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False
)

class Mouth:

    def __init__(self):
        self.clear()

    def clear(self):
        pixels.fill((0, 0, 0))
        pixels.show()

    def set_color(self, color):
        pixels.fill(color)
        pixels.show()

    def thinking(self):

        for i in range(NUM_PIXELS):
            pixels.fill((0, 0, 0))
            pixels[i] = (0, 0, 255)
            pixels.show()
            sleep(0.05)

    def speak_level(self, level):

        pixels.fill((0, 0, 0))

        lit = max(1, min(NUM_PIXELS, level))

        center_left = NUM_PIXELS // 2 - 1
        center_right = NUM_PIXELS // 2

        for i in range(lit // 2):

            left = center_left - i
            right = center_right + i

            if 0 <= left < NUM_PIXELS:
                pixels[left] = (0, 255, 0)

            if 0 <= right < NUM_PIXELS:
                pixels[right] = (0, 255, 0)

        pixels.show()

    def fake_talking(self, seconds=3):

        import time

        end_time = time.time() + seconds

        while time.time() < end_time:

            level = random.randint(1, NUM_PIXELS)

            self.speak_level(level)

            sleep(0.08)

        self.clear()

    def happy(self):
        self.set_color((255, 255, 0))

    def sad(self):
        self.set_color((0, 0, 255))

    def angry(self):
        self.set_color((255, 0, 0))

    def neutral(self):
        self.set_color((0, 255, 0))
