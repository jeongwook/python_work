class Users():
	"""User object."""

	def __init__(self, first_name, last_name, sex, age):
		"""Initialize user attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.sex = sex
		self.age = age

	def describe_user(self):
		"""Describe the user."""
		print(self.full_name.title() + " is " + str(self.age) + " and " + self.sex + ".") 

	def greet_user(self):
		"""Greet the user."""
		print("Hello " + self.full_name.title() + ", how are you today?")

me = Users('juan', 'yu', 'male', 30)
me.describe_user()
me.greet_user()

jason = Users('jason', 'doe', 'male', 36)
jason.describe_user()
jason.greet_user()

jin = Users('jin', 'doe', 'male', 30)
jin.describe_user()
jin.greet_user()
