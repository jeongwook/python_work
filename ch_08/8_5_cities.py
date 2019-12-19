def describe_city(city, country='the USA'):
	"""Print simple sentence about city and country"""
	print(city.title() + " is in " + country.title() + ".")

describe_city('Los Angeles')
describe_city('Santa Monica')
describe_city('Paris', 'France')
