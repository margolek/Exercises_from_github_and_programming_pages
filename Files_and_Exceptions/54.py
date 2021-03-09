"""

Combine the two programs from
Exercise 53 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.

"""
import json


def checknumber(filename):

	try:
		with open(filename) as js_obj:
			number = json.load(js_obj)
			print('Your favourite number is: {}'.format(number))

	except FileNotFoundError:
		print('There is not file name "{}". Create new.'.format(filename))
		a = input('Put your value: ')
		with open(filename,'w') as js_obj:
			number = json.dump(a,js_obj)

checknumber('number.json')