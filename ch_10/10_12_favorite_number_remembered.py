import json

filename = 'favorite_number.txt'

def get_fav_num():
	"""Return user's favorite number if available"""
	filename = 'favorite_number.txt'
	try:
		with open(filename) as f:
			num = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return num

def get_new_fav_num():
	"""Get new favorite number."""
	filename = 'favorite_number.txt'
	num = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(num, f)
	return num

def report_fav_num():
	"""Report user's favorite number"""
	num = get_fav_num()
	if num:
		print("I know your favorite number! It's " + str(num) + ".")
	else:
		get_new_fav_num()

report_fav_num()