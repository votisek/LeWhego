import pyautogui
import time
import brick1
import threading
import json
import vgamepad as vgp



gp = vgp.VX360Gamepad()

class Driver:
    def __init__(self):
        self.mapping = None
        self.runner = False
        self.volant = None
        self.brzda = None
        self.plyn = None
        self.padla = None
        self.tlacitko = None
        self.driftwav = "driftwav.json"

    def change_mapping(self, mapping):
        with open(mapping, "r") as file:
            self.mapping  = json.load(file)  

    def get_mapping(self, key, code):
        # Získá seznam hodnot pod klíčem (např. "brake", "flaps")
        values_list = self.mapping.get(key, [])
        
        # Projde seznam a hledá, jestli je "code" ve slovníku
        for item in values_list:
            if code in item:
                return item[code]
        return None

    def do_stuff(self):
        while self.runner:
                gp.left_joystick(self.get_mapping("volant", str(self.volant)), 0)
                gp.left_trigger(self.get_mapping("brzda", str(self.brzda)))
                gp.right_trigger(self.get_mapping("plyn", str(self.plyn)))
                match self.get_mapping("padla", padla):
                    case "slow":
                        gp.press_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                    case "jump":
                        gp.press_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    case "slow+jump":
                        gp.press_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                        gp.press_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    case "none":
                        gp.release_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_A)
                        gp.release_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                    case _:
                        print("wtf neco se rozbilo na padlech v driver")
                match self.get_mapping("tlacitko", self.tlacitko):
                    case "none":
                        gp.release_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_START)
                    case "start":
                        gp.press_button(vgp.XUSB_BUTTON.XUSB_GAMEPAD_START)
                    case _:
                        print("wtf neco se podelalo na tlacitku v driveru")
                gp.update()
    def do_console(self, console): 
