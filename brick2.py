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
clacson = color = Port.S2
"""
wheel = GyroSensor(Port.S1)
flap1 = TouchSensor(Port.A)
flap2 = TouchSensor(Port.B)
clacson = ColorSensor(Port.S2)

class Translate:
    def __init__(self):
        pass
    
    def wheel_out(self):
        wheel_angle = wheel.angle()
        if -135 <= wheel_angle < -130:
            wheel_out = -135
        elif -130 <= wheel_angle < -125:
            wheel_out = -130
        elif -125 <= wheel_angle < -120:
            wheel_out = -125
        elif -120 <= wheel_angle < -115:
            wheel_out = -120
        elif -115 <= wheel_angle < -110:
            wheel_out = -115
        elif -110 <= wheel_angle < -105:
            wheel_out = -110
        elif -105 <= wheel_angle < -100:
            wheel_out = -105
        elif -100 <= wheel_angle < -95:
            wheel_out = -100
        elif -95 <= wheel_angle < -90:
            wheel_out = -95
        elif -90 <= wheel_angle < -85:
            wheel_out = -90
        elif -85 <= wheel_angle < -80:
            wheel_out = -85
        elif -80 <= wheel_angle < -75:
            wheel_out = -80
        elif -75 <= wheel_angle < -70:
            wheel_out = -75
        elif -70 <= wheel_angle < -65:
            wheel_out = -70
        elif -65 <= wheel_angle < -60:
            wheel_out = -65
        elif -60 <= wheel_angle < -55:
            wheel_out = -60
        elif -55 <= wheel_angle < -50:
            wheel_out = -55
        elif -50 <= wheel_angle < -45:
            wheel_out = -50
        elif -45 <= wheel_angle < -40:
            wheel_out = -45
        elif -40 <= wheel_angle < -35:
            wheel_out = -40
        elif -35 <= wheel_angle < -30:
            wheel_out = -35
        elif -30 <= wheel_angle < -25:
            wheel_out = -30
        elif -25 <= wheel_angle < -20:
            wheel_out = -25
        elif -20 <= wheel_angle < -15:
            wheel_out = -20
        elif -15 <= wheel_angle < -10:
            wheel_out = -15
        elif -10 <= wheel_angle < -5:
            wheel_out = -10
        elif -5 <= wheel_angle < 0:
            wheel_out = -5
        elif 0 <= wheel_angle < 5:
            wheel_out = 0
        elif 5 <= wheel_angle < 10:
            wheel_out = 5
        elif 10 <= wheel_angle < 15:
            wheel_out = 10
        elif 15 <= wheel_angle < 20:
            wheel_out = 15
        elif 20 <= wheel_angle < 25:
            wheel_out = 20
        elif 25 <= wheel_angle < 30:
            wheel_out = 25
        elif 30 <= wheel_angle < 35:
            wheel_out = 30
        elif 35 <= wheel_angle < 40:
            wheel_out = 35
        elif 40 <= wheel_angle < 45:
            wheel_out = 40
        elif 45 <= wheel_angle < 50:
            wheel_out = 45
        elif 50 <= wheel_angle < 55:
            wheel_out = 50
        elif 55 <= wheel_angle < 60:
            wheel_out = 55
        elif 60 <= wheel_angle < 65:
            wheel_out = 60
        elif 65 <= wheel_angle < 70:
            wheel_out = 65
        elif 70 <= wheel_angle < 75:
            wheel_out = 70
        elif 75 <= wheel_angle < 80:
            wheel_out = 75
        elif 80 <= wheel_angle < 85:
            wheel_out = 80
        elif 85 <= wheel_angle < 90:
            wheel_out = 85
        elif 90 <= wheel_angle < 95:
            wheel_out = 90
        elif 95 <= wheel_angle < 100:
            wheel_out = 95
        elif 100 <= wheel_angle < 105:
            wheel_out = 100
        elif 105 <= wheel_angle < 110:
            wheel_out = 105
        elif 110 <= wheel_angle < 115:
            wheel_out = 110
        elif 115 <= wheel_angle < 120:
            wheel_out = 115
        elif 120 <= wheel_angle < 125:
            wheel_out = 120
        elif 125 <= wheel_angle < 130:
            wheel_out = 125
        elif 130 <= wheel_angle < 135:
            wheel_out = 130
        elif 135 <= wheel_angle:
            wheel_out = 135

        return wheel_out

    def clacson_out(self):
        if clacson.color() == None:
            return "clacson_false"
        else:
            return "clacson_true"
    
    def flap1_out(self):
        flap1_press = flap1.pressed()
        if flap1_press:
            return "flap1_true"
        else: 
            return "flap1_false"
    
    def flap2_out(self):
        flap2_press = flap2.pressed()
        if flap2_press:
            return "flap2_true"
        else:
            return "flap2_false"
