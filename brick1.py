from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.parameters import Color

"""
accelerator = color = Port.S1
clutch = touch = Port.S2
brake = color = Port.S3
transmission = motor = Port.A 
"""

hub = EV3Brick()
accelerator = ColorSensor()
clutch = TouchSensor()
brake = ColorSensor()
transmission = Motor()
transmissionin = Motor()