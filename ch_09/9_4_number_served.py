class Restaurant():
	"""A restaurant model."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and type."""
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints restaurant information."""
		print("The restaurant's name is " + self.name.title())
		print("The cuisine type is " + self.type.title())

	def open_restaurant(self):
		"""Message indicating the restaurant is open."""
		print("The restaurant is now open!")

	def set_number_served(self, number):
		"""Set the number of customers that have been served."""
		self.number_served = number

	def increment_number_served(self, number):
		"""Increment the number of customers who've been served."""
		self.number_served += number

restaurant = Restaurant('Juan Pho Yu', 'pho')

print(str(restaurant.number_served))
restaurant.number_served = 4
print(str(restaurant.number_served))

restaurant.set_number_served(14)
print(str(restaurant.number_served))

restaurant.increment_number_served(10)
print(str(restaurant.number_served))


