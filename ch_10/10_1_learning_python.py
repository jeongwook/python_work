filename = 'learning_python.txt'

print("-- Print once by reading in the entire file --")
with open(filename) as file_object:
	lines = file_object.read()
	print(lines.rstrip())

print("\n-- Print by looping over the file object --")
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())	

print("\n-- Print by storing in a list --")
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())	
