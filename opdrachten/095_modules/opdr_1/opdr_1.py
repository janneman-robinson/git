# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
import csv

def lees_csv(bestandsnaam):
    with open(bestandsnaam, mode='r') as bestand:
        csv_reader = csv.reader(bestand)
        for rij in csv_reader:
            print(rij)
