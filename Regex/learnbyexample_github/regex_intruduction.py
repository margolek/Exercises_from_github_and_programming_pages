
import re
def check(line):
	"""
	Check whether the given strings contain 0xB0.
	Display a boolean result as shown below.

	>>> line1 = 'start address: 0xA0, func1 address: 0xC0'
	>>> line2 = 'end address: 0xFF, func2 address: 0xB0'

	"""
	regex = re.compile(r'0xC0')
	if regex.search(line):
		return True
	else:
		return False
def replace(text):
	""" Replace all occurrences of 5 with five for the given string."""
	regex = re.compile(r'5')
	return regex.sub('five',text)
def replace2(text):
	"""
	Replace first occurrence of 5 with five for the given string.
	string = 'They ate 5 apples and 5 oranges'
	"""
	regex = re.compile(r'5')
	return regex.sub('five',text,count=1)
def filter(mylist):
	"""
	For the given list, filter all elements that do not contain e.
	items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
	"""
	regex = re.compile('e')
	return [x for x in mylist if not regex.search(x)]
def replace3(ip):
	"""
	Replace all occurrences of note irrespective of case with X.
	ip = 'This note should not be NoTeD'
	"""
	regex = re.compile(r'note',re.I)
	return regex.sub('X',ip)
def check2(ip):
	"""
	Check if at is present in the given byte input data.
	ip = b'tiger imp goat'
	"""
	regex = re.compile(rb'at')
	if regex.search(ip):
		return True
	else:
		return False
def display():
	"""
	For the given input string, display all lines not containing
	start irrespective of case.

		>>> para = 'good start
		Start working on that
		project you always wanted
		stars are shining brightly
		hi there
		start and try to
		finish the book
		bye'
	"""
	filename = r'data_for_regex_example.txt'
	with open(filename) as file_object:
		lines = file_object.readlines()
	regex = re.compile(r'start',re.I)
	return [x.rstrip() for x in lines if not regex.search(x)]
def filter2(item):
	"""
	For the given list, filter all elements that contains either a or w.
	items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
	"""
	regex = re.compile(r'a|w')
	return [x for x in item if regex.search(x)]
def filter3(item):
	"""
	For the given list, filter all elements that contains both e and n.
	items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
	"""
	regex1 = re.compile(r'e')
	regex2 = re.compile(r'n')
	return [x for x in item if regex1.search(x) and regex2.search(x)]
def replace4(ip):
	"""
	For the given string, replace 0xA0 with 0x7F and 0xC0 with 0x1F.
	ip = 'start address: 0xA0, func1 address: 0xC0'
	"""
	regex1 = re.compile('0xA0')
	regex2 = re.compile('0xC0')
	return re.sub(regex1,'0x7F',re.sub(regex2,'0x1F',ip))


