from random import randint

"""A class used that can be used to represent a dice."""

class Die():
	"""A simple attempt to model a die."""

	def __init__(self, sides=6):
		"""Initialize the dice's attributes"""
		self.sides = sides


	def roll_die(self):
		"""Roll die between 1 and the number of sides."""
		return randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)