import random

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2._platform.ev3 import INPUT_1, INPUT_3, INPUT_4
from api.wheel_movement import stop_both, move_back, turn_right, turn_left

leds = Leds()
TIME = 0.4

cs_left = ColorSensor(INPUT_1)
cs_middle = ColorSensor(INPUT_3)
cs_right = ColorSensor(INPUT_4)


def color_collision_protocol(color_sensor_tuple):
    leds.set_color("LEFT", "RED")
    leds.set_color("RIGHT", "RED")

    if color_sensor_tuple[0]:
        stop_both()
        move_back(15, TIME)
        turn_left(-30, TIME)
        turn_right(30, TIME)
    elif color_sensor_tuple[2]:
        stop_both()
        move_back(15, TIME)
        turn_right(-30, TIME)
        turn_left(30, TIME)
    elif color_sensor_tuple[1]:
        move_back(15, 2)
        if random.randint(1, 2) == 1:
            turn_left(-10, TIME)
            turn_right(10, TIME)
        else:
            turn_right(-10, TIME)
            turn_left(10, TIME)

    leds.set_color("LEFT", "GREEN")
    leds.set_color("RIGHT", "GREEN")


def detect_color():
    return cs_left.color, cs_middle.color, cs_right.color


def detect_line(border_color):
    return cs_left.color == border_color, cs_middle.color == border_color, cs_right.color == border_color