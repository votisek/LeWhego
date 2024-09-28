import mapping
import pyautogui as pag
import time
class Driver:
    def __init__(self, mapping, cycle):
        self.mapping = mapping
        self.cycle = cycle
        self.runner = False
    def get_mapping(self, key):
        return self.mapping[key]
    def do_stuff(self, brake, steer, transmission):
        while self.runner: 
            pass