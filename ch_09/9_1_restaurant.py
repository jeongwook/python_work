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


# my_restaurant = Restaurant('Juan Pho Yu', 'pho')

# print(my_restaurant.name)
# print(my_restaurant.type)

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()