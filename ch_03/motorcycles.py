motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modify
print("\n-- modify --")
motorcycles[0] = 'ducati'
print(motorcycles)

# append
print("\n-- append --")
motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki')
print(motorcycles)

print("\n-- insert --")
# insert
motorcycles.insert(0, 'ducati')
print(motorcycles)

# remove with del
print("\n-- remove with del --")
del motorcycles[0]
print(motorcycles)

# remove with pop
print("\n-- remove with pop --")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# popping from anywhere on the list
print("\n-- popping from anywhere --")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# removing an item by value
# The remove() method deletes only the first occurrence of the value you specify.
#If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed.
print("\n -- removing with value --")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive) 
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")



