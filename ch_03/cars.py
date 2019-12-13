cars = ['bmw', 'audi', 'toyota', 'subaru']
# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. 
# sort alphabetically
cars.sort()
print(cars)

# sort reverse alphabetically
cars.sort(reverse=True)
print(cars)

# sort temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the orginal list again:")
print(cars)

# reverse order
print("\n-- Reverse Order --")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# length
print(len(cars))