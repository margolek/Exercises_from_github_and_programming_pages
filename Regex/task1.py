import re


def find_my_pattern(input):
	""" Find a number as a form nn nnn"""
	regex = re.compile(r'(\d{2}) (\d{3})')
	output = regex.findall(input)
	return output


a = find_my_pattern('My first numper is 22 333 but friend of mine has 32 433 phone number')
print(a)