# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(bestand_naam, tekst):
    with open(bestand_naam, "a") as bestand:  # 'a' betekent append, dus toevoegen aan het bestand
        bestand.write(tekst + "\n")  # Voeg tekst toe, met een nieuwe regel na de tekst

# Voorbeeld van het gebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

