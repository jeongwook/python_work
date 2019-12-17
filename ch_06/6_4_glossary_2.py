glossary = {
	'loops': 'allows you to loop through all values',
	'tuple': 'lists which values cannot be updated',
	'dictionary': 'list with key-pair values',
	'boolean': 'expression that evaluates to True or False',
	'conditional statement': 'code that lets you evaluate different situations and allows for different outcomes',
}

for word, definition in glossary.items():
	print("\n" + word.title() + ": " + definition + ".")