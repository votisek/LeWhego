import mapping
import translator
import pyautogui as pag
import time
class Driver:
    def __init__(self, mapping, cycle):
        self.mapping = mapping
        self.cycle = cycle
    def get_mapping(self, key):
        return self.mapping[key]
    def do_stuff(self, brake, steer, transmission):
        

