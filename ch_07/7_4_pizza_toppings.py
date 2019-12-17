active = True
prompt = "\nPlease enter the pizza topping you would like: "
prompt += "\nEnter 'quit' to end the program. "

while active:
	message = input(prompt)

	if message.lower() == 'quit':
		active = False
	else:
		print("We will add " + message + " to your pizza.")


