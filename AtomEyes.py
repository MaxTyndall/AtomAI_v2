# AtomEyes.py
from adafruit_servokit import ServoKit
from time import sleep
import random
from config import *
kit = ServoKit(channels=16)
class Eyes:
    def __init__(self):
        self.center()
    def safe(self, value):
        return max(0, min(180, value))
    def set_angle(self, channel, angle):
        kit.servo[channel].angle = self.safe(angle)
    def center(self):
        self.set_angle(LEFT_X, CENTER_X)
        self.set_angle(RIGHT_X, CENTER_X)
        self.set_angle(LEFT_Y, CENTER_Y)
        self.set_angle(RIGHT_Y, CENTER_Y)
        self.open()
    def open(self):
        self.set_angle(LEFT_BLINK, LEFT_EYE_OPEN)
        self.set_angle(RIGHT_BLINK, RIGHT_EYE_OPEN)
    def close(self):
        self.set_angle(LEFT_BLINK, LEFT_EYE_CLOSED)
        self.set_angle(RIGHT_BLINK, RIGHT_EYE_CLOSED)
    def blink(self):
        self.close()
        sleep(BLINK_DELAY)
        self.open()
    def blink_twice(self):
        self.blink()
        sleep(0.25)
        self.blink()
    def wink_left(self):
        self.set_angle(LEFT_BLINK, EYE_CLOSED)
        sleep(0.2)
        self.set_angle(LEFT_BLINK, EYE_OPEN)
    def wink_right(self):
        self.set_angle(RIGHT_BLINK, EYE_CLOSED)
        sleep(0.2)
        self.set_angle(RIGHT_BLINK, EYE_OPEN)
    def look_left(self):
        self.set_angle(LEFT_X, LOOK_LEFT)
        self.set_angle(RIGHT_X, LOOK_LEFT)
    def look_right(self):
        self.set_angle(LEFT_X, LOOK_RIGHT)
        self.set_angle(RIGHT_X, LOOK_RIGHT)
    def look_up(self):
        self.set_angle(LEFT_Y, LOOK_UP)
        self.set_angle(RIGHT_Y, LOOK_UP)
    def look_down(self):
        self.set_angle(LEFT_Y, LOOK_DOWN)
        self.set_angle(RIGHT_Y, LOOK_DOWN)
    def random_look(self):
        x = random.randint(LOOK_LEFT, LOOK_RIGHT)
        y = random.randint(LOOK_UP, LOOK_DOWN)
        self.set_angle(LEFT_X, x)
        self.set_angle(RIGHT_X, x)
        self.set_angle(LEFT_Y, y)
        self.set_angle(RIGHT_Y, y)
    def thinking_animation(self):
        for _ in range(3):
            self.random_look()
            sleep(0.5)
        self.center()
    def idle(self):
        self.random_look()
        if random.random() < 0.3:
            self.blink()
