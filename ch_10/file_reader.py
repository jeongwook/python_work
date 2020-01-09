# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip())

# Reading line by line
filename = 'pi_digits.txt'

# with open(filename) as file_object:
# 	for line in file_object:
# 		print(line.rstrip())

# Making a List of Lines from a File
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

