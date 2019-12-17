cities = {
	'los angeles': {
		'state': 'california',
		'nickname': 'city of angels',
		},
	'santa monica': {
		'state': 'california',
		'nickname': 'sillicon beach',
	},
	'san francisco': {
		'state': 'california',
		'nickname': 'sillicon valley',
	},
}

for city, city_info in cities.items():
	print("The city of " + city.title() + " resides in " + 
		city_info['state'].title() + " and is nicknamed " +
		city_info['nickname'].title() + ".")