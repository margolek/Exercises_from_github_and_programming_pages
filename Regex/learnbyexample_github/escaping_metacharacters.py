import re
def transform1(input_string):
	"""
	Transform the given
	input strings to the expected output using same logic on both strings.

	input:
	>>> str1 = '(9-2)*5+qty/3'
	>>> str2 = '(qty+4)/2-(9-2)*5+pq/4'

	output should be:
	'35+qty/3'
	'(qty+4)/2-35+pq/4'
	"""
	
	return input_string.replace('(9-2)*5','35')
def replace(input_string):
	"""
	Replace '(4)\|' with '2' only at the start or end of given input strings.

	input:
	>>> s1 = r'2.3/(4)\|6 foo 5.3-(4)\|'
	>>> s2 = r'(4)\|42 - (4)\|3'
	>>> s3 = 'two - (4)\\|\n'

	output:
	'2.3/(4)\\|6 foo 5.3-2'
	'242 - (4)\\|3'
	'two - (4)\\|\n'
	"""
	regex = re.compile(r'^\(4\)\\\||\(4\)\\\|$')
	return regex.sub('2',input_string)
def replace2(input_string,items):
	"""
	Replace any matching element from the list 'items' with 'X'
	for given the input strings. Match the elements from 'items' literally.
	Assume no two elements of 'items' will result in any matching conflict.

	input:
	>>> items = ['a.b', '3+n', r'x\y\z', 'qty||price', '{n}']
	input string:
	'0a.bcd'
	'E{n}AMPLE'
	r'43+n2 ax\y\ze'

	output string:
	'0Xcd'
	'EXAMPLE'
	'4X2 aXe'
	
	"""
	regex = re.compile('|'.join(re.escape(e) for e in items))
	return regex.sub('X',input_string)
def replace3(input_string):
	"""
	Replace backspace character '\b''
	with a single space character for the given input string.

	input:
	ip = '123\b456'

	output:
	'123 456'
	"""
	regex = re.compile(r'\x08')
	return regex.sub(' ',input_string)
def replace4(input_string):
	"""
	Replace all occurrences of \e with e.

	input:
	ip = r'th\er\e ar\e common asp\ects among th\e alt\ernations'

	output:
	'there are common aspects among the alternations'
	"""
	regex = re.compile(re.escape('\e'))
	return regex.sub('e',input_string)
def replace5(input_string,eqns):
	"""
	Replace any matching item from the list
	'eqns' with 'X' for given the string 'ip'.
	Match the items from 'eqns' literally.

	input:
	>>> ip = '3-(a^b)+2*(a^b)-(a/b)+3'
	>>> eqns = ['(a^b)', '(a/b)', '(a^b)+2']

	output:
	'3-X*X-X+3'
	"""
	regex = re.compile('|'.join(re.escape(x) for x in eqns))
	return regex.sub('X',input_string)


	