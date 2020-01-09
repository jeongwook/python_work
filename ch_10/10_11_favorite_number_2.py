import json

filename = 'favorite_number.txt'
with open(filename) as f:
	fav_num = json.load(f)
	print("I know your favorite number! It's " + str(fav_num) + ".")