"""

One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.

"""

def add(*args):
	sum = 0
	try:
		for i in args:
			sum+=i
		print('Your sum is: {}'.format(sum))
	except TypeError:
		print('Wrong type of input argument')
	





add(2,2,3,4,5,'h')