"""A class that is used to represent a restaurant."""

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