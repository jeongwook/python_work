current_users = ['JUAN', 'jason', 'dave', 'josh', 'jin']
new_users = ['juan', 'JASON', 'sung', 'KEVIN', 'rodney']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
	if user.lower() in current_users_lower:
		print("Username " + user + " is not available. Please enter a new username.")
	else:
		print("Username " + user + " is available.")