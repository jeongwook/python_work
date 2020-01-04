"""A set of classes that represent admins."""
from users import Users

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