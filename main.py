import snippets
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

driver = snippets.controller_driver.Driver(snippets.controller_driver.mapping)
translator = snippets.translator.Translator(snippets.translator.mapping)
driver_thread = threading.Thread(target=driver.do_stuff())



