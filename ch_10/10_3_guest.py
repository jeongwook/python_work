name = input("What is your name?\n")

filename = "guest.txt"

with open(filename, 'w') as file_object:
	file_object.write(name)