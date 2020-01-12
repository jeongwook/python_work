def get_city_country(city, country, population=''):
	"""Generate a string in the form of City, Country"""
	city_country = city + ', ' + country
	city_country = city_country.title()
	if population:
		city_country += ' - population ' + str(population)
	return city_country