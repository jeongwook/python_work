people = []

personal_information = {
	'first_name': 'Jason',
	'last_name': 'Park',
	'age': 35,
	'city': 'Houston',
}
people.append(personal_information)


personal_information = {
	'first_name': 'Dave',
	'last_name': 'Lee',
	'age': 27,
	'city': 'Austin',
}
people.append(personal_information)

personal_information = {
	'first_name': 'Josh',WWW
	'last_name': 'Bae',
	'age': 27,
	'city': 'Dallas',
}
people.append(personal_information)

for person in people:
	print(person['first_name'].title() + " " + 
		person['last_name'].title() + " is " + str(person['age']) + 
		" and lives in " + person['city'].title() + ".")