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
def filter4():
	"""
	or the list words, filter all elements not starting with e or p or u.
