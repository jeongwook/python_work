import unittest
from city_functions import get_city_country

class CityCountriesTestCase(unittest.TestCase):
	"""Tests for city_functions.py."""

	def test_city_country(self):
		"""Do city, country such as 'Santiago, Chile' work?"""
		formatted_city_country = get_city_country('santiago', 'chile')
		self.assertEqual(formatted_city_country, 'Santiago, Chile')

	def test_city_country_population(self):
		"""
		Do city, country - population such as 'Santiago, Chile - 
		population 5000000' work?
		"""
		formatted_city_country = get_city_country('santiago', 'chile', 5000000)
		self.assertEqual(formatted_city_country, 'Santiago, Chile - population 5000000')
unittest.main() 