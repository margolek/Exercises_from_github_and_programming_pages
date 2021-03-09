"""

Modify your except block in Exercise 50 to fail
silently if either file is missing.

"""

def call_cat():
	cat_filename = 'cat.txt'
	try:
		with open(cat_filename) as cat_object:
			cat = cat_object.readlines()
	except FileNotFoundError:
		pass
	else:
		for i in cat:
			print(i.strip())

def call_dog(filename,todo):
	try:
		with open(filename,todo) as file_object:
			dog = file_object.readlines()
	except FileNotFoundError:
		pass
	else:
		for i in dog:
			print(i.strip())


call_dog('krowa.txt','r')
