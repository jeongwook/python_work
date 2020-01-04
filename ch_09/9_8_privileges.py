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


class Privileges():
	"""A simple model of privileges."""

	def __init__(self, privileges):
		"""Initialize the privilege's attributes."""
		self.privileges = privileges


	def show_privileges(self):
		"""Print out admin's privileges"""
		print("The admin user has the following privileges:")
		for priv in self.privileges:
			print(" - " + priv)


class Admin(Users):
	"""A simple model of an admin user."""

	def __init__(self, first_name, last_name, sex, age, privileges):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an admin.
		"""
		super().__init__(first_name, last_name, sex, age)
		self.privileges = Privileges(privileges)


me = Admin('juan', 'yu', 'male', 30, ['can add post', 'can delete post', 'can ban user'])
me.describe_user()
me.greet_user()
me.privileges.show_privileges()
