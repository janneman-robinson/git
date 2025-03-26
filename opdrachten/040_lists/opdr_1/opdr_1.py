# Opdracht 1 lists
# Naam student:
# Groep:

# Maak een lege lijst
personen = []

# Maak vier dictionaries met gegevens van personen
persoon1 = {"id": 0, "voornaam": "Emma", "achternaam": "Jansen"}
persoon2 = {"id": 1, "voornaam": "Liam", "achternaam": "de Vries"}
persoon3 = {"id": 2, "voornaam": "Sophie", "achternaam": "Bakker"}
persoon4 = {"id": 3, "voornaam": "Noah", "achternaam": "Visser"}

# Voeg de dictionaries toe aan de lijst met een list-methode
personen.extend([persoon1, persoon2, persoon3, persoon4])

# Print de volledige naam van de tweede persoon
print(personen[1]["voornaam"], personen[1]["achternaam"])
