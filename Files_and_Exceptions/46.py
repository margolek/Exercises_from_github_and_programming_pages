"""
Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = r'guest_book.txt'

with open(filename,'w') as file_object:
	while True:
		print(r'Hey user, can u pass your nick? or click "q" to close programm')
		nick = input()
		if nick == 'q':
			break
		else:
			print(r'Thanks for register in our page')
			print()
			file_object.write(nick + '\n')