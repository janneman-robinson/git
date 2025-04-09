# Opdracht 1 functies
# Naam student:
# Groep:


def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344  # Omrekeningsfactor van kilometers naar miles

def miles_naar_kilometers(miles):
    return miles * 1.609344  # Omrekeningsfactor van miles naar kilometers

# Voorbeeld van het gebruik van de functies
kilometers = 1223
miles = 867

# Bereken miles van kilometers en kilometers van miles
miles_result = kilometers_naar_miles(kilometers)
km_result = miles_naar_kilometers(miles)

# Print de resultaten
print(f"{kilometers} kilometers = {miles_result} miles")
print(f"{miles} miles = {km_result} kilometers")
