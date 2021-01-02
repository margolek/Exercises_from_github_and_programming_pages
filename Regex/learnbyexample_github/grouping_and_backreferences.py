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
	regex = re.compile(r'\b(\d+)\1+\b')
	return regex.sub('\g<1>',ip),regex.findall(ip)
def replace4(ip):
	"""
	Replace sequences made up of words separated by ':' or '.' by
	the first word of the sequence. Such sequences will end when ':' or '.'
	is not followed by a word character.

	input:
	>>> ip = 'wow:Good:2_two:five: hi-2 bye kite.777.water.'

	output:
	'wow hi-2 bye kite'
	"""
	regex = re.compile(r'(\w+)[:.](\w+[:.])+')
	return regex.sub('\g<1>', ip)
def split(ip):
	"""
	Split the given input string on one or more repeated sequence of cat.

	input:
	>>> ip = 'firecatlioncatcatcatbearcatcatparrot'

	output:
	['fire', 'lion', 'bear', 'parrot']
	"""
	regex = re.compile(r'(?:cat)+')
	return regex.split(ip)
def find(ip):
	"""
	For the given input string, find all occurrences of digit sequences with
	at least one repeating sequence. For example, '232323' and '897897'. If the
	repeats end prematurely, for example '12121', it should not be matched.

	input:
	>>> ip = '1234 2323 453545354535 9339 11 60260260'

	output:
	['2323', '453545354535', '11']
	['23', '4535', '1']
	"""
	regex = re.compile(r'\b(\d+)\1+\b')
	return [x[0] for x in regex.finditer(ip)],regex.findall(ip)
def convert(ip):
	"""
	Convert the comma separated strings to corresponding 'dict' objects as shown below.
	The keys are 'name', 'maths' and 'phy' for the three fields in the input strings.

	input:
	>>> row1 = 'rohan,75,89'
	>>> row2 = 'rose,88,92'

	output:
	{'name': 'rohan', 'maths': '75', 'phy': '89'}
	{'name': 'rose', 'maths': '88', 'phy': '92'}
	"""
	regex = re.compile(r'(\w+),(\d+),(\d+)')
	return {'name':regex.search(ip)[1],'maths':regex.search(ip)[2],
	'phy':regex.search(ip)[3]}
def surround(ip):
	"""
	Surround all whole words with ().
	Additionally, if the whole word is imp or ant, delete them.
	Can you do it with single substitution?

	input:
	ip = 'tiger imp goat eagle ant important'

	output:
	'(tiger) () (goat) (eagle) () (important)'
	"""
	regex1 = re.compile(r'(\b\w+\b)')
	regex2 = re.compile(r'(\(imp\)|\(ant\))')
	sub1 = regex1.sub('(\g<1>)', ip)
	return regex2.sub('()', sub1)
def filter(ip):
	"""
	Filter all elements that contains a sequence of lowercase
	alphabets followed by - followed by digits. They can be optionally
	surrounded by {{ and }}. Any partial match shouldn't be part of the output.

	input:
	>>> ip = ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']

	output:
	['{{apple-150}}', 'grape-87']
	"""
	regex = re.compile(r'({{[a-z]+-\d+}})|(\w+-\d+)')
	return [x for x in ip if regex.fullmatch(x)]
def display(ip):
	"""
	The given input string has sequences made up of words separated by : or .
	and such sequences will end when : or . is not followed by a word character.
	For all such sequences, display only the last word followed by - followed by
	first word.

	input:
	>>> ip = 'wow:Good:2_two:five: hi-2 bye kite.777.water.'

	output:
	['five-wow', 'water-kite']
	"""
	regex = re.compile(r'(\w+)[:.](?:(\w+)[:.])+')
	return [x.expand(r'\2-\1') for x in regex.finditer(ip)]

a = display('wow:Good:2_two:five: hi-2 bye kite.777.water.')
print(a)


