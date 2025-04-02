# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak de gastenlijst
lijst = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print("Oorspronkelijke lijst:", lijst)

# Marie belt af
lijst.remove("Marie")
print("Na afmelding van Marie:", lijst)

# George wil naast Kees zitten
index_kees = lijst.index("Kees")
lijst.insert(index_kees + 1, "George")
print("Na toevoeging van George:", lijst)
