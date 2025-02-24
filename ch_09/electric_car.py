"""A set of classes that can be used to represent electric cars."""

from car import Car


class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size


	def describe_battery(self):
		"""Print a statement describing the batter size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")


	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can approximately " + str(range)
		message += " miles on a full charge."
		print(message)


	def upgrade_battery(self):
		"""Check battery size and upgrade to 85 if it isn't already"""
		if self.battery_size == 70:
			self.battery_size = 85


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank.")