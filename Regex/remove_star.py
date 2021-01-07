

import re

def find_character():
	""" Create own class to delete all '*' """
	regex = re.compile(r'[^*]')
	return regex.findall('R*emo*ve a*ll* *fro*m in*p*ut *strin*g')


a = find_character()
print("".join(a))
