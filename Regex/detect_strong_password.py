"""

Create a function that checks their new password (passed as a string)
to make sure it meets the following requirements:

Between 8 - 20 characters
Contains only the following characters (and at least one character from each category):
uppercase letters,
lowercase letters,
digits,
special characters from !@#$%^&*?

"""
import re

def check_password(s):
	regex1 = re.compile(r'[A-Z]')
	regex2 = re.compile(r'[a-z]')
	regex3 = re.compile(r'[0-9]')
	regex4 = re.compile(r'[!@#?$%&*^]')
	regex5 = re.compile(r'[^a-zA-Z0-9!@#?$%&*^]')

	if regex1.search(s) and regex2.search(s) and regex3.search(s) and regex4.search(s) and not regex5.search(s):
		if len(s) >= 8 and len(s) <=20:
			return 'valid'
		else:
			return 'not valid'
	else:
		return 'not valid'



a = check_password('valid')
print(a)