# Create musicians
from Task1 import Musician, Band

anna_nowak = Musician("Anna", "Nowak", "guitar", "guitarist")
john_smith = Musician("John", "Smith", "drums", "drummer")
sara_jones = Musician("Sara", "Jones", "bass", "bassist")

# Create a band
print()
my_band = Band()

# Add musicians to the band
print()
my_band.add_musician(anna_nowak)
my_band.add_musician(john_smith)
my_band.add_musician(sara_jones)

# List all musicians in the band
print()
my_band.list_musicians()

# Play music
print()
my_band.play_music()

# Remove a musician from the band
print()
my_band.remove_musician("John Smith")

# List all musicians in the band after removal
print()
my_band.list_musicians()