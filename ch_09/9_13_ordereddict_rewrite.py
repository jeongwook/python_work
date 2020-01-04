from collections import OrderedDict

glossary = OrderedDict()

glossary['loops'] = 'allows you to loop through all values'
glossary['tuple'] = 'lists which values cannot be updated'
glossary['dictionary'] = 'list with key-pair values'
glossary['boolean'] = 'expression that evaluates to True or False'
glossary['conditional statement'] = 'code that lets you evaluate different situations and allows for different outcomes'

for word, definition in glossary.items():
	print("\n" + word.title() + ": " + definition + ".")