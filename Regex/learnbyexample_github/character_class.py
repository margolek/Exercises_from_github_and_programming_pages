import re
def filter(input_list):
	"""
	For the list 'items',
	filter all elements starting with 'hand' and ending with 's' or 'y' or 'le'.

	input:
	>>> items = ['-handy', 'hand', 'handy', 'unhand', 'hands', 'handle']

	output:
	['handy', 'hands', 'handle']
	"""
	regex = re.compile(r'hand(s|y|le)')
	return [x for x in input_list if regex.fullmatch(x)]
def replace(input_string):
	"""
	Replace all whole words 'reed' or 'read' or 'red' with 'X'.

	input:
	>>> ip = 'redo red credible :read: rod reed'

	output:
	'redo X credible :X: rod X'
	"""
	regex = re.compile(r'\bre(ed|ad|d)\b')
	return regex.sub('X',input_string)
def filter2(input_list):
	"""
	For the list words, filter all elements containing
	'e' or 'i' followed by 'l' or 'n'. Note that the order
	mentioned should be followed.

	input:
	>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

	output:
	['surrender', 'unicorn', 'eel']
	"""
	regex = re.compile(r'[ei].*[ln]')
	return [x for x in input_list if regex.search(x)]
def filter3(input_list):
	"""
	For the list words, filter all elements
	containing 'e' or 'i' and 'l' or 'n' in any order.

	input:
	>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']
	
	output:
	['surrender', 'unicorn', 'newer', 'eel']
	"""
	regex = re.compile(r'[e|i][l|n]|[l|n][e|i]')
	return [x for x in input_list if regex.search(x)]
def extract(input_string):
	"""
	Extract all hex character sequences, with '0x' optional prefix.
	Match the characters case insensitively, and the sequences
	shouldn't be surrounded by other word characters.

	input:
	>>> str1 = '128A foo 0xfe32 34 0xbar'
	>>> str2 = '0XDEADBEEF place 0x0ff1ce bad'

	output:
	['128A', '0xfe32', '34']
	['0XDEADBEEF', '0x0ff1ce', 'bad']

	"""
	regex = re.compile(r'\b(0x)?[\da-f]+\b',re.I)
	#0 in x[0] means whole part of chosen pattern
	# \b....\b is better option than split() method
	return [x[0] for x in regex.finditer(input_string)] 
def delete(input_string):
	"""
	Delete from '(' to the next occurrence of ')' unless they
	contain parentheses characters in between.

	input:
	>>> str1 = 'def factorial()'
	>>> str2 = 'a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)'
	>>> str3 = 'Hi there(greeting). Nice day(a(b)'

	output:
	'def factorial'
	'a/b + c%d - (e+*4)'
	'Hi there. Nice day(a'
	"""
	regex = re.compile(r'\([^()]*\)')
	return regex.sub('',input_string)
def filter4(input_list):
	"""
	For the list words, filter all elements not starting with 'e' or 'p' or 'u'.

	input:
	>>> words = ['surrender', 'unicorn', 'newer', 'door', 'empty', 'eel', 'pest']

	output:
	['surrender', 'newer', 'door']
	"""
	regex = re.compile(r'^[^epu]')
	return [x for x in input_list if regex.search(x)]
def filter5(input_list):
	"""
	For the list words, filter all elements
	not containing 'u' or'w' or 'ee' or '-'.

	input:
	words = ['p-t', 'you', 'tea', 'heel', 'owe', 'new', 'reed', 'ear']

	output:
	['tea', 'ear']
	"""
	regex = re.compile(r'[uw-]|ee')
	# why [^uw-]|ee do not work?
	return [x for x in input_list if not regex.search(x)]
def replace2(input_string):
	"""
	The given input strings contain fields separated by','
	and fields can be empty too. Replace last three fields with 'WHTSZ323'.

	input:
	>>> row1 = '(2),kite,12,,D,C,,'
	>>> row2 = 'hi,bye,sun,moon'

	output:
	'(2),kite,12,,D,WHTSZ323'
	'hi,WHTSZ323'
	"""
	regex = re.compile(r'(,[^,]*){3}$')
	return regex.sub(',WHTSZ323',input_string)
