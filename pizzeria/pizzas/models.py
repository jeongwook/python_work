from django.db import models

# Create your models here.

class Pizza(models.Model):
	"""A pizza."""
	name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Topping(models.Model):
	pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		"""Return a string representation of the model."""
		return self.name