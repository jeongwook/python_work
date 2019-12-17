dictionary = {
	'juan': ['california', 'korea', 'japan'],
	'jason': ['houston', 'california', 'florida'],
	'dave': ['austin', 'san antonio', 'california']
}

for name, places in dictionary.items():
	print(name.title() + "'s favorite places are:")
	for place in places:
		print("\t" + place.title())