def split(input_string):
	"""
	Split the given strings based on consecutive
	sequence of digit or whitespace characters.

	input:
	>>> str1 = 'lion \t Ink32onion Nice'
	>>> str2 = '**1\f2\n3star\t7 77\r**'

	output:
	['lion', 'Ink', 'onion', 'Nice']
	['**', 'star', '**']
	"""
	regex = re.compile(r'[\s\d]+')
	return regex.split(input_string)
def delete(input_string):
	"""
	Delete all occurrences of the sequence <characters> where characters
	is one or more non > characters and cannot be empty.

	input:
	>>> ip = 'a<apple> 1<> b<bye> 2<> c<cat>'

	output:
	'a 1<> b 2<> c'
	"""
	regex = re.compile(r'<[^>]+>')
	return regex.sub('', input_string)
def filter6(input_list):
	"""
	For the given list, filter all elements containing
	any number sequence greater than 624.

	input:
	>>> items=['hi0000432abcd', 'car00625', '42_624 0512','3.14 96 2 foo1234baz']
	
	output:
	['car00625', '3.14 96 2 foo1234baz']
	"""
	#focus more on this example
	return [e for e in input_list if any(int(m[0])>624 for m in re.finditer(r'\d+', e))]
def max_nested_braces(ip):
	"""
	Count the maximum depth of nested braces for the given strings.
	Unbalanced or wrongly ordered braces should return '-1'.
	Note that this will require a mix of regular expressions and Python code.

	input:
	'a*b'
	'}a+b{'
	'a*b+{}'
	'{{a+2}*{b+c}+e}'
	'{{a+2}*{b+{c*d}}+e}'
	'{{a+2}*{\n{b+{c*d}}+e*d}}'
	'a*{b+c*{e*3.14}}}'

	output:
	0
	-1
	1
	2
	3
	4
	-1
	"""
	regex = re.compile(r'\{[^{}]*\}')
	regex_alt = re.compile(r'[{}]')
	count = 0
	while True:
		ip,subs_num =  regex.subn('', ip)
		if subs_num == 0:
			break
		count+=subs_num
	if regex_alt.search(ip):
		return -1
	return count
def check_point(ip):
	"""
	By default, 'str.split' method will split on whitespace
	and remove empty strings from the result.
	Which 're' module function would you use to replicate this functionality?
	
	input:
	>>> ip = ' \t\r  so  pole\t\t\t\n\nlit in to \r\n\v\f  '

	output:
	split()
	['so', 'pole', 'lit', 'in', 'to']
	Add solution here
	['so', 'pole', 'lit', 'in', 'to']
	"""
	regex = re.compile(r'\S+')
	return regex.findall(ip)
def convert(ip):
	"""
	Convert the given input string to two different lists as shown below.
	
	input:
	ip = 'price_42 roast^\t\n^-ice==cat\neast'

	output:
	['price_42', 'roast', 'ice', 'cat', 'east']
	['price_42', ' ', 'roast', '^\t\n^-', 'ice', '==', 'cat', '\n', 'east']
	"""
	regex1 = re.compile(r'[\s==^-]+')
	regex2 = re.compile(r'([\s==^-]+)')
	#put question about it
	return regex1.split(ip),regex2.split(ip)
def filter7(ip):
	"""
	Filter all elements whose first non-whitespace
	character is not a # character.
	Any element made up of only whitespace characters should be ignored as well.

	input:
	items = ['    #comment', '\t\napple #42', '#oops', 'sure', 'no#1', '\t\r\f']

	output:
	['\t\napple #42', 'sure', 'no#1']
	"""
	regex = re.compile(r'\A\s*[^#\s]')
	#why \s in own class?
	return [x for x in ip if regex.search(x)]


