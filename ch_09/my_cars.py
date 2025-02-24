# -- importing multiple classes from a module

# from car import Car, ElectricCar

# my_beetle = Car('volkswagen' ,'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = Car('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# -- importing an entire module

# import car

# my_beetle = car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# -- importing a module into a module
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
