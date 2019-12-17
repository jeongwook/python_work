sandwich_orders = ['BLT', 'pastrami', 'ham and cheese', 'bacon cheese avacado', 
	'pastrami', 'caprese', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrammi.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print("I made your " + sandwich + " sandwich.")
	finished_sandwiches.append(sandwich)

print("\n--- sandwiches made ---")
for sandwich in finished_sandwiches:
	print(sandwich.title() + " sandwich was made.")
