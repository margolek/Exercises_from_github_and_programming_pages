"""
Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

filename = r'guest.txt'

with open(filename,'w') as file_object:
	a = input('Enter your nick: ')
	file_object.write(a)


