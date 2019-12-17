favorite_numbers = {
	'jason' : [3, 12],
	'jin' : [0, 32],
	'dave' : [1, 25],
	'josh' : [2, 61],
	'rodney' : [13, 8],
}

for name, numbers in favorite_numbers.items():
	print(name.title() + "'s favorite numbers are:")
	for number in numbers:
		print("\t" + str(number).title())