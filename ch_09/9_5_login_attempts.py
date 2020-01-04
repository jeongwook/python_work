class Users():
	"""User object."""

	def __init__(self, first_name, last_name, sex, age):
		"""Initialize user attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = first_name + " " + last_name
		self.sex = sex
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""Describe the user."""
		print(self.full_name.title() + " is " + str(self.age) + " and " + self.sex + ".") 

	def greet_user(self):
		"""Greet the user."""
		print("Hello " + self.full_name.title() + ", how are you today?")

	def increment_login_attempts(self):
		"""Increments the login attempt by 1."""
		self.login_attempts += 1

	def reset_login_attemtps(self):
		"""Resets the value of login attemtps to 0."""
		self.login_attempts = 0


me = Users('juan', 'yu', 'male', 30)
me.increment_login_attempts()
print(str(me.login_attempts))
me.reset_login_attemtps()
print(str(me.login_attempts))

