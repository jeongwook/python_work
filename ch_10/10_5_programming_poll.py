filename = 'programming_poll.txt'

while True:
	reason = input('Why do you like programming? Enter "quit" when done\n')
	if reason == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(reason + "\n")
