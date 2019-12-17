pets = []

emma = {
	'animal': 'dog',
	'owner': 'juan',
}
pets.append(emma)

loki = {
	'animal': 'dog',
	'owner': 'juan',
}
pets.append(loki)

kitty = {
	'animal': 'cat',
	'owner': 'kevin',
}
pets.append(kitty)

for pet in pets:
	print(pet['owner'].title() + " owns a " + pet['animal'] + ".")

