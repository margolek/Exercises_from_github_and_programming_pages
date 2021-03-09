import re
def replace(input_string):
	"""
	Replace 42//5 or 42/5 with 8 for the given input.

	input:
	ip = 'a+42//5-c pressure*3+42/5-14256'

	output:
	'a+8-c pressure*3+8-14256'
	"""
	regex = re.compile(r'42//?5')
	return regex.sub('8',input_string)

def filter(items):
	"""
	For the list 'items', filter all elements starting
	with 'hand' and ending with at most one more character or 'le'.

	input:
	items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']

	output:
	['hand', 'handy', 'hands', 'handle']
	"""
	regex = re.compile(r'^hand(.|le)?')
	return [x for x in items if regex.fullmatch(x)]

def split_met(input_string):
	"""
	Use re.split to get the output as shown for the given input strings.

	input:
	>>> eqn1 = 'a+42//5-c'
	>>> eqn2 = 'pressure*3+42/5-14256'
	>>> eqn3 = 'r*42-5/3+42///5-42/53+a'

	output:
	['a+', '-c']
	['pressure*3+', '-14256']
	['r*42-5/3+42///5-', '3+a']
	"""
	regex = re.compile(r'42//?5')
	return regex.split(input_string)
def remove(input_string):
	"""
	For the given input strings,
	remove everything from the first occurrence of 'i' till end of the string.

	input:
	>>> s1 = 'remove the special meaning of such constructs'
	>>> s2 = 'characters while constructing'

	output:
	'remove the spec'
	'characters wh'
	"""
	regex = re.compile(r'i.*')
	return regex.sub('',input_string)
def construct(input_string):
	"""
	For the given strings, construct a RE to get output as shown.

	input:
	>>> str1 = 'a+b(addition)'
	>>> str2 = 'a/b(division) + c%d(#modulo)'
	>>> str3 = 'Hi there(greeting). Nice day(a(b)'

	output:
	'a+b'
	'a/b + c%d'
	'Hi there. Nice day'
	"""
	regex = re.compile(r'\(.*?\)')
	return regex.sub('',input_string)

def correct(input_string):
	"""
	Correct the given RE to get the expected output.

	input:
	>>> words = 'plink incoming tint winter in caution sentient'
	>>> change = re.compile(r'int|in|ion|ing|inco|inter|ink')

	output:
	'plX XmX tX wX X cautX sentient'
	"""
	regex = re.compile(r'in(t|n|g|co|ter|k)?|ion')
	return regex.sub('X',input_string)

def checkpoint():
	"""
	For the given greedy quantifiers, what would be the equivalent
	form using {m,n} representation?

	? is same as --> {0,1}
	* is same as --> {0,inf}
	+ is same as --> {1,inf}

	(a*|b*) is same as (a|b)* — True or False? --> False
	"""

def remove2(input_string):
	"""
	For the given input strings, remove everything from
	the first occurrence of 'test' (irrespective of case)
	till end of the string, provided 'test' isn't at the end of the string.

	input:
	>>> s1 = 'this is a Test'
	>>> s2 = 'always test your RE for corner cases'
	>>> s3 = 'a TEST of skill tests?

	output:
	'this is a Test'
	'always '
	'a '
	"""
	regex = re.compile(r'test.+',re.I)
	return regex.sub('',input_string)

def filter2(word):
	"""
	For the input list words,
	filter all elements starting with s and containing e and t in any order.

	input:
	>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

	output:
	['subtle', 'sets', 'site']
	"""
	regex = re.compile(r'^s.*(e.*t|t.*e)')
	return [x for x in word if regex.search(x)]
def remove3(words):
	"""
	For the input list words, remove all elements having less than 6 characters.

	input:
	>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

	output:
	['sequoia', 'subtle', 'exhibit']
	"""
	regex = re.compile(r'.{6,}')
	return [x for x in words if regex.search(x)]
def filter3(words):
	"""
	For the input list words, filter all elements
	starting with s or t and having a maximum of 6 characters.

	input:
	>>> words = ['sequoia', 'subtle', 'exhibit', 'asset', 'sets', 'tests', 'site']

	output:
	['subtle', 'sets', 'tests', 'site']
	"""
	regex = re.compile(r'(s|t).{,5}')
	return [x for x in words if regex.fullmatch(x)]
def transform(input_string):
	"""
	Use re.split to get the output as shown below for given input strings.
	
	input:
	>>> s1 = 'go there  //   "this // that"'
	>>> s2 = 'a//b // c//d e//f // 4//5'
	>>> s3 = '42// hi//bye//see // carefully'

	output:
	['go there', '"this // that"']
	['a//b', 'c//d e//f // 4//5']
	['42// hi//bye//see', 'carefully']
	"""
	regex = re.compile(r' +// +')
	return regex.split(input_string,maxsplit=1)


