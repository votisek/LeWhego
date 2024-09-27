import mapping
class Driver:
    def __init__(self, mapping):
        self.mapping = mapping
    def get_mapping(self, key):
        return self.mapping[key]