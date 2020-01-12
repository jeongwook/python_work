import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
	"""Tests for class Employee"""
	def setUp(self):
		self.employee = Employee('Juan', 'Yu', 115000)

	def test_give_default_raise(self):
		"""Test default raise"""
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 120000)

	def test_give_custom_raise(self):
		"""Test custom raise"""
		self.employee.give_raise(35000)
		self.assertEqual(self.employee.annual_salary, 150000)

unittest.main()