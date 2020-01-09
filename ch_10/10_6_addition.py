print('Please provide two numbers to be added')

try:
	num_1 = input("First number: ")
	num_1 = int(num_1)

	num_2 = input("Second number: ")
	num_2 = int(num_2)
	print(num_1 + num_2)
except ValueError:
	print("One of the values you provided is not a number")

