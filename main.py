import controller_driver
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.parameters import Color
from brick1 import *
from brick2 import *
import threading

driver = controller_driver.Driver(controller_driver.mapping)
driver_thread = threading.Thread(target=driver.do_stuff())
driver_thread.daemon = True
while True:
    console = input()
    driver.get_mapping(console)



