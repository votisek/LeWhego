from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.parameters import Color

"""
accelerator = color = Port.S1
brake = color = Port.S3
"""

hub = EV3Brick()

accelerator = TouchSensor()
brake = TouchSensor()

class Output:
    def __init__(self):
        pass
    def accelerator(self): # Hodnota: 0x3
        if accelerator.pressed():
            return 0x311
        else:
            return 0x310
    
    def brake(self): # Hodnota: 0x4
        if brake.pressed():
            return 0x421
        else:
            return 0x420