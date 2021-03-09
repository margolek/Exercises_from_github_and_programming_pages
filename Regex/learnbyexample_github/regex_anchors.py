import re
def check(line):
	"""
	Check if the given strings start with 'be'
	>>> line1 = 'be nice'
	>>> line2 = '"best!"'
	>>> line3 = 'better?'
	>>> line4 = 'oh no\nbear spotted'
	"""
	regex = re.compile(r'^be')
	return True if regex.search(line) else False
def replace(input):
	"""
	For the given input string, change only whole word 'red' to 'brown'
	words = 'bred red spread credible'
	"""
	regex = re.compile('\bred\b')
	return regex.sub('brown',input)
def filter(word):
	"""
	For the given input list, filter all elements
	that contains 42 surrounded by word characters.
	words = ['hi42bye', 'nice1423', 'bad42', 'cool_42a', 'fake4b']
	"""
	regex = re.compile(r'\w42\w')
	return [x for x in word if regex.search(x)]
def filter2(word):
	"""
	For the given input list, filter all elements
	that start with 'den' or end with 'ly'.
	items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
	"""
	regex = re.compile(r'\Aden|ly\Z')
	return [x for x in word if regex.search(x)]
def change():
	"""
	For the given input string,
	change whole word 'mall' to '1234' 
	only if it is at the start of a line.
	"""
	filename = r'data2.txt'
	with open(filename) as file_object:
		lines = file_object.readlines()

	regex = re.compile(r'\A\bmall\b')
	return [regex.sub('1234',x) for x in lines]
def filter3(item):
	"""
	For the given list,
	filter all elements having a line starting with den or ending with ly.
	items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
	"""
	regex = re.compile('^den|ly$',re.M)
	return [x for x in item if regex.search(x)]
def filter4(item):
	"""
	For the given input list,
	filter all whole elements '12\nthree' irrespective of case.
	items = ['12\nthree\n', '12\nThree', '12\nthree\n4', '12\nthree']
	"""
	regex = re.compile(r'12\nthree',re.I)
	return [x for x in item if regex.fullmatch(x)]
def replace2(item):
	"""
	For the given input list, replace 'hand' with 'X'
	for all elements that start with 'hand' followed by at least one word character.
	items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
	"""
	regex = re.compile(r'\bhand\B')
	return [regex.sub('X',x) for x in item]
def filter5(item):
	"""
	For the given input list, filter all elements starting with h.
	Additionally, replace e with X for these filtered elements.
	items = ['handed', 'hand', 'handy', 'unhanded', 'handle', 'hand-2']
	"""
	regex = re.compile(r'^h')
	return [re.sub('e','X',x) for x in item if regex.search(x)]
