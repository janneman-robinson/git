# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Bouw de volledige naam door voornaam, eventueel tussenvoegsel en achternaam samen te voegen
        volledige_naam = f"{persoon['voornaam']} {persoon['tussenvoegsel']} {persoon['achternaam']}".strip()
        # Druk de volledige naam af
        print(volledige_naam)

# Lijst met dictionaries
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Aanroepen van de functie
volledige_naam(namen)
