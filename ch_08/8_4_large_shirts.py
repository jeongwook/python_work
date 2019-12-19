def make_shirt(size='large', message='I love Python'):
	"""Summarize the size of the shirt and the message printed on it."""
	print("Your shirt size is " + size + " and has " + '"' +
		message + '"' + " written on it.")

make_shirt()
make_shirt('medium')
make_shirt('small', 'I love coding')