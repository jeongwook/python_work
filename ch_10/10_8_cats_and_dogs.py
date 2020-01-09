filenames = ['cats.txt', 'dogs.txt', 'hamsters.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			print(filename.title() + "'s contents: ")
			for line in f:
				print(line.rstrip())
			print()
	except FileNotFoundError:
		print("File " + filename + " is missing.")