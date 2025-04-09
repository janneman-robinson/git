# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering?\n")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")

with open("enquete_resultaten.txt", "w") as bestand:
    bestand.write(f"Regering: {vraag1}\n")
    bestand.write(f"Python-lessen: {vraag2}\n")
    bestand.write(f"Mooiste stad: {vraag3}\n")
