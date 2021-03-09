import re
def filter1(item):
	"""
	For the given input list,
	filter all elements that start with 'den' or end with 'ly'
	items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\n', 'dent']
	"""
	regex = re.compile(r'\Aden|ly\Z')
	return [x for x in item if regex.search(x)]
def filter2(item):
	"""
	For the given list,
	filter all elements having a line starting with 'den' or ending with 'ly'.
	items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
	output = ['lovely', '1\ndentist', '2 lonely', 'fly\nfar', 'dent']
	"""
	regex = re.compile(r'^den|ly$',re.M)
	return [x for x in item if regex.search(x)]
def replace(input_string):
	"""
	For the given input strings,
	replace all occurrences of 'removed'
	or 'reed' or 'received' or 'refused' with 'X'.

	>>> s1 = 'creed refuse removed read'
	>>> s2 = 'refused reed redo received'

	output should be:
	'cX refuse X read'
	'X X redo X'
	"""
	regex = re.compile(r'removed|reed|received|refused')
	return regex.sub('X',input_string)
def replace2(input_string,words):
	"""
	For the given input strings, replace all matches from the list 'words' with 'A'.

	input:
	>>> s1 = 'plate full of slate'
	>>> s2 = "slated for later, don't be late"
	>>> words = ['late', 'later', 'slated']

	output should be:
	'pA full of sA'
	"A for A, don't be A"
	"""
	regex = re.compile('|'.join(words))
	return regex.sub('A',input_string)
def filter3(items,words):
	"""
	Filter all whole elements from the
	input list 'items' based on elements listed in 'words'.

	input:
	>>> items = ['slate', 'later', 'plate', 'late', 'slates', 'slated ']
	>>> words = ['late', 'later', 'slated']

	output should be:
	['later', 'late']
	"""
	regex = re.compile('|'.join(words))
	return [x for x in items if regex.fullmatch(x)]




