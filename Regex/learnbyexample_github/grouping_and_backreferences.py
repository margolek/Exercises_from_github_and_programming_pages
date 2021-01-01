import re
def replace(ip):
	"""
	Replace the space character that occurs after a word
	ending with 'a' or 'r' with a newline character.

	input:
	>>> ip = 'area not a _a2_ roar took 22'

	output:
	area
	not a
	_a2_ roar
	took 22
	"""
	regex = re.compile(r'([ar]) ')
	return regex.sub('\1\n', ip)
def add(ip):
	"""
	Add [] around words starting with s and containing e and t in any order.

	input:
	>>> ip = 'sequoia subtle exhibit asset sets tests site'

	output:
	'sequoia [subtle] exhibit asset [sets] tests [site]'
	""" 
	regex = re.compile(r'\bs\w*(\w*e\w*t|\w*t\w*e)\w*')
	return regex.sub('[\g<0>]', ip)
def replace2(ip):
	"""
	Replace all whole words with 'X' that start and end
	with the same word character.
	Single character word should get replaced with 'X' too, as it satisfies
	the stated condition.

	input:
	>>> ip = 'oreo not a _a2_ roar took 22'

	output:
	'X not X X X took X'
	"""

	regex = re.compile(r'\b(\w)(\w*\1)?\b')
	return regex.sub('X', ip)
def convert(ip):
	#Do skończenia
	"""
	Convert the given markdown headers to corresponding anchor tag.
	Consider the input to start with one or more '#' characters followed
	by space and word characters. The 'name' attribute is constructed by
	converting the header to lowercase and replacing spaces with hyphens.
	Can you do it without using a capture group?

	input:
	>>> header1 = '# Regular Expressions'
	>>> header2 = '## Compiling regular expressions'

	output:
	'# <a name="regular-expressions"></a>Regular Expressions'
	'## <a name="compiling-regular-expressions"></a>Compiling regular expressions'
	"""
	regex = re.compile(r'(#+) (((\b\w+\b) |(\b\w+\b))+)')
	m = regex.search(ip)
	return f'{m[1]} <a name="{m[2].lower().replace(" ","-")}></a>{m[2]}'
def convert2(ip):
	"""
	Convert the given markdown anchors to corresponding hyperlinks.

	input:
	>>> anchor1 = '# <a name="regular-expressions"></a>Regular Expressions'
	>>> anchor2 = '## <a name="subexpression-calls"></a>Subexpression calls'

	output:
	'[Regular Expressions](#regular-expressions)'
	'[Subexpression calls](#subexpression-calls)'
	"""
	regex = re.compile(r'(#+).*("(.*)").*(</a>(.*))')
	m = regex.search(ip)

	return f'[{m[5]}]({m[1]}{m[3]})'
def count():
	"""
	Count the number of whole words that have at least two occurrences
	of consecutive repeated alphabets. For example, words like 'stillness' and
	'Committee' should be counted but not words like
	'root' or 'readable' or 'rotational'.
	"""
	filename = r'data3.txt'
	with open(filename) as file_obj:
		text = file_obj.read()

	regex = re.compile(r'\b(\w*(\w)\2){2}\w*\b')
	return len(regex.findall(text))
def replace3(ip):
	"""
	For the given input string, replace all occurrences of digit sequences
	with only the unique non-repeating sequence. For example, '232323' should
	be changed to '23' and '897897' should be changed to '897'. If there no repeats
	(for example '1234') or if the repeats end prematurely (for example '12121'),
	it should not be changed.

	input:
	>>> ip = '1234 2323 453545354535 9339 11 60260260'

	output:
	'1234 23 4535 9339 1 60260260'
	"""



