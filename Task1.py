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

    def add_musician(self, musician):
        self.musicians.append(musician)

    def remove_musician(self, name):
        for musician in self.musicians:
            if musician.first_name+ " " + musician.last_name == name:
                self.musicians.remove(musician)
                print(f"{musician.first_name} {musician.last_name} has been removed from the band.")
                return
        print(f"No musician with the name '{name}' found in the band.")

    def play_music(self):
        print("Band is playing:")
        for musician in self.musicians:
            musician.play()

    def list_musicians(self):
        print("  {:<15} {:<15} {:<15} {:<10}".format("First Name", "Last Name", "Instrument", "Role"))
        for musician in self.musicians:
            print("  {:<15} {:<15} {:<15} {:<10}".format(
                musician.first_name, musician.last_name, musician.instrument, musician.role))
