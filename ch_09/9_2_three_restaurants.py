class Restaurant():
	"""A restaurant model."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and type."""
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		"""Prints restaurant information."""
		print("The restaurant's name is " + self.name.title())
		print("The cuisine type is " + self.type.title())

	def open_restaurant(self):
		"""Message indicating the restaurant is open."""
		print("The restaurant is now open!")


my_restaurant = Restaurant('Juan Pho Yu', 'pho')
jasons_restaurant = Restaurant("Poke Poke", 'poke')
jins_restaurant = Restaurant("Jin Gukbap", 'gukbap')
my_restaurant.describe_restaurant()
jasons_restaurant.describe_restaurant()
jins_restaurant.describe_restaurant()
