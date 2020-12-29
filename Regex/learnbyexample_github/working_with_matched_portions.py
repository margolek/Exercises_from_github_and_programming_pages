import re
def extract(input_string):
	"""
	For the given strings, extract the matching portion from first 'is' to last 't'.

	input:
	>>> str1 = 'This the biggest fruit you have seen?'
	>>> str2 = 'Your mission is to read and practice consistently'

	output:
	'is the biggest fruit'
	'ission is to read and practice consistent'
	"""
	regex = re.compile(r'is.*t')
	return regex.search(input_string)[0]
def find(input_string):
	"""
	Find the starting index of first occurrence
	of 'is' or 'the' or 'was' or 'to' for the given input strings.

	input:
	>>> s1 = 'match after the last newline character'
	>>> s2 = 'and then you want to test'
	>>> s3 = 'this is good bye then'
	>>> s4 = 'who was there to see?'

	output:
	12
	4
	2
	4
	"""
	regex = re.compile(r'is|the|was|to')
	return regex.search(input_string).start()
def find2(input_string):
	"""
	Find the starting index of last occurrence
	of 'is' or 'the' or 'was' or 'to' for the given input strings.

	input:
	>>> s1 = 'match after the last newline character'
	>>> s2 = 'and then you want to test'
	>>> s3 = 'this is good bye then'
	>>> s4 = 'who was there to see?'

	output:
	12
	18
	17
	14
	"""
	regex = re.compile(r'.*(is|the|was|to)')
	return regex.search(input_string).start(1)
def extract2(input_string):
	"""
	The given input string contains ':' exactly once.
	Extract all characters after the ':' as output.

	input:
	>>> ip = 'fruits:apple, mango, guava, blueberry'

	output:
	'apple, mango, guava, blueberry'
	"""
	regex = re.compile(r':(.*)')
	return regex.search(input_string).group(1)
def replace(input_string):
	"""
	The given input strings contains some text 
	followed by '-' followed by a number.
	Replace that number with its 'log' value using 'math.log()'.

	input:
	>>> s1 = 'first-3.14'
	>>> s2 = 'next-123'

	output:
	'first-1.144222799920162'
	'next-4.812184355372417'
	"""
	import math
	regex = re.compile(r'-(.*)')
	return regex.sub('-'+str(math.log(float(regex.search(input_string)[1]))),input_string)
def replace2(input_string):
	"""
	Replace all occurrences of
	'par' with 'spar',
	'spare' with 'extra'
	and 'park' with 'garden'
	for the given input strings.

	input:
	>>> str1 = 'apartment has a park'
	>>> str2 = 'do you have a spare cable'
	>>> str3 = 'write a parser'

	output:
	'aspartment has a garden'
	'do you have a extra cable'
	'write a sparser'
	"""
	regex = re.compile(r'park|spare|par')
	rep = {'par':'spare','spare':'extra','park':'garden'}
	return regex.sub(lambda x: rep[x[0]],input_string)
def extract3(input_string):
	"""
	Extract all words between '('' and ')' from the given input string as a list.
	Assume that the input will not contain any broken parentheses.

	input:
	>>> ip = 'another (way) to reuse (portion) matched (by) capture groups'

	output:
	['way', 'portion', 'by']
	"""
	regex = re.compile(r'\((.*)\)')
	return [x for x in input_string.split() if regex.search(x)]
def extract4(input_string):
	"""
	Extract all occurrences of < up to next occurrence of >,
	provided there is at least one character in between < and >.

	input:
	>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

	output:
	['<apple>', '<> b<bye>', '<> c<cat>']
	"""
	regex = re.compile(r'<.+?>')
	return regex.findall(input_string)
def find3(input_string):
	"""
	se re.findall to get the output as shown below for the given input strings.
	Note the characters used in the input strings carefully.

	input:
	>>> row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
	>>> row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

	output:
	[('-2', '5'), ('4', '+3'), ('+42', '-53'), ('4356246', '-357532354')]
	[('1.32', '-3.14'), ('634', '5.63'), ('63.3e3', '9907809345343.235')]
	"""
	regex = re.compile(r'(.+?),(.+?) ') # ? means non greedy searching
	return regex.findall(input_string)
def find3_continue(input_string):
	"""
	This is an extension to previous question.

	For row1, find the sum of integers of each tuple element.
	For example, sum of -2 and 5 is 3.

	For row2, find the sum of floating-point numbers of each tuple element.
	For example, sum of 1.32 and -3.14 is -1.82.

	input:
	>>> row1 = '-2,5 4,+3 +42,-53 4356246,-357532354 '
	>>> row2 = '1.32,-3.14 634,5.63 63.3e3,9907809345343.235 '

	output:
	[3, 7, -11, -353176108]
	[-1.82, 639.63, 9907809408643.234]
	"""
	regex = re.compile(r'(.+?),(.+?) ')
	return [float(x[0])+float(x[1]) for x in regex.findall(input_string)]
def change(input_string):
	"""
	Use re.split to get the output as shown below.

	input:
	>>> ip = '42:no-output;1000:car-truck;SQEX49801'

	output:
	['42', 'output', '1000', 'truck', 'SQEX49801']
	"""
	regex = re.compile(r';|:.+?-')
	return regex.split(input_string)

def change2(input_list):
	"""
	For the given list of strings, change the elements into a tuple of original
	element and number of times t occurs in that element.

	input:
	>>> words = ['sequoia', 'attest', 'tattletale', 'asset']

	output:
	[('sequoia', 0), ('attest', 3), ('tattletale', 4), ('asset', 1)]
	"""
	regex = re.compile(r't')
	#better option is to use subn() here
	return [(x,len(regex.findall(x))) for x in input_list]
def make_tuple(input_string):
	"""
	The given input string has fields separated by ':'.
	Each field contains four uppercase alphabets followed
	optionally by two digits. Ignore the last field, which is empty.
	See docs.python: Match.groups and use 're.finditer' to get the output
	as shown below. If the optional digits aren't present,
	show 'NA' instead of 'None'

	input:
	>>> ip = 'TWXA42:JWPA:NTED01:'

	output:
	[('TWXA', '42'), ('JWPA', 'NA'), ('NTED', '01')]
	"""
	regex = re.compile(r'(\w{4})(\d{2})?')
	return [x.groups('NA') for x in regex.finditer(input_string)]

def convert(input_string):
	"""
	Convert the comma separated strings to corresponding dict objects as shown below.

	input:
	>>> row1 = 'name:rohan,maths:75,phy:89'
	>>> row2 = 'name:rose,maths:88,phy:92'

	output:
	{'name': 'rohan', 'maths': '75', 'phy': '89'}
	{'name': 'rose', 'maths': '88', 'phy': '92'}
	"""
	regex = re.compile(r'(.+?):(.+?),|(.+?):(.+?)') #why 3rd dict element is none?
	return {x[1]:x[2] for x in regex.finditer(input_string)}
