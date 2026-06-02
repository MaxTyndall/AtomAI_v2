from adafruit_servokit import ServoKit
from time import sleep
import random

kit = ServoKit(channels=16)

LEFT_X = 0
LEFT_Y = 1
LEFT_BLINK = 2
RIGHT_X = 3
RIGHT_Y = 4
RIGHT_BLINK = 5

OPEN_LEFT = 0
OPEN_RIGHT = 0
CLOSED_LEFT = 60
CLOSED_RIGHT = 60

CENTER_X = 90
CENTER_Y = 90

def safe_angle(angle):
    return max(0, min(180, angle))

def set_servo(channel, angle):
    kit.servo[channel].angle = safe_angle(angle)

def open_eyes():
    set_servo(LEFT_BLINK, OPEN_LEFT)
    set_servo(RIGHT_BLINK, OPEN_RIGHT)

def close_eyes():
    set_servo(LEFT_BLINK, CLOSED_LEFT)
    set_servo(RIGHT_BLINK, CLOSED_RIGHT)

def blink():
    close_eyes()
    sleep(0.18)
    open_eyes()

def blink_twice():
    blink()
    sleep(0.25)
    blink()

def wink_left():
    set_servo(LEFT_BLINK, CLOSED_LEFT)
    sleep(0.2)
    set_servo(LEFT_BLINK, OPEN_LEFT)

def wink_right():
    set_servo(RIGHT_BLINK, CLOSED_RIGHT)
    sleep(0.2)
    set_servo(RIGHT_BLINK, OPEN_RIGHT)

def center_eyes():
    set_servo(LEFT_X, CENTER_X)
    set_servo(RIGHT_X, CENTER_X)
    set_servo(LEFT_Y, CENTER_Y)
    set_servo(RIGHT_Y, CENTER_Y)
    open_eyes()

def look(x, y):
    set_servo(LEFT_X, x)
    set_servo(RIGHT_X, x)
    set_servo(LEFT_Y, y)
    set_servo(RIGHT_Y, y)

def look_random():
    x = random.randint(70, 110)
    y = random.randint(70, 110)
    look(x, y)

def idle_eyes():
    look_random()
    if random.random() < 0.35:
        blink()
