class Restaurant():
	"""A restaurant model."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and type."""
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		"""Prints restaurant information."""
		print("The restaurant's name is " + self.name.title())
		print("The cuisine type is " + self.type)

	def open_restaurant(self):
		"""Message indicating the restaurant is open."""
		print("The restaurant is now open!")


class IceCreamStand(Restaurant):
	"""A simple model of an ice cream stand."""

	def __init__(self, restaurant_name, cuisine_type, flavors):
		"""
		Initalize attributes of the parent class.
		Then initialize attributes specific to an ice cream stand
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors


	def describe_flavors(self):
		"""Message indicating what flavors are available."""
		print("The ice cream stand has the following flavors:")
		for flavor in self.flavors:
			print(flavor.title() )


ice_cream_stand = IceCreamStand('Snow Monster', 'dessert', ['chocolate', 'strawberry', 'vanilla'])
ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_flavors()