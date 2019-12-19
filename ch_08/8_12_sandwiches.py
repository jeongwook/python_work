def sandwiches(*items):
	"""Output the type of sandwich based on items given"""
	print("Making your sandwich which consists of: ")
	for item in items:
		print("- " + item)

	print()

sandwiches('lettuce', 'tomato', 'onions', 'cheese', 'ham')