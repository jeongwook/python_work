filename = "guest_book.txt"

while True:
	name = input("What is your name? Enter 'quit' when done\n")
	if name == 'quit':
		break
	else: 
		print("Hello " + name)
		with open(filename, 'a') as f:
			f.write(name + "\n")

