# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...
# Variabelen a en b (hoewel ze niet nodig zijn voor de vergelijking)
a = 4
b = -2

# Functie om y te berekenen
def bereken_y(x):
    y = (4 * x**3) - (2 * x**2) - 1
    return y

# Test de functie met verschillende waarden van x
for x in [1, 2, 0]:
    print(f"De uitkomst is: {bereken_y(x)}")

