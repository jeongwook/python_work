sandwich_orders = ['BLT', 'ham and cheese', 'bacon cheese avacado', 'caprese']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print("I made your " + sandwich + " sandwich.")
	finished_sandwiches.append(sandwich)

print("\n--- sandwiches made ---")
for sandwich in finished_sandwiches:
	print(sandwich.title() + " sandwich was made.")
