responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	vacation = input("If you could visit one place in the world, where would you go? ")
	responses[name] = vacation

	repeat = input("Would someone else like to take the poll? (yes/no) ")
	if repeat == 'no':
		polling_active = False


print("\n--- Polling Results---")
for name, response in responses.items():
	print(name +"'s dream vacation is " + response + ".")