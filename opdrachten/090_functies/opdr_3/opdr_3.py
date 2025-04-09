# Opdracht 1 functies
# Naam student:
# Groep:


import math

# Functie voor het volume van een kubus
def kubus_vol(zijde):
    return zijde ** 3  # Volume van een kubus is zijde³

# Functie voor het volume van een bol
def bol_vol(radius):
    return (4/3) * math.pi * (radius ** 3)  # Volume van een bol is (4/3) * pi * r³

# Voorbeeld van het gebruik van de functies
volume_kubus = kubus_vol(5)
volume_bol = bol_vol(4)

# Print de resultaten
print(f"De inhoud van deze kubus is: {volume_kubus}")
print(f"De inhoud van deze bol is: {volume_bol}")
