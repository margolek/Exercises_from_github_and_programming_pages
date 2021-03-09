import re
def replace(ip):
	"""
	Replace all whole words with 'X' unless it is preceded by '(' character.

	input:
	>>> ip = '(apple) guava berry) apple (mango) (grape'

	output:
	'(apple) X X) X (mango) (grape'
	"""
	regex = re.compile(r'(?<!\()(\b\w+\b)')
	return regex.sub('X', ip)
def replace2(ip):
	"""
	Replace all whole words with 'X' unless it is followed by ')' character.

	input:
	>>> ip = '(apple) guava berry) apple (mango) (grape'

	
	output:
	'(apple) X berry) X (mango) (X'
	"""
	regex = re.compile(r'(\b\w+\b)(?!\))')
	return regex.sub('X', ip)
def replace3(ip):
	"""
	Replace all whole words with 'X' unless it
	is preceded by '(' or followed by ')' characters.

	input:
	>>> ip = '(apple) guava berry) apple (mango) (grape'

	output:
	'(apple) X berry) X (mango) (grape'
	"""
	regex = re.compile(r'(?<!\()(\b\w+\b)(?!\))')
def extract(ip):
	"""
	Extract all whole words that do not end with e or n.

	input:
	>>> ip = 'at row on urn e note dust n'
	
	output:
	['at', 'row', 'dust']
	"""
	regex = re.compile(r'\b\w+\b(?<![en])')
	return regex.findall(ip)
def extract2(ip):
	"""
	Extract all whole words that do not start with a or d or n.

	input:
	>>> ip = 'at row on urn e note dust n'

	output:
	['row', 'on', 'urn', 'e']
	"""
	regex = re.compile(r'(?![adn])\b\w+\b')
	return regex.findall(ip)
def extract3(ip):
	"""
	Extract all whole words only if they are followed by : or , or -.

	input:
	>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

	output:
	['poke', 'so', 'ever']
	"""
	regex = re.compile(r'(\w+)(?=[:,-])')
	return regex.findall(ip)
def extract4(ip):
	"""
	Extract all whole words only if they are preceded by '=' or '/' or '-'.

	input:
	>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

	output:
	['so', 'is', 'sit']
	"""
	regex = re.compile(r'(?<=[=/-])(\w+)')
	return regex.findall(ip)
def extract5(ip):
	"""
	Extract all whole words only if
	they are preceded by '=' or ':' and followed by ':' or '.'.

	input:
	>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

	output:
	['so', 'ink']
	"""
	regex = re.compile(r'(?<=[=:])(\w+)(?=[:\.])')
	return regex.findall(ip)
def extract6(ip):
	"""
	Extract all whole words only if they
	are preceded by '=' or ':' or '.' or '(' or '-' and not
	followed by '.' or '/'.

	input:
	>>> ip = 'poke,on=-=so:ink.to/is(vast)ever-sit'

	output:
	['so', 'vast', 'sit']
	"""
	regex = re.compile(r'(?<=[=\.\(-])(\w+\b)(?![./])')
	return regex.findall(ip)
def remove(ip):
	"""
	Remove leading and trailing whitespaces from all the individual
	fields where ',' is the field separator.

	input:
	>>> csv1 = ' comma  ,separated ,values \t\r '
	>>> csv2 = 'good bad,nice  ice  , 42 , ,   stall   small'

	output:
	'comma,separated,values'
	'good bad,nice  ice,42,,stall   small'
	"""
	regex = re.compile(r'(?<![^,])\s+|\s+(?![^,])')
	return regex.sub('', ip)
def filter(ip):
	"""
	Filter all elements that satisfy all of these rules:

	1)should have at least two alphabets
	2)should have at least 3 digits
	3)should have at least one special character
	among '%' or '*' or '#' or '$'
	4)should not end with a whitespace character

	input:
	>>> pwds = ['hunter2', 'F2H3u%9', '*X3Yz3.14\t', 'r2_d2_42', 'A $B C1234']

	output:
	['F2H3u%9', 'A $B C1234']
	"""
	regex = re.compile(r'(?=(.*[a-zA-Z]){2,})(?=(.*[0-9]){3,})(?=(.*[%*#$]){1,})(?!.*\s\Z)')
	return [x for x in ip if regex.search(x)]
def surround(ip):
	"""
	For the given string, surround
	all whole words with '{}' except for whole
	words 'par' and 'cat' and 'apple'.

	input:
	>>> ip = 'part; cat {super} rest_42 par scatter apple spar'

	output:
	'{part}; cat {{super}} {rest_42} par {scatter} apple {spar}'
	"""
	regex = re.compile(r'\b(?!(?:par|cat|apple)\b)\w+\b')
	return regex.sub('{\g<0>}', ip)
def extract7(ip):
	"""
	Extract integer portion of floating-point numbers for the given string.
	A number ending with '.' and no further digits should not be considered.
	
	input:
	>>> ip = '12 ab32.4 go 5 2. 46.42 5'

	output:
	['32', '46']
	"""
	regex = re.compile(r'(\d+)\.(?:\d+)')
	return regex.findall(ip)
def extract8(ip):
	"""
	For the given input strings, extract all
	overlapping two character sequences.

	input:
	>>> s1 = 'apple'
	>>> s2 = '1.2-3:4'

	output:
	['ap', 'pp', 'pl', 'le']
	['1.', '.2', '2-', '-3', '3:', ':4']
	"""
	regex = [ip[x:x+2] for x in range(len(ip))]
	del regex[-1]
	return regex
def extract9(ip):
	"""
	Extract all whole words unless they
	are preceded by ':' or '<=>' or '----' or '#'.

	input:
	>>> ip = '::very--at<=>row|in.a_b#b2c=>lion----east'

	output:
	['at', 'in', 'a_b', 'lion']
	"""
	regex = re.compile(r'(?<!:)(?<!<=>)(?<!----)(?<!#)\b\w+')
	return regex.findall(ip)

