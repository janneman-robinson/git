# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


tekst = input("Geef de tekst die je wilt encrypten..\n")
versleuteld = ""

for char in tekst:
    if char.isalpha():
        basis = ord('A') if char.isupper() else ord('a')
        nieuw_char = chr((ord(char) - basis + 5) % 26 + basis)
        versleuteld += nieuw_char
    else:
        versleuteld += char

print(versleuteld)

