number = input("Enter a number, and I'll tell you if it's a multiple of 10: ") 
number = int(number)

if number % 10 == 0:
	print("Your number is a multiple of 10.")
else:
	print("Your number is not a multiple of 10.")