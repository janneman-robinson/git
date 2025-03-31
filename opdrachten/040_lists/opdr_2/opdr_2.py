# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
}

rivieren = list(rivier_info.keys())

# Print de naam van de 1e rivier en het 2e land waar deze doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")
# hier print rivier 0, dus De Rijn, en vakje 2, dus duitsland, en ze hebben een hoofdletter (door de .capatalize)

# Print de naam van de 2e rivier en het 1e land waar deze doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")
# hier print rivier 1, dus De Maas, en vakje 1, dus nederland, en ze hebben een hoofdletter (door de .capatalize)