magicians = ['jason', 'dave', 'jin', 'josh', 'rodney']

def show_magicians(magicians):
	"""Show a list of magicians."""
	for magician in magicians:
		print(magician)

def make_great(magicians):
	"""Modify and add "the Great" to each magician."""
	# Build a new list to hold the great musicians.
	great_magicians = []

    # Make each magician great, and add it to great_magicians.
	while magicians:
		magician = magicians.pop()
		great_magician = magician.title() + ' the Great'
		great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
	for great_magician in great_magicians:
		magicians.append(great_magician)

	return great_magicians

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)