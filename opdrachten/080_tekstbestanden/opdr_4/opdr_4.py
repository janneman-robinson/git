# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

feestganger = {}

# Vraag de feestganger om antwoorden
feestganger['voornaam'] = input(vragen[0] + "\n")
feestganger['achternaam'] = input(vragen[1] + "\n")
feestganger['drank'] = input(vragen[2] + "\n")
feestganger['eten'] = input(vragen[3] + "\n")

# Toon bedankt bericht
print("Bedankt voor het invullen!")
print("See you at the party.")

# Sla de gegevens op in een tekstbestand
with open("feestganger_info.txt", "w") as bestand:
    for key, value in feestganger.items():
        bestand.write(f"{key}: {value}\n")
