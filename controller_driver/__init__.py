import mapping
import pyautogui
import time
import brick1
import threading
class Driver:
    def __init__(self, mapping, cycle):
        self.mapping = mapping
        self.cycle = cycle
        self.runner = False
    def get_mapping(self, key):
        return self.mapping[key]
    def do_stuff(self, brake, acceleration, steer, transmission):
        while self.runner: 
            