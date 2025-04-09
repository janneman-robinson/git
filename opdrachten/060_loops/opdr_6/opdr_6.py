# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
pizzas.sort()

pizzas.append('yo-favorito')
pizzas.remove('olivio')

print(pizzas[:3])                        # Eerste 3 pizza's
print([pizzas[len(pizzas)//2]])         # Middelste pizza
print(pizzas[-3:])                      # Laatste 3 pizza's

