import controller_driver
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.parameters import Color
import brick1
import brick2
import threading

driver = controller_driver.Driver(controller_driver.mapping)

driver_thread = threading.Thread(target=driver.do_stuff())
console_thread = threading.Thread(target=driver.do_console())
driver_thread.daemon = True
driver_thread.start()

brick1 = brick1.Output()
brick2 = brick2.Output()

main = True
while main:
    driver.volant = hex(brick2.wheel())
    driver.brzda = brick1.brake()
    driver.plyn = brick1.accelerator()
    driver.padla = brick2.flaps()
    driver.tlacitko = brick2.tlacitko()
