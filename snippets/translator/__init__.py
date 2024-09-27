from pybricks.parameters import Color
class Translator:
    def __init__(self, mapping):
        self.mapping = mapping
    def brake_power(self, val_in):
        val_out = "brake0"
        match val_in:
            case Color.BLACK:
                val_out = "brake0"
            case Color.BROWN:
                val_out = "brake1"
            case Color.BLUE:
                val_out = "brake2"
            case Color.GREEN:
                val_out = "brake3"
            case Color.RED:
                val_out = "brake4"
            case _:
                val_out = "brake0"
        return self.mapping[val_out]
    def steer_angle(self, val_in):
        if val_in > 135:
            val_in = 135
        if val_in < -135:
            val_in = -135
        return val_in
    

