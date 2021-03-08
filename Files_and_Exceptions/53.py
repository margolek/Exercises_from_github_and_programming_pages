"""

Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite
number! It’s _____.”

"""
import json

def makenumber(input):

		number = input
		filename = 'number.json'
		with open(filename,'w') as js_obj:
			json.dump(number,js_obj)


def readnumber(filename):

	with open(filename) as js_obj:
		number = json.load(js_obj)
		print('I know your favourite number is {}'.format(number))

	
makenumber(5)
readnumber('number.json')

