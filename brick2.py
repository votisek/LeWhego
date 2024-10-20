from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from pybricks.parameters import Color

hub = EV3Brick()
"""
wheel = gyro = Port.S1
flap1 = motor = Port.S2
flap2 = motor = Port.S3
nitro = touch = Port.S4
"""
wheel = GyroSensor(Port.S1)
flap_l = TouchSensor(Port.S2)
flap_r = TouchSensor(Port.S3)
tlacitko = TouchSensor(Port.S4)

class Output:
    def __init__(self):
        pass
    
    def wheel(self): # Hodnota 0x1
        limited_angle = max(-90, min(90, wheel.angle()))
        hex_value = 0x100 + (limited_angle + 90)
        return hex(hex_value)

    def flaps(self): # Hodnota 0x2
        if flap_l.pressed() and flap_r.pressed():
            return 0x231
        elif flap_l.pressed():
            while flap_l.pressed():
                pass
            return 0x221
        elif flap_r.pressed():
            while flap_r.pressed():
                pass
            return 0x211
        else:
            return 0x200

    def tlacitko(self): # Hodnota 0x5
        if tlacitko.pressed():
            return 0x521
        else:
            return 0x520
