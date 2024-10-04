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
flap1 = motor = Port.A
flap2 = motor = Port.B
"""
wheel = GyroSensor(Port.S1)
flap_plus = TouchSensor(Port.A)
flap_minus = TouchSensor(Port.B)

class Output:
    def __init__(self):
        pass
    
    def wheel(self):        
        return int("0x2".join(hex(wheel.angle())))

    def flaps(self):
        if flap_minus.pressed() and flap_plus.pressed():
            while flap_minus.pressed() and flap_plus.pressed():
                pass
            return 0x131
        elif flap_minus.pressed():
            while flap_minus.pressed():
                pass
            return 0x121
        elif flap_plus.pressed():
            while flap_plus.pressed():
                pass
            return 0x111
        else:
            return 0x100
