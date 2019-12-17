prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
	age = input(prompt)

	if age == 'quit':
		break
	elif int(age) < 3:
		print("Your ticket is free.")
	elif int(age) < 13:
		print("Your ticket is $10.")
	elif int(age) >= 13:
		print("Your ticket is $15.")

