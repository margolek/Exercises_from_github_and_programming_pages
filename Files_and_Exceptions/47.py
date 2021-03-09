"""
Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'responses.txt'

with open(filename,'w') as file_object:

	while True:
		reason = input('Add reason why you like programming or quit programm using "q": ')
		if reason != 'q':
			file_object.write(reason + '\n')
		else:
			break
