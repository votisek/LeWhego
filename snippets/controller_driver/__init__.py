import pybricks
import mapping
class Driver:
    def __init__(self, mapping):
        self.mapping = mapping
    def get_mapping(self, key):
        return self.mapping[key]
brick = Driver(mapping=mapping.mapping)
print(brick.get_mapping(0x01))
