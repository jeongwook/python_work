print('Please provide two numbers to be added')
print("Enter 'q' to quit")
while True:
	try:
		num_1 = input("\nFirst number: ")
		if num_1 == 'q':
			break
		num_1 = int(num_1)

		num_2 = input("Second number: ")
		if num_2 == 'q':
			break
		num_2 = int(num_2)
		print(num_1 + num_2)
	except ValueError:
		print("One of the values you provided is not a number\n")