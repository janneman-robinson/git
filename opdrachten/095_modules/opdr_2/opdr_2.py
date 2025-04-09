# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

from my_modules import csv

# Voorbeeldlijst van personen
personen = [
    {"voornaam": "Jan", "tussenvoegsel": "Van Der", "achternaam": "Vliet"},
    {"voornaam": "Jan", "tussenvoegsel": "Jaap", "achternaam": "Siewers"},
    {"voornaam": "Pieter", "tussenvoegsel": "de", "achternaam": "Boer"},
    {"voornaam": "Piet", "tussenvoegsel": "", "achternaam": "Kramer"},
    {"voornaam": "Pie", "tussenvoegsel": "", "achternaam": "Wijnands"}
]

# Functie om te filteren op basis van het begin van een veld
def filter(persoon_lijst, filterveld, filter):
    for persoon in persoon_lijst:
        if persoon[filterveld].startswith(filter):
            print(f"{persoon['voornaam']} {persoon['tussenvoegsel']} {persoon['achternaam']}")

# Gebruik de filterfunctie om te zoeken op basis van de voornaam
print("Filter op voornaam met 'ja':")
filter(personen, "voornaam", "Ja")

print("\nFilter op voornaam met 'Pie':")
filter(personen, "voornaam", "Pie")
