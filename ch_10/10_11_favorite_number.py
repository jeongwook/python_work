import json

filename = 'favorite_number.txt'
number = input("What is your favorite number? ")
with open(filename, 'w') as f:
	json.dump(number, f)

