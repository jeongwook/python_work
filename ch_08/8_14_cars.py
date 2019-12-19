def make_car(manufacturer, model_name, **optional):
	"""Stores information about a car."""
	car = {}
	car['manufacturer'] = manufacturer
	car['model_name'] = model_name
	for key, value in optional.items():
		car[key] = value
	print(car)

car = make_car('subaru', 'outback', color='blue', tow_package=True)
