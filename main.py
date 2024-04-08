class Musician:
    def __init__(self, first_name, last_name, instrument, role):
        self.first_name = first_name
        self.last_name = last_name
        self.instrument = instrument
        self.role = role

    def play(self):
        print(f"{self.first_name} {self.last_name} plays {self.instrument}")

class Band:
    def __init__(self):
        self.musicians = []
