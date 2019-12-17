favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people_to_take_poll = ['juan', 'jason', 'dave', 'jen', 'phil']

for person in people_to_take_poll:
	if person in favorite_languages.keys():
		print("Thank you " + person.title() + " for responding.")
	else: 
		print(person.title() + ", please come take the poll.")

print("\nList in dictionary")
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

